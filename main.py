from . import tasks

def main():
    with open('./Tasks.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file) # read csv
        tasks = Tasks(csv_reader)
    freeTime = [4,4,4,4,4,4,4] # free time on week from monday to sunday
    maxActiv = 2
main()
