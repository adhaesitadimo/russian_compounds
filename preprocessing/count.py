import numpy as np
import re
from nltk.corpus import stopwords

nums = r'[0-9]+'
latins = r'[A-Za-z]+'
stop = set(stopwords.words('russian') + ['года', 'века', 'метров', 'м', 'э', 'лет', 'руб', 'млрд', 'млн', 'км', 'кг',
                                         'мм', 'сек', 'тысячи', 'ночи', 'см', 'км/ч', 'г', 'тыс', 'эры', 'минут'])

with open('noun_compounds_NN.txt', 'r') as compounds_train:
    compounds = []
    for line in compounds_train:
        if not re.match(nums, line) and not re.match(latins, line) and line.split()[0] not in stop and \
                line.split()[1] not in stop and '-' not in line and '2' not in line and '.' not in line:
            compounds.append(line.strip())
    print(len(compounds))
    print(len(np.unique(compounds, return_counts=True)[0]))
    inds = np.unique(compounds, return_counts=True)[1].argsort()
    compounds_sort = np.unique(compounds, return_counts=True)[0][inds[::-1]]
    print(compounds_sort[:1000])
    with open('compounds_top10000_NN.txt', 'w') as top1000:
        for i in range(10001):
            top1000.write(compounds_sort[i] + '\r\n')
