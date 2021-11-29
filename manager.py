import datetime as dt

class Manager:
    """
    All tasks method
    """
    def __init__(self, tasks, freeTime):
        self._tasks = tasks
        self._freeTime = freeTime

    def getUrgentTask(self):
        """
        Receive the list of tasks and return the more urgent task
        """
        df = self._tasks.toDataFrame()
        df = df[df["status"] == 0]
        df = df.sort_values(by="deliveryDate", ascending=False)
        df = df[df["deliveryDate"] == df.iloc[0]["deliveryDate"]]
        df = df.sort_values(by="priority", ascending=False)
        try:
            return df.iloc[0]["name"]
        except:
            raise Exception("No tasks to complete!")