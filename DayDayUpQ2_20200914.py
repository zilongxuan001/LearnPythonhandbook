#DayDayUPQ2.py

dayfactor = 0.005
dayup = pow(1+ dayfactor, 365)
daydown = pow(1- dayfactor, 365)
print("向上： {:.2f}, 向下：{:.2f}".format(dayup, daydown))

dayup2 = pow(1+ dayfactor*2, 365)
daydown2 = pow(1- dayfactor*2, 365)
print("向上： {:.2f}, 向下：{:.2f}".format(dayup2, daydown2))