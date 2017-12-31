#!/usr/bin/env python

import nba
import JSON
import Reddit
import logging

import datetime

def main():
    #set up logger
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(filename='/Users/eau/Documents/eau3/Eclipse Workspace/NBA Reddit Bot/ProcessLog.log', format='%(levelname)s:%(message)s', filemode='w', level=logging.INFO)
    
    logging.info("Last run: " + str(datetime.datetime.now()))
    
    #get yesterday's date
    date = Reddit.getDate()
    
    #try to open the file. If it exists, just import it. Otherwise, create it and export to JSON
    file_name = '/Users/eau/Documents/eau3/Eclipse Workspace/NBA Reddit Bot/player_list_' + date + '.json'
    try:
        with open(file_name, 'r') as file:
            player_list = JSON.importJSON(file_name)
    except:
        player_list = nba.createPlayerDict(date)
        JSON.exportJSON(player_list, file_name)
    
    #get the score for each player, put them into score_list
    score_list = {}
    for key in player_list.keys():
        score = player_list[key].getScore()
        score_list[key] = score
        
    
    #sort the lists, getting the top (list_size) number of players
    list_size = 6
    over_list = sorted(score_list.iteritems(), key = lambda x:-x[1])[:list_size]
    under_list = sorted(score_list.iteritems(), key = lambda x:-x[1], reverse = True)[:list_size]
    
    #create the text to be posted
    formattedText = Reddit.formatList(over_list, under_list, player_list)
    
    #post the comment
    Reddit.postComment(Reddit.getNextDayThreadID(), formattedText)
     
    
main()
        
        
    
    
