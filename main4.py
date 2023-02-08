from pgeocode import GeoDistance
import math

dict = GeoDistance("IN")

cd = dict.query_postal_code("400037","400028")

w=2
sc=math.ceil(50+(cd*.1017*math.ceil(w)))
print(cd)
print(sc)
