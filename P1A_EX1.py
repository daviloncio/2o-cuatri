import automata_celular as ac
from PIL import Image

### Función auxiliar para pintar matriz en png -----------------
def plot_estado(num_rows, num_cols, estado, filename):
    cell_size = 40
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

def main():
  m = 6
  n = 6
  estado_inicial = [1,0,1,1,0,1,
                    0,0,1,1,0,0,
                    1,0,0,0,0,1,
                    1,0,1,1,0,1,
                    0,0,0,0,0,0,
                    0,1,1,1,1,0]
  mundo = ac.Mundo(m,n,estado_inicial)
  plot_estado(m, n, mundo.estado, "output/P1A/1A_mundo0")
  mundo.actualiza()
  plot_estado(m, n, mundo.estado, "output/P1A/1A_mundo1")

if __name__ == "__main__":
    main()
