#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:26:08 2019

@author: 3671451
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu
from ranux import *


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Attaque())  
team2.add("Player 3", Defense())   
team2.add("Player 4", Attaque2())  
team1.add("Player 2", Defense())   

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)