from location import Location
import random

class Party:

  def __init__(self, simulation, name, colour, strategy=""):
    self.location = Location()
    self.simulation = simulation

    if strategy == "":
      self.random_strategy()
    else:
      self.strategy = strategy
    
    self.name = name
    self.colour = colour # random_colour() ???
    self.voters = []

#  def random_strategy(self):
#    self.strategy = random.choose(self.simulation.get_allowed_strategies())

  def random_strategy(self):
    a = random.randint(1,5)
    if a == 1:
      self.strategy = "sticker"
    elif a == 2:
      self.strategy = "predator"
    elif a == 3:
      self.strategy = "hunter"
    elif a == 4:
      self.strategy = "aggregator"
    elif a == 5:
      self.strategy = "random"

  def add_voter(self, voter):
    return self.voters.append(voter)

  def reset_voters(self):
    self.voters = []

  def count_voters(self):
    return len(self.voters)

  def update_location(self):
    if self.strategy == "sticker":
      self.update_location_sticker()
    elif self.strategy == "predator":
      self.update_location_predator()
    elif self.strategy == "hunter":
      self.update_location_hunter()
    elif self.strategy == "aggregator":
      self.update_location_aggregator()
    elif self.strategy == "random":
      self.update_location_random()
    else:
      print("Strategy " + self.strategy + " does not exist!")

  def update_location_predator(self):
    parties = self.simulation.get_parties()
    biggest_party = self
    for p in parties:
      if biggest_party.count_voters() < p.count_voters():
        biggest_party = p
    self.location.move_towards(biggest_party.location)

  def update_location_aggregator(self):
    if len(self.voters) > 0:
      sum_x = 0
      sum_y = 0
      for voter in self.voters:
        sum_x += voter.location.x
        sum_y += voter.location.y
      self.location.set_x(sum_x / len(self.voters))
      self.location.set_y(sum_y / len(self.voters))

  def update_location_hunter(self):
    #get previous move
    #if voters before prev move >= voters after prev move
    #  then turn 180 degrees and move again anywhere 90 degrees either side 
    #if voters before prev move < voters after prev move
    #  move same way as previous move again
    
    #read previous move
    current_count = self.count_voters()
    if current_count == self.previous_count:
      pass
    if current_count > self.previous_count:
      self.location.x += 0.01
      self.location.y += 0.01
    if current_count < self.previous_count:
      pass

  def save_state(self):
    self.previous_count = self.count_voters()

  def update_location_random(self):
    self.location.random_move()

  def update_location_sticker(self):
    pass

  def get_location(self):
    return self.location

  def get_strategy(self):
    return self.strategy

  def get_name(self):
    return self.name

  def get_colour(self):
    return self.colour

  def get_voters(self):
    return self.voters