# The Orchestra component is responsible for managing and coordinating tasks.

from queue import Queue
from src.executor.core import Executor

class Orchestra:
    """
    The Orchestra manages the task queue and the executor threads.
    """
    def __init__(self, num_executors: int = 1):
        self.task_queue = Queue()
        self.executors = []
        for _ in range(num_executors):
            executor = Executor(self.task_queue)
            self.executors.append(executor)

    def start(self):
        """
        Starts the orchestra and the executor threads.
        """
        print("Starting the orchestra...")
        for executor in self.executors:
            executor.start()

    def stop(self):
        """
        Stops the orchestra and the executor threads.
        """
        print("Stopping the orchestra...")
        # Add a None task for each executor to signal them to stop.
        for _ in self.executors:
            self.task_queue.put(None)
        # Wait for all tasks to be processed.
        self.task_queue.join()
        # Wait for all executor threads to finish.
        for executor in self.executors:
            executor.join()
        print("Orchestra stopped.")

    def add_task(self, task):
        """
        Adds a task to the task queue.
        """
        self.task_queue.put(task)
