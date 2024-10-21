REM @ECHO OFF

where /q pixi.exe
IF %ERRORLEVEL% NEQ 0 (
    ECHO Install pixi first: https://pixi.sh/latest/
    PAUSE
    EXIT /B
)

pixi.exe run python ./convert.py %*
