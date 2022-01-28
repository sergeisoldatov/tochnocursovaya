# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



class Participant:
  def __init__(self, name):
    self.name = name
    self.points = 0
    self.choice = ""

  def toNumericalChoice(self):
      switcher = {
        "rock": 0,
        "paper": 1,
        "scissor": 2
      }
      return switcher[self.choice]

  def incrementPoint(self):
    self.points += 1
  def choose(self):
    self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
    print("{name} selects {choice}".format(name=self.name, choice = self.choice))

class GameRound:
  def __init__(self, p1, p2):
      self.rules = [
        [0, -1, 1],
        [1, 0, -1],
        [-1, 1, 0]
      ]

      p1.choose()
      p2.choose()
      result = self.compareChoices(p1, p2)
      if result > 0:
        p1.incrementPoint()
      elif result < 0:
        p2.incrementPoint()
      print("Round resulted in a {result}".format(result=self.getResultAsString(result)))
  def compareChoices(self):
    print("implement")
  def awardPoints(self):
    print("implement")
  def compareChoices(self, p1, p2):
      return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

  def getResultAsString(self, result):
    res = {
      0: "draw",
      1: "win",
      -1: "loss"
    }
    return res[result]

class Game:
  def __init__(self):
    self.endGame = False
    self.participant = Participant("Spock")
    self.secondParticipant = Participant("Kirk")

  def start(self):
    while not self.endGame:
      GameRound(self.participant, self.secondParticipant)
      self.checkEndCondition()

  def checkEndCondition(self):
    print("implement")
  def determineWinner(self):
    print("implement")

  def determineWinner(self):
    resultString = "It's a Draw"
    if self.participant.points > self.secondParticipant.points:
      resultString = "Winner is {name}".format(name=self.participant.name)
    elif self.participant.points < self.secondParticipant.points:
      resultString = "Winner is {name}".format(name=self.secondParticipant.name)
    print(resultString)

  def checkEndCondition(self):
    answer = input("Continue game y/n")
    if answer == 'y':
      GameRound(self.participant, self.secondParticipant)
      self.checkEndCondition()
    else:
      print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name=self.participant.name,
                                                                                      p1points=self.participant.points,
                                                                                      p2name=self.secondParticipant.name,
                                                                                      p2points=self.secondParticipant.points))
      self.determineWinner()
      self.endGame = True

game = Game()
game.start()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
