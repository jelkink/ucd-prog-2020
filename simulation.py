from party import Party
from voter import Voter
from tracker import Tracker
from log import Log

#create a simulation class, which creates parties & voters and runs the simulation
#voters,parties,numbers of simulations
class Simulation:

  def __init__(self):
    self.voters = []
    self.parties = []
    self.log = Log("simulation.log")

  def generate_parties(self, n):
    for i in range(n):
      self.parties.append(Party(self, "P" + format(i, 'd') , "colour" + format(i, 'd')))
    
  def generate_voters(self, n):
    for i in range(n):
      self.voters.append(Voter(self))

  def get_parties(self):
    return self.parties

  def get_voters(self):
    return self.voters
  
  def set_tracker(self, tracker):
    self.tracker = tracker

  def run(self, number_of_steps):
    for i in range(number_of_steps):
      
      print("\nStep {}:".format(i))

      for party in self.parties:
        party.reset_voters()

      for voter in self.voters:
        voter.update_vote()

      for party in self.parties:
        print("Party {} with the {} strategy has {} votes.".format(party.name, party.strategy, party.count_voters()))
        party.update_location()

      self.tracker.save_current_state()
