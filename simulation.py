from party import Party
from voter import Voter

#create a simulation class, which creates parties & voters and runs the simulation
#voters,parties,numbers of simulations
class Simulation:

  def __init__(self):
    self.voters = []
    self.parties = []

  def generate_parties(self, n):
    for i in range(n):
      self.parties.append(Party(self, "Party " + format(i, 'd') , "colour" + format(i, 'd')))
    
  def generate_voters(self, n):
    for i in range(n):
      self.voters.append(Voter(self))

  def get_parties(self):
    return self.parties

  def get_voters(self):
    return self.voters

  def run(self, number_of_steps):
    for i in range(number_of_steps):
      for voter in self.voters:
        voter.vote()
      for party in self.parties:
        party.update_location()
