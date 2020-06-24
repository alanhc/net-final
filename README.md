# net-final
以聊天機器人為介面的虛擬化雲服務系統
為解決實驗室多人使用同一台主機，而又不想使用一般的雲服務(GCP、AWS、Azure)。本系統以telegram為指令終端介面、使用虛擬的容器化技術，希望透過container的隔離方式做到安全、快速且有效的個人化私有雲服務系統。

## Pre-requirements
make sure you have these requirements:
* docker
* pipenv
 

1. use ngrok to port forwarding
```
ngrok run http 5000
```
2. set up
setup telegram api
```
https://api.telegram.org/bot{bot_token}/setWebhook?url=https://{url}/hook
```
setup config.ini
```
ACCESS_TOKEN = {bot_token}
```
3. run
```
pipenv install
pipenv run python main.py
```
