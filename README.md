# swipe-bot

To make it work:
1. download chromedriver depend on your Chrome on https://chromedriver.chromium.org/downloads, unzip and move to `/usr/local/bin` (mac os / linux)

2.Install selenium on Python3.7+ that you will use:
``` 
pip install selenium
```
3. create a "secrets.py" file with variables in project directory with your Facebook login:
``` 
 username = 'your_username'
 password = 'your_password'
```
Now you can run it.



You can easily add your cron job by on your Ubuntu by run 'crontab -e' in terminal. 
And put inside:
```
0 */13 * * * export DISPLAY=:0 && export PATH=$PATH:/usr/local/bin && /usr/bin/python3 /home/mike/git/swipe-bot/swipe-bot.py
```
last path should be path to your script, and before it you specify path to your python with selenium. 
