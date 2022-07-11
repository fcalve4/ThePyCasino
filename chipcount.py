import os
import csv
from operator import itemgetter

main_path = os.getcwd()
record_path = main_path + '\\record.csv'


def get_score(balance, name):
    try:
        with open(record_path, 'x', newline='') as file:
            try:
                for row in (list(csv.reader(file))):
                    if name.lower().capitalize() in row:
                        balance = row[0]
                        break
                    else:
                        balance = 1000
            except:
                balance = 1000

    except FileExistsError:
        with open(record_path, 'r') as file:
            for row in (list(csv.reader(file))):
                if name.lower().capitalize() in row:
                    balance = row[0]
                    break
                else:
                    balance = 1000

    return int(balance)


def save_score(balance, name):
    scorename = [str(balance), name.lower().capitalize()]
    try: 
        with open(record_path, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(scorename)

    except FileExistsError:
        with open(record_path, 'r') as file:
            reader = csv.reader(file)
            filedata = []
            for row in reader:
                filedata.append(row)
            with open(record_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for i in filedata:
                    if name.lower().capitalize() in i:
                        pass
                    else:
                        writer.writerow(i)
                writer.writerow(scorename)



def leaderboard():

    with open(record_path, 'r') as file:
        reader = csv.reader(file)
        filedata = []
        for row in reader:
            lst = []
            lst.append(int(row[0]))
            lst.append(row[1])
            filedata.append(lst)
            
        top10= sorted(filedata, key=itemgetter(0), reverse=True)

    print(
    """
     _______________________________________________________________________
    |                                                                       |
    |      _                   _           _                         _      |
    |     | |    ___  __ _  __| | ___ _ __| |__   ___   __ _ _ __ __| |     | 
    |     | |   / _ \/ _` |/ _` |/ _ \ '__| '_ \ / _ \ / _` | '__/ _` |     |
    |     | |__|  __/ (_| | (_| |  __/ |  | |_) | (_) | (_| | | | (_| |     |
    |     |_____\___|\__,_|\__,_|\___|_|  |_.__/ \___/ \__,_|_|  \__,_|     |
    |                                                                       |
    |_______________________________________________________________________|
    """
    )
    for i in top10:
        print("{}: {} chips".format(i[1], str(i[0])).center(78))
    x = input("\n                          (Press any key to continue)\n").center(64)