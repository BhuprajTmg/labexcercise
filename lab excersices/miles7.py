#7.you live 4 miles from university. The bus drves at25mph but spends 2 minutes at each of the 10 stops on the way.
# How long will it take the bus journey take?Alternatively you could run to the university.YOu jog the first at 7mps;
# then run the next two at 15mph;before jogging the last at 7mph again.
# will this be the quicker or slower than the bus?
#1.60934

distance=4
speed1=25
#bus stops at 10 places and spent 2 minutes.
stop_t=10*2
time=distance/speed1
tem=time*60
total_time=tem+stop_t
print("the total time too reach university by bus:",total_time)
#he runs with the speed of 7mph
speed2=7
time1=1/speed2
time_1=60*time1
speed3=15
time2=2/speed3
time_2=60*time2
speed4=7
time3=1/speed4
time_3=60*time3

total_time2=time_1+time_2+time_3

print(f"the total time to reach by walk is:{total_time2} ")

if total_time2<total_time:
   print(f"walking is faster to reach university")
elif  total_time<total_time2:
   print("traveling by bus is fasterto reach university.")



