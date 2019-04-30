import csv
import datetime as dt

def createListDict():
    """
    Opens the csv file, make each task a dict and add to list with all the files.
    """
    tasks = []
    with open('./Tasks.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file) # read csv
        for row in csv_reader:
            task = {} # create task as dict
            task["Task"] = row["Task"]
            task["Priority"] = row["Priority"]
            task["DeliveryDate"] = dt.datetime.strptime(row["DeliveryDate"],"%d/%m/%y")
            task["HoursRequired"] = int(row["HoursRequired"])
            task["Status"] = row["Status"]
            tasks.append(task) # append task in list with all tasks
    return tasks

def sortList(param = ["Priority","DeliveryDate"], list):
    """
    Classify the list based on the parameters.
    Parameters priority order is left to right.
    """
    # for task in list:
    #
    # which method??
    pass

def main():
    tasks = createListDict()
    print(tasks[0])
main()
