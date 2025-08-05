# The Executor component is responsible for running tasks.

import threading
from queue import Queue

class Executor(threading.Thread):
    """
    The Executor is a worker thread that retrieves tasks from a queue and executes them.
    """
    def __init__(self, task_queue: Queue):
        super().__init__()
        self.task_queue = task_queue
        self.daemon = True

    def run(self):
        """
        The main loop of the executor.
        """
        while True:
            try:
                task = self.task_queue.get()
                if task is None:
                    # A None task is a signal to stop.
                    break
                self.execute_task(task)
            except Exception as e:
                print(f"Error executing task: {e}")

    def execute_task(self, task):
        """
        Executes a single task.
        """
        print(f"Executing task: {task}")
        # In a real implementation, this would be much more complex.
        # For now, we will just call the function.
        try:
            task()
        except Exception as e:
            print(f"Task failed: {e}")
        finally:
            self.task_queue.task_done()
