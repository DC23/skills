"""
Two-phase release script for DC23/skills.

Usage:
    python scripts/bump_release.py vX.Y.Z [--dry-run]

Manual verification steps:
    1. Run with --dry-run to inspect all commands before execution.
    2. Confirm the pyproject.toml bump-my-version config targets the correct line
       in scripts/install-dc23-skills.sh before running for real.
    3. After Phase 1, verify the PR diff shows only the VERSION change.
    4. After Phase 2, confirm `git tag` lists the expected tag on the correct
       main commit.
"""

import re
import subprocess
import sys
from pathlib import Path

INSTALLER = "scripts/install-dc23-skills.sh"
VENV_BMV = Path(__file__).parent / "venv" / "bin" / "bump-my-version"

_SEMVER_RE = re.compile(r"^v\d+\.\d+\.\d+$")


def validate_version(version: str) -> None:
    """Exit with an error if version is not a valid vX.Y.Z semver string."""
    if not _SEMVER_RE.match(version):
        sys.exit(f"Error: '{version}' is not a valid version. Expected format: vX.Y.Z")


def assert_installer_version(installer_path: str, expected: str) -> None:
    """Exit with an error if VERSION in the installer doesn't match expected."""
    text = Path(installer_path).read_text()
    match = re.search(r'VERSION="([^"]+)"', text)
    if not match:
        sys.exit(f"Error: no VERSION= line found in {installer_path}")
    actual = match.group(1)
    if actual != expected:
        sys.exit(
            f"Error: VERSION in {installer_path} is '{actual}', expected '{expected}'.\n"
            "Did you forget to merge the release branch before tagging?"
        )


def _remote_url() -> str:
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        capture_output=True, text=True, check=True,
    )
    url = result.stdout.strip()
    # Normalise SSH to HTTPS for display
    url = re.sub(r"^git@github\.com:", "https://github.com/", url)
    url = re.sub(r"\.git$", "", url)
    return url


def phase1_commands(version: str) -> list[str]:
    """Return the shell commands that Phase 1 would execute (for dry-run / tests)."""
    branch = f"release/{version}"
    return [
        f"git checkout -b {branch}",
        f"{VENV_BMV} bump --new-version {version}",
        f"git push -u origin {branch}",
    ]


def phase2_commands(version: str) -> list[str]:
    """Return the shell commands that Phase 2 would execute (for dry-run / tests)."""
    return [
        "git checkout main",
        "git pull --rebase",
        f"git tag {version}",
        f"git push --tags",
    ]


def _run(cmd: str) -> None:
    subprocess.run(cmd, shell=True, check=True)


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("-")]

    if not args:
        sys.exit("Usage: python scripts/bump_release.py vX.Y.Z [--dry-run]")

    version = args[0]
    validate_version(version)

    print(f"\n=== Phase 1: bump VERSION and open PR for {version} ===\n")
    for cmd in phase1_commands(version):
        if dry_run:
            print(f"  [dry-run] {cmd}")
        else:
            _run(cmd)

    if dry_run:
        remote = "https://github.com/DC23/skills"
        branch = f"release/{version}"
        print(f"\n  [dry-run] PR URL would be: {remote}/compare/{branch}")
        print("\n  [dry-run] Skipping Phase 2 in dry-run mode.")
        return

    try:
        remote = _remote_url()
    except subprocess.CalledProcessError:
        remote = "https://github.com/DC23/skills"

    branch = f"release/{version}"
    print(f"\nPR URL: {remote}/compare/{branch}")
    input("\nMerge the PR, then press Enter to continue to Phase 2...\n")

    print(f"\n=== Phase 2: tag {version} on main ===\n")
    _run("git checkout main")
    _run("git pull --rebase")

    assert_installer_version(INSTALLER, version)

    _run(f"git tag {version}")
    _run("git push --tags")
    print(f"\nDone. {version} tagged and pushed.")


if __name__ == "__main__":
    main()
