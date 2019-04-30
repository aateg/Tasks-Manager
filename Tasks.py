import csv
import datetime as dt

def createListDict():
    tasks = []
    with open('./Tasks.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # line_count = 0
        for row in csv_reader:
            task = {}
            task["Task"] = row["Task"]
            task["Priority"] = row["Priority"]
            task["DeliveryDate"] = dt.datetime.strptime(row["DeliveryDate"],"%d/%m/%y")
            task["HoursRequired"] = int(row["HoursRequired"])
            task["Status"] = row["Status"]
            tasks.append(task)
    return tasks
    g
def sortList(param = ["Priority","DeliveryDate"]):
    pass

def main():
    tasks = createListDict()
    print(tasks[0])
main()
