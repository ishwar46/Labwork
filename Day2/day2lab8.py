distance=4
speed1=25
#bus stops at 10 places and spent 2 minutes
stop_T=10*2
time=1/speed1
minute=time*60
total_time=minute+stop_T
print(f"the total time to reach university by bus is {total_time}")
#the runs with the speed of 7 mph
speed2=7
time1=1/speed2
time_1=time1*60
speed3=15
time2=2/speed3
time_2=time2*60
speed4=7
time3=1/speed4
time_3=time3*60
total_time2=time_1+time_2+time_3
print(f"the total time for walking is {total_time2}")

if total_time2>total_time:
    print(f"walking is faster to reach university")
else:
    print(f" taking bus is faster to reach university")
    