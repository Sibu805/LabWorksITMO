#Percentage diagram
BLUE = '\u001b[44m'
RESET = '\u001b[0m'

def drawer(percentage):
    print(BLUE + " " * int(percentage) + RESET, f"{percentage:.2f}%")

def percentage_diagram(sequence):

    conditions = [(-10, -5), (-5, 0), (0, 5), (5, 10)]
    condition_counts = {interval: 0 for interval in conditions}

    try:
        with open(sequence, 'r') as file:
            data = list(map(float, file.read().split()))
    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что 'sequence.txt' находится в каталоге.")
        return
    if not data:
        print("В файле нет данных.")
        return
    
    for value in data:
        for interval in conditions:
            if interval[0] <= value < interval[1]:
                condition_counts[interval] += 1
                break

    print("Процентная диаграмма по интервалам:")
    Numbers = len(data)
    for interval, count in condition_counts.items():
        percentage = (count / Numbers) * 100
        print(f"{interval[0]} to {interval[1]}: ", end='')
        drawer(percentage)

if __name__ == "__main__":
    percentage_diagram("sequence.txt")
