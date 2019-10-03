import random
import numpy

normlist = []
amount = 100000

for x in range(1,amount+1):
    a = random.randrange(1,101)/100
    b = random.randrange(1,101)/100
    c = random.randrange(1,101)/100
    d = random.randrange(1,101)/100
    point_x = numpy.array([a,b])
    point_y = numpy.array([c,d])
    normlist.append(numpy.linalg.norm(point_x-point_y))

print(sum(normlist)/amount)
