from nba_py import player

# class that holds player data taken from stats.nba.com
class Player:
    
    #constructor, set up dictionaries
    def __init__(self):
        self.PLAYER_NAME = ""
        self.PLAYER_ID = ""
        self.TEAM_ID = ""
        self.TEAM_ABBREVIATION = ""
        
        self.boxScore = {}
        self.careerHigh = {}
        self.seasonAverage = {}
        
    
    def setStats(self, player_stats, index):
        self.setBoxScore(player_stats, index)
        
        player_career = player.PlayerCareer(self.PLAYER_ID)
        regular_season_totals = player_career.regular_season_totals()
        
        self.setSeasonAverage(regular_season_totals)
        
        
    def setBoxScore(self, player_stats, index):
        for key in player_stats.keys():
            self.boxScore[key] = player_stats[key][index]
            
        self.boxScore[u'TOV'] = self.boxScore["TO"]
        self.PLAYER_NAME = self.boxScore["PLAYER_NAME"]
        self.PLAYER_ID = self.boxScore["PLAYER_ID"]
        self.TEAM_ID = self.boxScore["TEAM_ID"]
        self.TEAM_ABBREVIATION = self.boxScore["TEAM_ABBREVIATION"]
        
    def setSeasonAverage(self, regular_season_totals):
        for key in regular_season_totals.keys():
            self.seasonAverage[key] = regular_season_totals[key][len(regular_season_totals[key])-1]
        
        
    def getScore(self):
        if(self.boxScore["MIN"] == None):
            return 0

        gameFGA = self.boxScore["FGA"]
        gameFGM = self.boxScore["FGM"]
        gameFTA = self.boxScore["FTA"]
        gameFTM = self.boxScore["FTM"]
        gameFG3M = self.boxScore["FG3M"]
        gamePTS = self.boxScore["PTS"]
        gameREB = self.boxScore["REB"]
        gameAST = self.boxScore["AST"]
        gameSTL = self.boxScore["STL"]
        gameBLK = self.boxScore["BLK"]
        gameTOV = self.boxScore["TOV"]
        gameScore = -0.45 * gameFGA + gameFGM -0.75 * gameFTA + gameFTM + 3.0 * gameFG3M + 0.5 * gamePTS + 1.5 * gameREB + 2.0 * gameAST + 3.0 * gameSTL + 3.0 * gameBLK - 2.0 * gameTOV
        
        seasonFGA = self.seasonAverage["FGA"]
        seasonFGM = self.seasonAverage["FGM"]
        seasonFTA = self.seasonAverage["FTA"]
        seasonFTM = self.seasonAverage["FTM"]
        seasonFG3M = self.seasonAverage["FG3M"]
        seasonPTS = self.seasonAverage["PTS"]
        seasonREB = self.seasonAverage["REB"]
        seasonAST = self.seasonAverage["AST"]
        seasonSTL = self.seasonAverage["STL"]
        seasonBLK = self.seasonAverage["BLK"]
        seasonTOV = self.seasonAverage["TOV"]
        seasonScore = -0.45 * seasonFGA + seasonFGM -0.75 * seasonFTA + seasonFTM + 3.0 * seasonFG3M + 0.5 * seasonPTS + 1.5 * seasonREB + 2.0 * seasonAST + 3.0 * seasonSTL + 3.0 * seasonBLK - 2.0 * seasonTOV
        
        return gameScore - seasonScore
    