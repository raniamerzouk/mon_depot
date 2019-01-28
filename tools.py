from soccersimulator import *

class SuperState(object):
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player

    @property
    def ball(self):
        return self.state.ball.position

    @property
    def player(self):
        return self.state.player_state(self.id_team,self.id_player).position
    
    @property
    def goal(self):
        if id_team == 1:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2)
        else:
            return Vector2D(0, GAME_HEIGHT/2)

    def aller_vers_point(self, b):
        return SoccerAction(accelereation=Vector2D(self-b))
    
    def shooter_vers_but(self, b):
        return SoccerAction(shoot=Vector2D(b-self))
    
    def trouver_adv(self):
        if self.
            
        
 
