from fnmatch import fnmatch,fnmatchcase
#fnmatch  适合通配符
print(fnmatch("fnmatch.txt","*.txt"))

all_file = ["test.py","zhan.r","fuck.py","set.txt"]

python_file = [file for file in all_file if fnmatch(file,"*.py")]
print(python_file)


import re

pattern = re.compile("(\d+)/(\d+)/(\d+)")
result = re.match(pattern,"20/7/1994")
print(result.group())
print(result.groups())
print(result.group(1))