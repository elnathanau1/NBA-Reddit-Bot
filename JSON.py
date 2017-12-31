import json, logging
from Player import Player

def exportJSON(player_list, file_name):
    data = {}
    for key in player_list.keys():
        tempPlayer = {}
        tempPlayer["PLAYER_NAME"] = player_list[key].PLAYER_NAME
        tempPlayer["PLAYER_ID"] = player_list[key].PLAYER_ID
        tempPlayer["TEAM_ID"] = player_list[key].TEAM_ID
        tempPlayer["TEAM_ABBREVIATION"] = player_list[key].TEAM_ABBREVIATION
        tempPlayer["BOX_SCORE"] = player_list[key].boxScore
        tempPlayer["CAREER_HIGH"] = player_list[key].careerHigh
        tempPlayer["SEASON_AVERAGE"] = player_list[key].seasonAverage
        data[key] = tempPlayer
    
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)
        
    logging.info("Exported JSON to " + file_name + " successfully")
    
def importJSON(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        
    player_list = {}
    for key in data.keys():
        tempPlayer = Player()
        tempPlayer.PLAYER_NAME = data[key]["PLAYER_NAME"]
        tempPlayer.PLAYER_ID = data[key]["PLAYER_ID"]
        tempPlayer.TEAM_ID = data[key]["TEAM_ID"]
        tempPlayer.TEAM_ABBREVIATION = data[key]["TEAM_ABBREVIATION"]
        tempPlayer.boxScore = data[key]["BOX_SCORE"]
        tempPlayer.careerHigh = data[key]["CAREER_HIGH"]
        tempPlayer.seasonAverage = data[key]["SEASON_AVERAGE"]
        player_list[key] = tempPlayer
     
     
    logging.info("Imported " + file_name + " successfully")   
    return player_list