# NBA Reddit Bot

Reddit bot written for /r/nba. Calculates the players that played better/worse than their season averages, and outputs a table with statistics from stats.nba.com (using nba_py). Uses praw to post comment into the Next Day Thread on /r/nba

## Getting Started

Go to https://www.reddit.com/prefs/apps, and click “create an app”. Record the client_id, client_secret, and your reddit user/pass in praw.ini under [bot1]. 

Make sure to update file_name with the correct file path in bot.py


## Built With

* [nba_py](https://github.com/seemethere/nba_py) - NBA Stats API
* [praw](https://github.com/praw-dev/praw) - Reddit API

## Author
Elnathan Au (eau3)
12/30/17