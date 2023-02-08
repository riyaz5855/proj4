from pgeocode import GeoDistance
import random

dict = GeoDistance("IN")

cd = dict.query_postal_code("400037", "400072")
print(cd)
val = list() # all values for company
wt = 2
if cd < 100:
    a = round((50 + (0.1017 * cd))*wt)
else:
    a = round((50 + (1.1017 * cd))*wt)

print('------------------------')
print(a)
l=[(i/100) for i in range(100, 160)]

l2=[round((a*random.choice(l))) for i in range(8)]
l2=sorted(l2)

print(l2)

l3=[l[i] for i in range(10,25)]
for i in l2:
    t=random.choice(l3)
    q, r = i - 2, round(i * t)
    val.append(str(q) + '-' + str(r))
   
print(val)