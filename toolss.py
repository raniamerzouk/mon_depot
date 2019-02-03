#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rayon d'un joueur
PLAYER_RADIUS =1.
#Rayon de la balle 
BALL_RADIUS = 0.65
#Longueur du terrain
GAME_WIDTH = 150 
#Largeur du terrain 
GAME_HEIGHT= 90
GAME_GOAL_HEIGHT = 10 
MAX_GAME_STEPS = 2000
max_PlayerSpeed = 1
maxPlayerAcceleration = 0.2
maxBallAcceleration = 5

class SuperState(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.team = id_team 
        self.id_player = id_player
        
    @property
    def ball(self):
        return self.state.ball.position
    
    @property
    def player(self):
        return self.state.player_state(self.id_team, self.id_player).position
    
    @property 
    def goal(self):
        return Vector2D(GAME_WIDTH * (2- self.id_team), GAME_HEIGHT /2)
    
    @property
    def aller_vers(self,obj):
        return Vector2D(obj-player)
    
    #foncer vers le but 
    @property
    def foncer_vers_but(self):
        return SoccerAction(shoot = (self.goal - self.ball).normalize())
   
    #shoot vers le but 
    @property
    def tirer_au_but(self):
        return SoccerAction(shoot =(self.goal - self.ball).normalize()*maxPlayerShoot) 
    
    @property
    def takeSecond(elem):
        return elem[1]
    
    #trouver l'adversaire le plus proche 
    @property
    def adversaire_prche(self):
        liste = [(id_player, (self.state.player_state(id_team, id_player).position - self.state.player). norm) for (id_team,id_player) in state.players if id_team != self.id_team]
        liste_triee = sorted(liste, key = takeSecond)
        return liste_triee[0,0]

        
