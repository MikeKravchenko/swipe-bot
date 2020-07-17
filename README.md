# swipe-bot

to run:
 - download chromedriver, unzip, move to `/usr/local/bin` (mac os / linux)
 - `pip install selenium`

create a secrets.py file with variables:
``` 
 username = 'your_username'
 password = 'your_password'
```

You can easy add your cron job by:

- 'crontab -e' 

and put insede:

- 0 */13 * * * export DISPLAY=:0 && export PATH=$PATH:/usr/local/bin && /usr/bin/python3 /home/mike/git/swipe-bot/swipe-bot.py
