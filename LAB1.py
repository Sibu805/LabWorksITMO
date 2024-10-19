#флаг Финляндии
BLUE = '\u001b[44m'
WHITE ='\u001b[47m'
RESET = '\u001b[0m'

def drawer(color, length=1):
    print(f"'{color}' * length + {RESET},  end=''")

#s_vertical - ширина вертикальной полосы
#h_horizontal - ширина горизонтальной полосы, высота и ширина флага
def draw_flag(heigth, width, s_vertical, h_horizontal):
    s_start = width//3
    s_end = s_start + s_vertical
    h_start = height//2 - h_horizontal//2
    h_end = h_start + h_horizontal

    for height in (height):
        for width in (width):
             if h_start <= height < h_end:
                 drawer(BLUE, s_vertical)
             elif s_start <= width < s_end:
                 drawer(BLUE, h_horizontal)
             else:
                  drawer(WHITE)
           

    draw_flag(height, width, s_vertical, h_horizontal)
    
       
def main():
    height = 20
    width = 30
    s_vertical = 10
    h_horizontal = 10

    print(height, width, s_vertical, h_horizontal)

if __name__ == "__main__":
    main()
    


    





