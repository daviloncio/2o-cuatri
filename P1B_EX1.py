import automata_celular as ac
from PIL import Image
from random import randint

### Función auxiliar para pintar matriz en png -----------------
def plot_estado(num_rows, num_cols, estado, filename):
    cell_size = 2
    image = Image.new(mode='L', size=(cell_size*num_cols, cell_size*num_rows), color='white')
    
    for i in range(num_rows):
        for j in range(num_cols):
            state = estado[i*num_rows+j]
            color = 0 if state == 1 else 255
            x = j * cell_size
            y = i * cell_size
            for dy in range(cell_size):
                for dx in range(cell_size):
                    image.putpixel((x+dx, y+dy), color)
    image.save(filename + ".png")
### -------------------------------------------------------------

## MODIFICAR:
## Añade en mainlo necesario para colocar, en cada turno t, 
## CelulaInversorBinario inicializada a 1 en posición
## (3*t,3*t) del mundo, tal como explica el enunciado.

def main():
  m = 40
  n = 40
  estado_inicial = [randint(0,1) for b in range(1,m*n+1)]
  mundo = ac.Mundo(m,n,estado_inicial)
  for t in range(1,11):
    mundo.actualiza()
    plot_estado(m, n, mundo.estado, [f"output/P1B/P1B_mundo{t}"])

if __name__ == "__main__":
    main()
