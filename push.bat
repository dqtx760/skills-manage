@echo off
chcp 65001 >nul
echo ========================================
echo   Skills 一键推送到 GitHub
echo ========================================
echo.

cd /d "%~dp0"

echo [1/4] 拉取远程更新...
git pull origin master --allow-unrelated-histories
if errorlevel 1 (
    echo 拉取失败，可能是没有远程仓库，先跳过
    echo.
)

echo [2/4] 添加所有文件到 Git...
git add -A

echo.
echo [3/4] 提交更改...
echo 请输入提交信息（直接回车使用默认信息）:
set /p COMMIT_MSG=
if "%COMMIT_MSG%"=="" set COMMIT_MSG=chore: 更新 skills

git commit -m "%COMMIT_MSG%"
if errorlevel 1 (
    echo 没有需要提交的内容，跳过
    echo.
)

echo.
echo [4/4] 推送到 GitHub...
git push

echo.
echo ========================================
echo   完成！按任意键退出...
echo ========================================
pause >nul
