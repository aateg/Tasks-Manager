from task import AllTasks
from manager import Manager
import csv

def main():
    with open('./Tasks.csv', mode='r') as csv_file:
        csvReader = csv.DictReader(csv_file) # read csv
        tasks = AllTasks(csvReader)
    freeTime = 2

    manager = Manager(tasks, freeTime)
    print(manager.getUrgentTask())


main()