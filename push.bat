@echo off
chcp 65001 >nul
echo ========================================
echo   Skills 一键推送到 GitHub
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] 添加所有文件到 Git...
git add -A

echo.
echo [2/3] 提交更改...
echo 请输入提交信息（直接回车使用默认信息）:
set /p COMMIT_MSG=
if "%COMMIT_MSG%"=="" set COMMIT_MSG=chore: 更新 skills

git commit -m "%COMMIT_MSG%"

echo.
echo [3/3] 推送到 GitHub...
git push

echo.
echo ========================================
echo   完成！按任意键退出...
echo ========================================
pause >nul
