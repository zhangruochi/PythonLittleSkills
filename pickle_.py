import pickle
import copyreg

class GameState:
    def __init__(self,level = 0,lives = 4,points = 0):
        self.level = level
        self.lives = lives
        self.points = points

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)     

def unpickle_game_state(kwargs):
    return GameState(**kwargs)


copyreg.pickle(GameState,pickle_game_state)


state = GameState()
state.points += 100
serialized  = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

"""
state.__setattr__("magic",5)
print(state.__dict__)
"""

class GameState:
    def __init__(self,level = 0,lives = 4,points = 0,magic = 5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic


state_after_2 = pickle.loads(serialized)
print(state_after_2.__dict__)




           