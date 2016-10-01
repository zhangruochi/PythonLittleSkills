from time import time
from time import localtime
from time import strftime
now = time()  # 时间戳
print(localtime(now))  #time.struct_time(tm_year=2016, tm_mon=10, tm_mday=1, tm_hour=20, tm_min=53, tm_sec=48, tm_wday=5, tm_yday=275, tm_isdst=0)
time_format = "%Y-%m-%d %H:%M:%S"
time_now_str = strftime(time_format,localtime(now)) #2016-10-01 20:56:12
print(time_now_str)

#反向处理
from time import mktime
from time import strptime
time_tuple = strptime(time_now_str,time_format)
now = mktime(time_tuple)
print(now)
