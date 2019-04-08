# -*- coding: utf-8 -*-
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .mes_tools import *
import math

#Question 1
class Echauffement(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

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
        Strategy.__init__(self, "Random")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        
        if s.has_ball(s.player):
            shoot = s.lance_max - s.player
            return SoccerAction(shoot = shoot.normalize()*5)
        
##Question 3
#class Defense(Strategy):
#    if s.milieu:
#        pos = 
    
    
        
            
            
        
        