
class Tracker:

  def __init__(self, simulation):
    self.simulation = simulation
    simulation.set_tracker(self)

    # create an empty dict with all parties as keys
  
  def save_current_state(self):
    pass

  def export_to_csv(self):
    pass