import praw

import logging
import json
from pandas.compat import FileNotFoundError

# submission: 7n6m8k

def formatList(over_list, under_list, player_list):
    date = getDate()
    returnString = "#Player performances for " + date[4:6] + "/" + date[6:8] + "/" + date[0:4]
    returnString += "\n\n---\n\n"
    returnString += "Players that played much **better** than their season average: \n\n"
    returnString += "NAME|TEAM|MIN|PTS|FG|3PT|REB|AST|STL|BLK|TOV|\n"
    returnString += ":--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|\n"
    
    for pair in over_list:
        (key, value) = pair
        returnString += str(player_list[key].PLAYER_NAME) + "|"
        returnString += str(player_list[key].TEAM_ABBREVIATION) + "|"
        returnString += str(player_list[key].boxScore["MIN"]) + "|"
        returnString += str(int(player_list[key].boxScore["PTS"])) + "|"
        returnString += str(int(player_list[key].boxScore["FGM"])) + "-" + str(int(player_list[key].boxScore["FGA"])) + "|"
        returnString += str(int(player_list[key].boxScore["FG3M"])) + "-" + str(int(player_list[key].boxScore["FG3A"])) + "|"
        returnString += str(int(player_list[key].boxScore["REB"])) + "|"
        returnString += str(int(player_list[key].boxScore["AST"])) + "|"
        returnString += str(int(player_list[key].boxScore["STL"])) + "|"
        returnString += str(int(player_list[key].boxScore["BLK"])) + "|"
        returnString += str(int(player_list[key].boxScore["TOV"])) + "\n"
        returnString += "Season Average:|"
        returnString += "|"
        returnString += str(player_list[key].seasonAverage["MIN"]) + "|"
        returnString += str(player_list[key].seasonAverage["PTS"]) + "|"
        returnString += str(player_list[key].seasonAverage["FGM"]) + "-" + str(player_list[key].seasonAverage["FGA"]) + "|"
        returnString += str(player_list[key].seasonAverage["FG3M"]) + "-" + str(player_list[key].seasonAverage["FG3A"]) + "|"
        returnString += str(player_list[key].seasonAverage["REB"]) + "|"
        returnString += str(player_list[key].seasonAverage["AST"]) + "|"
        returnString += str(player_list[key].seasonAverage["STL"]) + "|"
        returnString += str(player_list[key].seasonAverage["BLK"]) + "|"
        returnString += str(player_list[key].seasonAverage["TOV"]) + "\n"
        returnString += "|||||||||||\n"
        
    returnString = returnString[:-12]
    
    returnString += "\n\n---\n\n"
    
    returnString += "Players that played much **worse** than their season average: \n\n"
    returnString += "NAME|TEAM|MIN|PTS|FG|3PT|REB|AST|STL|BLK|TOV|\n"
    returnString += ":--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|\n"
    
    for pair in under_list:
        (key, value) = pair
        returnString += str(player_list[key].PLAYER_NAME) + "|"
        returnString += str(player_list[key].TEAM_ABBREVIATION) + "|"
        returnString += str(player_list[key].boxScore["MIN"]) + "|"
        returnString += str(int(player_list[key].boxScore["PTS"])) + "|"
        returnString += str(int(player_list[key].boxScore["FGM"])) + "-" + str(int(player_list[key].boxScore["FGA"])) + "|"
        returnString += str(int(player_list[key].boxScore["FG3M"])) + "-" + str(int(player_list[key].boxScore["FG3A"])) + "|"
        returnString += str(int(player_list[key].boxScore["REB"])) + "|"
        returnString += str(int(player_list[key].boxScore["AST"])) + "|"
        returnString += str(int(player_list[key].boxScore["STL"])) + "|"
        returnString += str(int(player_list[key].boxScore["BLK"])) + "|"
        returnString += str(int(player_list[key].boxScore["TOV"])) + "\n"
        returnString += "Season Average:|"
        returnString += "|"
        returnString += str(player_list[key].seasonAverage["MIN"]) + "|"
        returnString += str(player_list[key].seasonAverage["PTS"]) + "|"
        returnString += str(player_list[key].seasonAverage["FGM"]) + "-" + str(player_list[key].seasonAverage["FGA"]) + "|"
        returnString += str(player_list[key].seasonAverage["FG3M"]) + "-" + str(player_list[key].seasonAverage["FG3A"]) + "|"
        returnString += str(player_list[key].seasonAverage["REB"]) + "|"
        returnString += str(player_list[key].seasonAverage["AST"]) + "|"
        returnString += str(player_list[key].seasonAverage["STL"]) + "|"
        returnString += str(player_list[key].seasonAverage["BLK"]) + "|"
        returnString += str(player_list[key].seasonAverage["TOV"]) + "\n"
        returnString += "|||||||||||\n"
        
    returnString = returnString[:-12]
    
    returnString += "\n\n---\n\n"
    
    returnString += "*^These ^tables ^were ^generated ^by ^a ^bot ^for ^discussion ^purposes ^only. ^Contact ^/u/etau97hi1 ^for ^any ^questions, ^concerns, ^or ^suggestions*"
    return returnString
    
    
def postComment(submissionID, text):
    try:
        with open('/Users/eau/Documents/eau3/Eclipse Workspace/NBA Reddit Bot/written_submissions.txt', 'r') as file:
            submissions = json.load(file)
            
    except FileNotFoundError:
        submissions = []
    
    if submissionID not in submissions:
        reddit = praw.Reddit('bot1')
        submission = reddit.submission(submissionID)
        submission.reply(text)
        logging.info("Posted in submission " + submissionID)
        
        submissions.append(submissionID)
        
        with open('/Users/eau/Documents/eau3/Eclipse Workspace/NBA Reddit Bot/written_submissions.txt', 'w') as file:
            json.dump(submissions, file)
        
    else:
        logging.warning("Have already posted at " + submissionID + " before")
    
def getNextDayThreadID():
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit("nba")
    
    for i in range(1, 10):
        submission = reddit.submission(id = subreddit.sticky(number = i))
        title = submission.title
        if title[:17] == "[Next day thread]":
            return submission.id
        
def getDate():
    from datetime import date, timedelta
    yesterday = date.today() - timedelta(days = 1)
    
    returnString = '20' + yesterday.strftime('%y%m%d')
    logging.info("Found date: " + returnString)
    return returnString
    