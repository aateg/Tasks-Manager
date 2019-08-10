import csv
import datetime as dt


class Tasks:
    """
    All tasks method
    """
    class Task:
        """
        Internal class
        """
        def __init__(self, task):
            self.name = task["task"]
            self.priority = int(task["priority"])
            self.delivery_date = dt.datetime.strptime(task["delivery_date"],"%d/%m/%y")
            self.hours_required = int(task["hours_required"])
            self.status = task["status"]

    def __init__(self):
        self.tasks = []

    def create_task(self, csv_reader):
        for task in csv_reader:
            add_task(Task(task))

    def add_task(self, Task):
        self.tasks.append(Task)

    def get_urgent_task(list):
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
