"""Tests for scripts/bump-release.py — all non-destructive (no git ops, no file mutations)."""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import bump_release


class TestVersionValidation:
    def test_rejects_missing_v_prefix(self):
        with pytest.raises(SystemExit):
            bump_release.validate_version("1.2.3")

    def test_rejects_non_semver(self):
        with pytest.raises(SystemExit):
            bump_release.validate_version("vfoo")

    def test_rejects_partial_semver(self):
        with pytest.raises(SystemExit):
            bump_release.validate_version("v1.2")

    def test_accepts_valid_version(self):
        bump_release.validate_version("v1.2.3")

    def test_accepts_multi_digit_parts(self):
        bump_release.validate_version("v10.20.300")


class TestVersionAssertion:
    def test_assertion_passes_when_version_matches(self, tmp_path):
        installer = tmp_path / "install.sh"
        installer.write_text('VERSION="v2.0.0"\n')
        bump_release.assert_installer_version(str(installer), "v2.0.0")

    def test_assertion_fails_on_mismatch(self, tmp_path):
        installer = tmp_path / "install.sh"
        installer.write_text('VERSION="v1.0.0"\n')
        with pytest.raises(SystemExit):
            bump_release.assert_installer_version(str(installer), "v2.0.0")

    def test_assertion_fails_when_version_line_absent(self, tmp_path):
        installer = tmp_path / "install.sh"
        installer.write_text("# no version here\n")
        with pytest.raises(SystemExit):
            bump_release.assert_installer_version(str(installer), "v2.0.0")


class TestDryRun:
    def test_phase1_dry_run_returns_commands(self):
        cmds = bump_release.phase1_commands("v1.3.0")
        assert any("release/v1.3.0" in c for c in cmds)
        assert any("bump-my-version" in c for c in cmds)
        assert any("push" in c for c in cmds)

    def test_phase2_dry_run_returns_commands(self):
        cmds = bump_release.phase2_commands("v1.3.0")
        assert any("checkout main" in c or "checkout" in c for c in cmds)
        assert any("pull" in c for c in cmds)
        assert any("tag" in c and "v1.3.0" in c for c in cmds)
        assert any("push" in c and "tag" in c for c in cmds)
