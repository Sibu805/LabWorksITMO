#флаг Финляндии
BLUE = '\u001b[44m'
WHITE ='\u001b[47m'
RESET = '\u001b[0m'

def drawer(color, length=1):
    print(color + " " *length + RESET,  end='')

#s_vertical - ширина вертикальной полосы
#h_horizontal - ширина горизонтальной полосы, высота и ширина флага
def draw_flag(height, width, s_vertical, h_horizontal):
    s_start = width//3
    s_end = s_start + s_vertical
    h_start = height//2 - h_horizontal//2
    h_end = h_start + h_horizontal

    for h in range(height):
        for w in range(width):
             if h_start <= h < h_end and s_start <= w < s_end:
                 drawer(BLUE)
             elif h_start <= h < h_end:
                 drawer(BLUE)
             elif s_start <= w < s_end:
                 drawer(BLUE)
             else:
                  drawer(WHITE)


        print()

       
           
def main():
    height = 11
    width = 51
    s_vertical = 5
    h_horizontal = 2

    draw_flag(height, width, s_vertical, h_horizontal)

if __name__ == "__main__":
    main()

# y = x/2 function graph
def draw_graph():

    for y in range(10,-11,-1):
        for x in range(-10,11,1):
            if x == 0 and y == 0:
                print('+',end=' ')
            elif x == 0:
                print('|',end=' ')
            elif y == 0:
                print('-',end=' ')
            elif y == x/2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


draw_graph()
   
    


    





