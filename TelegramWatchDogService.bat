setlocal
d:
echo %~dp0 src
cd %~dp0src
python ./watchDogTelegramService.py