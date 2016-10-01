import pickle
import copyreg

class GameState:
    def __init__(self,level = 0,lives = 4,points = 0):
        self.level = level
        self.lives = lives
        self.points = points


state = GameState()
state.points += 100
serialized  = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

"""
state.__setattr__("magic",5)
print(state.__dict__)
"""

#修改类名 增加和删除属性等都可以用 copyreg 模块解决
class BetterGameState:
    def __init__(self,level = 0,points = 0,magic = 5):
        self.level = level
        self.points = points
        self.magic = magic

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs["version"] = 2
    return unpickle_game_state, (kwargs,)     

def unpickle_game_state(kwargs):
    version = kwargs.pop("version",1)
    if version == 1:
        kwargs.pop("lives")
    return GameState(**kwargs)


copyreg.pickle(BetterGameState,pickle_game_state)        


state_after_2 = pickle.loads(serialized)
print(state_after_2.__dict__)




           