import time
import datetime

print("Hello World")

timeNow = datetime.datetime.now()

print(timeNow) # returns years, months, days, hours, minutes, seconds, micro seconds

# get date from the time in Years-Months-Days format

today =  timeNow.strftime("%Y-%m-%d")

# time in hours minutes seconds format

Now = timeNow.strftime("%H:%M:%S") 

print("Todays date is {}".format(today))

print("Next section will be executed 10 sec later")

time.sleep(10)
print("Time is ", Now)

# counting the time the current thread took to execute in seconds
print(time.thread_time())
