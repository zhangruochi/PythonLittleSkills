# 使用 time 模块 不能很好的解析电脑所支持的各种时区


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


#使用 datetime 模块
from datetime import datetime
import pytz

#将纽约时间转化为 UTC 时间
arrival_nyc = '2014-05-01 23:33:24'
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
eastern = pytz.timezone('US/Eastern')
nyc_dt = eastern.localize(nyc_dt_naive)
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
print(utc_dt)


#将 UTC 时间转化为旧金山时间
pacific = pytz.timezone('US/Pacific')
sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
print(sf_dt)


#将 UTC 时间转化为尼泊尔时间
nepal = pytz.timezone('Asia/Katmandu')
nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
print(nepal_dt)

