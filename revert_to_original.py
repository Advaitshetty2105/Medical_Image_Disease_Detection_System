# -*- coding: utf-8 -*-
"""
MediScan AI - One-Click Hard Revert Script
Hard-reverts the local repository and GitHub origin fork back to the original upstream state (commit d96f5c1).
"""

import subprocess
import sys
import os

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
UPSTREAM_COMMIT = "d96f5c1"

def run_cmd(cmd):
    print(f">> Running: {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=REPO_DIR, text=True)
    if res.returncode != 0:
        print(f"[ERROR] Command failed with exit code {res.returncode}")
        return False
    return True

def main():
    print("=" * 60)
    print("  MEDISCAN AI - ONE-CLICK HARD REVERT UTILITY")
    print("=" * 60)
    print("This will HARD REVERT your repository back to the exact")
    print(f"upstream commit: {UPSTREAM_COMMIT} (DeeppParmar/main).")
    print("All added tests, CI workflows, and modifications will be")
    print("completely erased and reset line-by-line.")
    print("=" * 60)

    # 1. Save backup branch
    print('\n[1/4] Ensuring backup branch "backup-features" is saved...')
    run_cmd("git branch -f backup-features HEAD")

    # 2. Hard reset to upstream
    print(f"\n[2/4] Hard resetting working tree and index to {UPSTREAM_COMMIT}...")
    if not run_cmd(f"git reset --hard {UPSTREAM_COMMIT}"):
        print("Aborting due to reset failure.")
        sys.exit(1)

    # 3. Clean untracked files
    print("\n[3/4] Cleaning all untracked files and directories...")
    run_cmd("git clean -fd")

    # 4. Force push to origin
    print("\n[4/4] Force-pushing reset state to origin main...")
    run_cmd("git push origin main --force")

    print("\n" + "=" * 60)
    print("SUCCESS: Repository has been hard-reverted to original upstream!")
    print("A backup of your changes was preserved in branch: backup-features")
    print("To restore your features anytime, run: restore_backup_features.bat")
    print("=" * 60)

if __name__ == '__main__':
    main()
