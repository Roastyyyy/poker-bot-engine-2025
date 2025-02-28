from poker_game_runner.state import Observation
from poker_game_runner.utils import Range, HandType
import time
import random

BOT_NAME = "Dean Moore" # Change this to your bot's name

class Bot:
  @classmethod
  def get_name_class(cls, path):
    return BOT_NAME

  def get_name(self):
      return BOT_NAME

  def act(self, obs: Observation):
    # Your code here
    action = random.randit(1,10)
    if action == 1:
      return 0
    if action <= 8 and >= 2:
      return random.randit(1,1000)
    if action == 9:
      return obs.get_max_raise()
    if action == 10:
      return 1
    #return obs.get_max_raise() # All-in
