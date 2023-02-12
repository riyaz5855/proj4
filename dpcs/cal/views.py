import math
import random

from django.shortcuts import render
from pgeocode import GeoDistance

dict = GeoDistance("IN")

sr = [i for i in range(1, 9)]
ll = ['https://www.fedex.com/', 'https://www.dtdc.in/', 'https://www.delhivery.com/', 'https://www.bluedart.com/',
      'https://www.aramex.com/us/en', 'https://www.shadowfax.in/', 'https://ekartlogistics.com/']

comp_name = ['FedEx', 'EcomExpress', 'DTDC', 'DELHIVERY', 'BLUE DART', 'aramex', 'Shadowfax', 'Ekart Logistics']

complk = {'FedEx': 'https://www.fedex.com/', 'EcomExpress': 'https://ecomexpress.in/', 'DTDC': 'https://www.dtdc.in/',
          'DELHIVERY': 'https://www.delhivery.com/', 'BLUE DART': 'https://www.bluedart.com/',
          'aramex': 'https://www.aramex.com/us/en', 'Shadowfax': 'https://www.shadowfax.in/',
          'Ekart Logistics': 'https://ekartlogistics.com/'}

comp_num = {'FedEx': 'tel:1800 209 6161', 'EcomExpress': 'tel:+91-8826398220', 'DTDC': 'tel:+91-7305770577',
            'DELHIVERY': 'tel:+91-8069856101', 'BLUE DART': 'tel:1860 233 1234',
            'aramex': 'tel:022-6480 3300', 'Shadowfax': 'tel:+91-8068172518',
            'Ekart Logistics': 'tel:1800 208 9898'}

comp_logo = {'/static/cal/images/fedex.jpg': 'https://www.fedex.com/',
             '/static/cal/images/express.jpg': 'https://ecomexpress.in/',
             '/static/cal/images/dtdc.jpg': 'https://www.dtdc.in/',
             '/static/cal/images/dh.jpg': 'https://www.delhivery.com/',
             '/static/cal/images/dart.jpg': 'https://www.bluedart.com/',
             '/static/cal/images/max.jpg': 'https://www.aramex.com/us/en',
             '/static/cal/images/fx.jpg': 'https://www.shadowfax.in/',
             '/static/cal/images/ecart.jpg': 'https://ekartlogistics.com/'}


# Create your views here.
def show(request):
    # elm = list(comp.items())
    # elm = list(comp_logo.items())
    random.shuffle(comp_name)

    # newcomp = Convert(elm)
    # print(newcomp)

    if request.method == 'POST':
        sp = int(request.POST.get('spincode'))
        dp = int(request.POST.get('dpincode'))
        w = int(float(request.POST.get('weight')))

        if w > 1:
            return render(request, 'auth.html')

        ans = hid(sp, dp, w)

        val = []
        l = [(i / 100) for i in range(100, 160)]
        l2 = [round((ans * random.choice(l))) for i in range(8)]
        l2 = sorted(l2)
        l3 = [l[i] for i in range(10, 25)]

        for i in l2:
            t = random.choice(l3)
            q, r = i - 2, round(i * t)
            val.append(str(q) + '-' + str(r))

        # keys = list(comp_logo.keys())
        # random.shuffle(keys)

        # shuffled_dict = {key: comp_logo[key] for key in keys}

        fv = zip(sr, comp_name, complk.values(), comp_logo, val, comp_num.values())

        # for a, b, c, d in zip(sr, comp.keys(), comp.values(), val):
        #    fv.append([a, b, c, d])
        return render(request, 'index.html', {'fv': fv, })

    return render(request, 'auth.html')


def hid(sp, dp, w):
    cd = dict.query_postal_code(sp, dp)
    sc = math.ceil(50 + (cd * .1017 * math.ceil(w)))
    return sc


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def home(request):
    return render(request, 'home.html')
