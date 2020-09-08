import sys
from statistics import mean

grades = [int(n) for n in sys.argv[1:]]
avrg = mean(grades)
res = [n for n in grades if n > avrg]
print(res)
