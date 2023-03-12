import automata_celular as ac
from view import MundoPlot
from random import randint

def main():
  m = 40
  n = 40
  estado_inicial = [randint(0,1) for b in range(1,m*n+1)]

  cell_size = 10
  color0 = (255, 255, 255, 1)
  color1 = (0, 0, 0, 1)
  mundo = ac.Mundo(m,n,estado_inicial)
  plot = MundoPlot([mundo],cell_size,color0,color1)
  
  plot.plot_estado(f"output/P1B/P1B_mundo0")
  for i in range(1,11):
    mundo.actualiza()
    plot.plot_estado(f"output/P1B/P1B_mundo{i}")

if __name__ == "__main__":
    main()
