import pandas as pd


if __name__ == '__main__':
    data = {'Часть 1': [], 'Часть 2': [], 'Контекст': []}
    with open('/home/willstudent/russian_compounds/compound_lists/text/compounds_top10000_AN_inflect.txt', 'r') as compounds:
        with open('compounds_top10000_AN_context.txt', 'r') as context:
            for line1, line2 in zip(compounds, context):
                part1 = line1.strip().split()[0]
                part2 = line1.strip().split()[1]
                data['Часть 1'].append(part1)
                data['Часть 2'].append(part2)
                data['Контекст'].append(line2.split('|'))
    df = pd.DataFrame(data=data)
    df.to_csv('compounds_AN_top10000.csv')