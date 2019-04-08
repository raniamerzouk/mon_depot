#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:29:52 2019

@author: 3671451
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .strat import *

def get_team(nb_players):
    team = SoccerTeam (name = "hop")
    if nb_players == 1:
        team.add("joueur 1", Attaque())
    if nb_players == 2:
        team.add("joueur 1", Attaque())
        team.add("joueur 2", Attaque())

    return team
