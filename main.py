from simulation import Simulation

def main():
  sim = Simulation()
  sim.generate_voters(1000)
  sim.generate_parties(5)
  sim.run(200)

if __name__ == "__main__":
  main()
    