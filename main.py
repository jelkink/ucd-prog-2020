from simulation import Simulation

def main():
  sim = Simulation()
  sim.generate_voters(100)
  sim.generate_parties(5)
  sim.run(10)

if __name__ == "__main__":
  main()
    