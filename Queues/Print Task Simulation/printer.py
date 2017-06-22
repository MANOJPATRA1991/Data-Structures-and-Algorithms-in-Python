class Printer(object):
    def __init__(self, ppm):
        self.pageRate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        """
        :type new_task: Task
        """
        self.currentTask = new_task
        self.timeRemaining = new_task.get_pages() * 60 / self.pageRate
