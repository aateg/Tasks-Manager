from datetime import datetime as dt
import pandas as pd

class AllTasks:

    def __init__(self, csv_reader):
        self._tasks = []
        for data in csv_reader:
            self._tasks.append(data)

    def toDataFrame(self):
        df = pd.DataFrame(self._tasks)
        df["priority"] = df["priority"].astype(int)
        df["status"] = df["status"].astype(int)
        df["deliveryDate"] = pd.to_datetime(df["deliveryDate"], format="%d/%m/%y")
        return df
