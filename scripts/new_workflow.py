#!/usr/bin/env python3
"""Create a dynamic workflow artifact directory."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def slugify(value: str) -> str:
    """Convert title to safe directory slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:72].strip("-") or "workflow"


def validate_path_component(name: str, component_type: str) -> str:
    """
    Validate a path component to prevent path traversal attacks.

    Raises ValueError if the component contains dangerous patterns.
    """
    if not name:
        raise ValueError(f"{component_type} cannot be empty")

    # Block obvious path traversal patterns
    dangerous_patterns = ["..", "~", "$"]
    for pattern in dangerous_patterns:
        if pattern in name:
            raise ValueError(f"{component_type} contains forbidden pattern '{pattern}': {name}")

    # Block absolute paths
    if name.startswith("/") or (len(name) > 1 and name[1] == ":"):
        raise ValueError(f"{component_type} must be a relative path, not: {name}")

    # Block null bytes (common injection technique)
    if "\0" in name:
        raise ValueError(f"{component_type} contains null byte (injection attempt)")

    # Block common dangerous names (but allow "." as it's a valid relative path)
    forbidden_names = {
        "", "CON", "PRN", "AUX", "NUL",
        "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9",
    }
    if name.upper() in forbidden_names:
        raise ValueError(f"{component_type} is a reserved name: {name}")

    return name


def safe_resolve(root: Path, relative_path: str) -> Path:
    """
    Safely resolve a path, ensuring it stays within the root directory.

    This prevents path traversal attacks like ../../../etc/passwd
    """
    # Normalize and resolve the root directory
    try:
        root_resolved = root.resolve()
    except (OSError, RuntimeError) as e:
        raise ValueError(f"Cannot resolve root path: {e}")

    # Build the target path
    target = root_resolved / relative_path

    # Check that the final path is within the root
    try:
        target_resolved = target.resolve()
    except (OSError, RuntimeError) as e:
        raise ValueError(f"Cannot resolve target path: {e}")

    # Ensure the resolved path starts with the root
    try:
        target_resolved.relative_to(root_resolved)
    except ValueError:
        raise ValueError(
            f"Path escape attempt detected: '{relative_path}' "
            f"resolves outside allowed directory '{root_resolved}'"
        )

    return target_resolved


def write_new(path: Path, content: str) -> None:
    """Write content to a file only if it doesn't exist (no overwrite)."""
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Security notes:
  - Only creates directories within the specified root (default: .workflow)
  - Prevents path traversal attacks (e.g., ../../../etc)
  - Cannot overwrite existing files or directories
  - Rejects reserved filenames and absolute paths
        """
    )
    parser.add_argument("title", help="Workflow title or task summary")
    parser.add_argument(
        "--root",
        default=".workflow",
        help="Workflow root directory (default: .workflow)"
    )
    parser.add_argument("--slug", help="Optional explicit workflow slug")
    args = parser.parse_args()

    try:
        # Validate root path
        root_input = validate_path_component(args.root, "Root path")

        # Create root path (will be resolved for security checks)
        root_path = Path(root_input)

        # Validate and sanitize slug
        slug_input = args.slug or args.title
        slug = slugify(slug_input)

        # Additional validation: slug should only contain safe chars
        if not re.match(r"^[a-z0-9][a-z0-9-]*$", slug) and slug != "workflow":
            raise ValueError(f"Generated slug is invalid: {slug}")

        # Safe path resolution - this is the key security check
        run_dir = safe_resolve(root_path, slug)

        # Define subdirectories
        packets_dir = run_dir / "packets"
        results_dir = run_dir / "results"

        # Create directories (parents=True is safe because we validated the path)
        packets_dir.mkdir(parents=True, exist_ok=False)
        results_dir.mkdir(parents=True, exist_ok=False)

        # Create workflow state
        now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        state = {
            "title": args.title,
            "slug": slug,
            "created_at": now,
            "status": "planned",
            "approval": {"required": None, "granted": None, "notes": ""},
            "packets": [],
            "verification": {"status": "not_started", "checks": []},
        }

        # Create workflow files
        write_new(
            run_dir / "plan.md",
            f"""# {args.title}

## Goal

## Success Criteria

## Audience

## Current Context

## Constraints

## Risks

## Approval Required

## Work Packets

## Integration Policy

## Verification

## Final Deliverable
""",
        )
        write_new(
            run_dir / "orchestration.md",
            f"""# Orchestration: {args.title}

## Sequence

## Branching Rules

## Packet Prompts

## Integration Notes
""",
        )
        write_new(
            run_dir / "final-report.md",
            f"""# Final Report: {args.title}

## Completed

## Evidence

## Verification

## Skipped Checks

## Remaining Risks

## Next Step
""",
        )
        write_new(run_dir / "state.json", json.dumps(state, indent=2) + "\n")

        print(run_dir)
        return 0

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"File system error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
