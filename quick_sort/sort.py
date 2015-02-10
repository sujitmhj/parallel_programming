#!/usr/bin/python

from threading import Thread

import random
import os
import sys
path = os.path.dirname(os.path.abspath(__file__)) + "/../"
sys.path.append(path)

# example = __import__("examples", globals(), locals(), sys.argv[1])

from execution_timer import Timer
def quick_sort_sequential(arr,left,right):
    if left >= right : return
    ind = left
    target = arr[right-1]
    i=left
    while True:
        if i == right-1: break
        if arr[i] <= target:
            tmp = arr[ind]
            arr[ind] = arr[i]
            arr[i] = tmp
            ind += 1
        i+=1
    arr[right-1]=arr[ind]
    arr[ind]=target
    quick_sort_sequential(arr,left,ind)
    quick_sort_sequential(arr,ind+1,right)


def quick_sort_parallel(arr,left,right):
    if left >= right : return
    ind = left
    target = arr[right-1]
    i=left
    while True:
        if i == right-1: break
        if arr[i] <= target:
            tmp = arr[ind]
            arr[ind] = arr[i]
            arr[i] = tmp
            ind += 1
        i+=1
    arr[right-1]=arr[ind]
    arr[ind]=target
    t1 = Thread(target=quick_sort_parallel, args=[arr,left,ind])
    t2 = Thread(target=quick_sort_parallel, args=[arr,ind+1,right])
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    try:
     if sys.argv[1] is not None:
        n = int(sys.argv[1])
    except:
        n = 100
    arr = random.sample(range(1, 10000000), n)
    timer = Timer()
    timer.start_sequential()
    quick_sort_sequential(arr,0,len(arr))
    timer.end_sequential()
    timer.start_parallel()
    quick_sort_parallel(arr,0,len(arr))
    timer.end_parallel()
