from simulation import Simulation
from tracker import Tracker

def main():
  sim = Simulation()
  sim.generate_voters(10000)
  sim.generate_parties(5)
  tracker = Tracker(sim)
  sim.run(100)

if __name__ == "__main__":
  main()
    