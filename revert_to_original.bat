@echo off
setlocal
cd /d "%~dp0"

echo ============================================================
echo   MEDISCAN AI - ONE-CLICK HARD REVERT TO ORIGINAL REPOSITORY
echo ============================================================
echo This will completely wipe all recent changes line-by-line
echo and reset your repository and origin fork to DeeppParmar's commit.
echo.
echo A local backup will be saved to branch: backup-features
echo ============================================================
echo.

set /p CONFIRM="Are you sure you want to hard revert? (y/n): "
if /i not "%CONFIRM%"=="y" (
    echo Cancelled by user.
    pause
    exit /b 0
)

echo.
echo [1/4] Saving backup branch backup-features...
git branch -f backup-features HEAD

echo.
echo [2/4] Hard resetting repository to original upstream commit (d96f5c1)...
git reset --hard d96f5c1

echo.
echo [3/4] Cleaning all untracked files and directories...
git clean -fd

echo.
echo [4/4] Force pushing reverted state to origin main...
git push origin main --force

echo.
echo ============================================================
echo Hard revert complete! Your repository matches DeeppParmar:main.
echo Backup preserved in: backup-features
echo ============================================================
pause
