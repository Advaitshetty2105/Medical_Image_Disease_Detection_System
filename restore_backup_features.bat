@echo off
setlocal
cd /d "%~dp0"

echo ============================================================
echo   MEDISCAN AI - ONE-CLICK RESTORE BACKUP FEATURES
echo ============================================================
echo This will restore all your features from branch: backup-features
echo back onto your main branch and push to origin.
echo ============================================================
echo.

git checkout main
git reset --hard backup-features
git push origin main

echo.
echo ============================================================
echo Features restored successfully!
echo ============================================================
pause
