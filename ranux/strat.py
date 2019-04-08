# -*- coding: utf-8 -*-
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .mes_tools import *
import math

#Question 1
class Echauffement(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Echauffement")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)

        if s.has_ball(s.player):
            shoot = s.closest_opponent - s.player
            return SoccerAction(shoot = shoot.normalize()*5)

#Question 2        
class Attaque(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaque")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
       
        t = s.lance_max
        x = s.posd_volley.x
        a = ((s.ball.y-t.y)/(s.ball.x - t.x))
        b = (GAME_HEIGHT/2) - (a * x)
        pos = Vector2D(x, a* x + b)
         
        if s.has_ball(s.player):
            shoot = pos - s.player
            return SoccerAction(shoot = shoot)
        
#Question 3
class Defense(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defense")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        
        pos = s.posd_volley
        
        if s.milieu:
            SoccerAction(acceleration =  s.deplacement(s.balleamelioree))
            if s.has_ball(s.player):
                shoot = s.lance_max - s.player
                return SoccerAction(shoot = shoot)
        else:
            return SoccerAction(s.deplacement(s.posd_volley))
        
#Question 5
class Attaque2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Attaque2")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        
        if s.has_ball:
            if s.coeq_prochefilets:
                shoot = s.coequipierproche - s.player
                return SoccerAction(shoot = shoot.normalize()*2)
            return SoccerAction(shoot = (s.lance_max - s.player)*5)
        else:
            SoccerAction(acceleration = s.deplacement(s.balleamelioree))
            
    
    
        
            
            
        
        