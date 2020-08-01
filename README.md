# swipe-bot for Tinder

To make it work:
1. download chromedriver depend on your Chrome on https://chromedriver.chromium.org/downloads, unzip and move to `/usr/local/bin` (mac os / linux)

2.Install selenium on Python3.7+:
``` 
pip install selenium
```
3. create a "secrets.py" file in project folder with your Facebook login into Tinder:
``` 
 username = 'your_username'
 password = 'your_password'
```
You are ready to go!



You can easily add your cron job on your Ubuntu by run 'crontab -e' in terminal. 
And put inside:
```
0 */13 * * * export DISPLAY=:0 && export PATH=$PATH:/usr/local/bin && /usr/bin/python3 /path/to/swipe-bot/swipe-bot.py
```
