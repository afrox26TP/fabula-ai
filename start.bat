@echo off
cd /d "%~dp0"
start "KoboldCpp" koboldcpp\koboldcpp.exe --model models\Cydonia-24B-v4.3-IQ4_XS.gguf --usecuda --gpulayers -1 --contextsize 16384 --quantkv q8_0 --port 5001 --skiplauncher
python server.py
pause
