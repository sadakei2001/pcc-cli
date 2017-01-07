@echo off

set PROGRAM_DIR=%~d0%~p0

python %PROGRAM_DIR%..\src\pcc\driver.py %*
