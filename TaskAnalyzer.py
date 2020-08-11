class Task():
    def __init__(self,startTime,endTime,workers):
        self.startTime = startTime
        self.endTime = endTime
        self.workers = workers
        self.parallelTasks = set()
        self.seen = False
    
    @staticmethod
    def setParallelTasks(taskArray):
        """
        takes array of tasks and add parallel tasks into each task.
        can be used as preprocess function
        """
        for idx, task1 in enumerate(taskArray):
            for idx2 in range(idx+1,len(taskArray)):
                task2 = taskArray[idx2]
                if task1.startTime >= task2.startTime and task1.startTime <= task2.endTime:
                    task1.parallelTasks.add(task2)
                    task2.parallelTasks.add(task1)
                elif task1.startTime <= task2.startTime and task1.endTime >= task2.startTime:
                    task1.parallelTasks.add(task2)
                    task2.parallelTasks.add(task1)
    
    @staticmethod
    def findMaxParallelWorkers(taskArray):
        """
        takes array of tasks and return max parallel workers and start time and end time of period.
        """
        Task.setParallelTasks(taskArray)
        maxWorkers = 0
        currentWorkers = 0
        startTime = 0
        endTime = 0
        currentEndTime = 0
        currentStartTime = 0
        for task in taskArray:
            if not task.seen:
                currentWorkers = task.workers
                currentStartTime = task.startTime
                currentEndTime = task.endTime
                for parallelTask in task.parallelTasks:
                    if not parallelTask.seen:
                        currentWorkers += parallelTask.workers                
                        if parallelTask.startTime > currentStartTime:
                            currentStartTime = parallelTask.startTime
                        if parallelTask.endTime < currentEndTime:
                            currentEndTime = parallelTask.endTime
                        parallelTask.seen = True
                if currentWorkers > maxWorkers:
                    maxWorkers = currentWorkers
                    startTime = currentStartTime
                    endTime = currentEndTime
                task.seen = True
        return [maxWorkers,startTime,endTime]


task1 = Task(100,200,2)
task2 = Task(150,170,3)
task3 = Task(300,400,1)
task4 = Task(350,600,10)

tasks = [task1,task2,task3,task4]

print(Task.findMaxParallelWorkers([task1,task2,task3,task4]))

            
