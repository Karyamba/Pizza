@echo off

call %~dp0D:\Pizza\venv\Scripts\activate

cd %~dpD:\0Pizza

set TOKEN=5898593098:AAGTg179orUU4cnveAw1abVViL_n2t2ecPE

python bot_telegram.py

pause