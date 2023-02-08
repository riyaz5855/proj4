from django.shortcuts import render
from pgeocode import GeoDistance
import math
import random

dict = GeoDistance("IN")


sr=[i for i in range(1,9)]
comp=['FedEx','EcomExpress','DTDC','DELHIVERY','BLUE DART','aramex','Shadowfax','Ecart Logistics']
# Create your views here.
def show(request):
    random.shuffle(comp)
    if request.method == 'POST':
        sp = int(request.POST.get('spincode'))
        dp = int(request.POST.get('dpincode'))
        w = int(request.POST.get('weight'))
        ans=hid(sp,dp,w)
        
        val=[]
        l=[(i/100) for i in range(100, 160)]
        l2=[round((ans*random.choice(l))) for i in range(8)]
        l2=sorted(l2)
        l3=[l[i] for i in range(10,25)]

        for i in l2:
            t=random.choice(l3)
            q, r = i - 2, round(i * t)
            val.append(str(q) + '-' + str(r))


        fv=[]
        for a,b,c in zip(sr,comp,val):
            fv.append([a,b,c])
        return render(request, 'index.html',{'fv':fv})

    return render(request, 'index4.html')


def hid(sp,dp,w):
    cd = dict.query_postal_code(sp,dp)
    sc=math.ceil(50+(cd*.1017*math.ceil(w)))
    return sc
