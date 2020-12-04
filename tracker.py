
class Tracker:

  def __init__(self, simulation):
    self.simulation = simulation
    self.votes = {}

  def add_party(self, name):
    self.votes[name] = []
  
  def save_current_state(self):
    for party in self.simulation.get_parties():
      self.votes[party.get_name()].append(party.count_voters())

  # create Excel file with all data
  def export_to_csv(self, filename):
    pass

# excel file should have columns like:
# 1) iteration number
# 2) votes
# 3) x
# 4) y
# with one CSV file for each party