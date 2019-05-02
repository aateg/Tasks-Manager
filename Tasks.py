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
            task["Priority"] = int(row["Priority"])
            task["DeliveryDate"] = dt.datetime.strptime(row["DeliveryDate"],"%d/%m/%y")
            task["HoursRequired"] = int(row["HoursRequired"])
            task["Status"] = row["Status"]
            tasks.append(task) # append task in list with all tasks
    return tasks

# def sortList(param = ["Priority","DeliveryDate"], list):
#     """
#     Classify the list based on the parameters.
#     Parameters priority order is left to right.
#     """
#     # for task in list:
#     #
#     # which method??
#     pass

def getUrgentTask(list):
    """
    Receive the list of tasks and return the more urgent task
    """
    urgent = list[0]
    for task in list[1:]:
        if(task["Priority"] > urgent["Priority"]):
            urgent = task
        elif(task["Priority"] == urgent["Priority"]):
            if(task["DeliveryDate"] <= urgent["DeliveryDate"]):
                urgent = task
    return urgent

def alocateTasks(list, freeTime, maxActiv, minActiv = 1):
    """
    return list with activities alocated per free time on week
    """
    tasksAlocated = []
    while(len(list) != 0):
        task = {}
        urgent = getUrgentTask(list)
        list.pop(list.index(urgent))
        delta = urgent["DeliveryDate"].date()-dt.datetime.today().date()
        hoursPerDay = round(urgent["HoursRequired"]/delta.days)
        # now it is only alocate this hours on freeTime
        if(hoursPerDay < maxActiv):
            # put minActiv
            task["Task"] = urgent["Task"]
            task["TimeOnActiv"] = minActiv
            task["DayToStart"] = dt.datetime.today().date()
        else:
            task["Task"] = urgent["Task"]
            task["TimeOnActiv"] = hoursPerDay
            task["DayToStart"] = dt.datetime.today().date()
        tasksAlocated.append(task)

def main():
    tasks = createListDict()
    freeTime = [4,4,4,4,4,4,4] # free time on week from monday to sunday
    maxActiv = 2
    alocateTasks(tasks, freeTime, 4)
    # print(tasks[0])
main()
