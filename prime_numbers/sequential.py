#!/usr/bin/python

from threading import Thread
import datetime
import sys
class Prime():
    """docstring for ClassName"""

    def __init__(self, limit):
        self.limitn = limit+1
        self.not_prime = set()
        self.primes = []
        pass

    def sequential_primes(self):
        self.not_prime = set()
        self.primes = []
        for i in range(2, self.limitn):
            if i in self.not_prime:
                continue
            for f in range(i*2, self.limitn, i):
                self.not_prime.add(f)
            self.primes.append(i)
        return self.primes
    def mark_not_prime(self,num):
        for f in range(num*2, self.limitn, num):
            self.not_prime.add(f)

    def parallel_primes(self):
        self.not_prime = set()
        self.primes = []
        threads = []
        for i in range(2, self.limitn):
            if i in self.not_prime:
                continue
            t = Thread(target=self.mark_not_prime, args=[i])
            t.start()
            threads.append(t)

            self.primes.append(i)
        for t in threads:
            t.join()

        return self.primes




if __name__ == '__main__':
    try:
        if sys.argv[1] is not None:
            n = int(sys.argv[1])
    except:
        n = 100
    prime = Prime(n)

    time1 = datetime.datetime.now()
    print "Sequential execution started"
    prime.parallel_primes()
    
    time2 = datetime.datetime.now() 
    diff = time2 - time1
    print "Sequential execution time: ", diff.seconds

    print "Parallel execution started"
    prime.sequential_primes()
    time3 = datetime.datetime.now()
    diff = time3 - time2
    print "Parallel execution time: ", diff.seconds
