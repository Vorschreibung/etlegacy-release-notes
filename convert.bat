@ECHO OFF

where /q pixi.exe
IF %ERRORLEVEL% NEQ 0 (
    ECHO Install pixi first: https://pixi.sh/latest/
    ECHO Or simply download and rename to 'pixi.exe' and place it next to 'convert.bat'.
    PAUSE
    EXIT /B
)

pixi.exe run python ./convert.py %*
