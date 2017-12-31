
import json, urllib
import logging
from Player import Player

def createPlayerDict(date):
    from nba_py import game
    
    player_dict = {}
    
    for id in getGameIDs(date):
        logging.info("Processing game: " + id)
        boxscore = game.Boxscore(id)
        player_stats = boxscore.player_stats()
        for index in range(0, len(player_stats["PLAYER_NAME"])):
            logging.info("Processing player: " + player_stats["PLAYER_NAME"][index])
            if(player_stats["MIN"][index] != None):
                tempPlayer = Player()
                tempPlayer.setStats(player_stats, index)
                player_dict[tempPlayer.PLAYER_ID] = tempPlayer
    
    
    logging.info("Player dict successfully created.")
    return player_dict
        
        
def getGameIDs(date):
    url = "http://data.nba.net/10s/prod/v1/" + date + "/scoreboard.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    returnList = []
    for i in range(0, data["numGames"]):
        returnList.append(data["games"][i]["gameId"])
        
    return returnList
