import time
import os

SET_COLOR = "\x1b[48;5;196m"  
END = "\x1b[0m"               
CLEAR = "\033[H"  

def plotter():
    print(f"{SET_COLOR}{' '}{END}", end='')

def twin_circles(position=0, radius=6):
    for y in range(2 * radius + 1):
        for x in range(4 * radius + 2):
            if (x - radius)**2 + (y - (radius + position))**2 <= radius**2:
                plotter()
            elif (x - (3 * radius + 1))**2 + (y - (radius + position))**2 <= radius**2:
                plotter()
            else:
                print(" ", end='')

        print()  

def main():
    position = 0
    frames = 0

    while True:
        twin_circles(position)

        frames += 1
        if frames >= 3:
            os.system('cls' if os.name == 'nt' else 'clear') 
            frames = 0

        position += 2 
        if position > 10:
            position = 0

        time.sleep(0.5)  

if __name__ == "__main__":
    main()