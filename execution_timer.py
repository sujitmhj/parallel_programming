import datetime

class Timer():
    """docstring for Timer"""
    def __init__(self):
        self.old_time = 0
        pass

    def set_old_time(self):
        self.old_time = datetime.datetime.now()

    def start_sequential(self):
        print "Sequential execution started"
        self.set_old_time()

    def end_sequential(self):
        diff = datetime.datetime.now() - self.old_time
        print "Sequential execution time: ", diff.seconds

    def start_parallel(self):
        print "Parallel execution started"
        self.set_old_time()

    def end_parallel(self):
        diff = datetime.datetime.now() - self.old_time
        print "Parallel execution time: ", diff.seconds
