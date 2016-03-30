import sched, time
from threading import Timer
from datetime import datetime,timedelta

s=sched.scheduler(time.time, time.sleep)

def print_time() :
    print("From print_time", time.time())

def print_some_times():
    print time.time()
    nT = getTargetTime(150)
    s.enterabs(nT,1,print_some_times,())

def Timer_times():
    print time.time()
    nT = getTargetTime(150)
    Timer(nT, Timer_times, ()).start()


def getTargetTime(work_pr):
    try:
        n = int(time.time())
        mGap = int(n % work_pr)
        tgTime = n + (work_pr - mGap)
        return tgTime
    except:
        print("Error")



Timer_times()
s.run()
