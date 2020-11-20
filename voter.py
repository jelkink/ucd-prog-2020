from location import Location

class Voter:

  def __init__(self):
    self.location = Location()

  def update_vote(self):
    self.vote.add_voter(self)

  def get_vote(self):
    return self.vote

  def get_location(self):
    return self.location