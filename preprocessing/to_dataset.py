import pandas as pd

if __name__ == '__main__':
    data = {'Часть 1': [], 'Часть 2': []}
    with open('compounds_top10000.txt', 'r') as compounds:
        for line in compounds:
            part1 = line.strip().split()[0]
            part2 = line.strip().split()[1]
            data['Часть 1'].append(part1)
            data['Часть 2'].append(part2)
    df = pd.DataFrame(data=data)
    df.to_csv('compounds_AN_top10000.csv')