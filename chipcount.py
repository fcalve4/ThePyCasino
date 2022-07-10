import os
import csv

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





