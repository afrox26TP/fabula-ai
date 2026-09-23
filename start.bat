@echo off
cd /d "%~dp0"
rem Model loaded at startup; any other .gguf in models\ can be picked in the app
set "MODEL=models\Impish-Bloodmoon-12B-Q6_K.gguf"
if not exist "%MODEL%" for %%f in (models\*.gguf) do set "MODEL=%%f"
rem fabula.kcpps holds the GPU/context settings; --baseconfig reapplies them on every model switch
start "KoboldCpp" koboldcpp\koboldcpp.exe --config fabula.kcpps --baseconfig fabula.kcpps --model "%MODEL%" --admin --admindir models --host 127.0.0.1 --port 5001 --skiplauncher
python server.py
pause
