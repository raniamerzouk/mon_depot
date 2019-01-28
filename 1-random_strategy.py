# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import *

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        pb = state.ball.position
        pj = state.player_state(1,0).position
        v = pb-pj
        if (id_team == 2):
            but = Vector2D(0, GAME_HEIGHT/2)
        else:
            but = Vector2D(GAME_WIDTH, GAME_HEIGHT/2)
        if (v.norm < PLAYER_RADIUS + BALL_RADIUS):
            return SoccerAction(shoot=(but-pb)/50)
        else:
            return SoccerAction(acceleration=v)


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Random", RandomStrategy())  # Random strategy
team2.add("Static", Strategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
