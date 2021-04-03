import enquiries
import random
import requests
import Player
import graficos
from Game import Game

class PreguntasMatematicas(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.message_requirement = self.game["message_requirement"]
    self.requirement = self.game["requirement"]
    self.award = self.game["award"]
    self.name = self.game["name"]
    self.rules = self.game["rules"]

    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
    print(self.question["question"])
    self.answers = [self.question["answers"][x] for x in range (5)]
    self.clues = [self.question[f"clue_{x}"] for x in range (1,4)]