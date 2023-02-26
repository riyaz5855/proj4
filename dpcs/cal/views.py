import math
import random

from django.shortcuts import render
from pgeocode import GeoDistance

dict = GeoDistance("IN")

sr = [i for i in range(1, 9)]
ll = ['https://www.fedex.com/', 'https://www.dtdc.in/', 'https://www.delhivery.com/', 'https://www.bluedart.com/',
      'https://www.aramex.com/us/en', 'https://www.shadowfax.in/', 'https://ekartlogistics.com/']

comp_name = ['FedEx', 'EcomExpress', 'DTDC', 'DELHIVERY', 'BLUE DART', 'aramex', 'Shadowfax', 'Ekart Logistics']

complk = ['https://www.fedex.com/', 'https://ecomexpress.in/', 'https://www.dtdc.in/',
          'https://www.delhivery.com/',  'https://www.bluedart.com/',
           'https://www.aramex.com/us/en', 'https://www.shadowfax.in/', 'https://ekartlogistics.com/']

comp_num = {'tel:1800 209 6161', 'tel:+91-8826398220', 'tel:+91-7305770577',
            'tel:+91-8069856101',  'tel:1860 233 1234',
            'tel:022-6480 3300',  'tel:+91-8068172518',
              'tel:1800 208 9898'}

comp_logo = ['/static/cal/images/fedex.jpg',
             '/static/cal/images/express.jpg',
             '/static/cal/images/dtdc.jpg',
             '/static/cal/images/dh.jpg',
             '/static/cal/images/dart.jpg',
             '/static/cal/images/max.jpg',
             '/static/cal/images/fx.jpg',
             '/static/cal/images/ecart.jpg',]

comp_pc = [19000, 25000, 11400, 17500, 17677, 8456, 7000, 19000]

comp_rt = [4.4, 3.0, 2.7, 3.9, 2.0, 4.3, 4.7, 2.2]

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

        # Zip the original lists together into a list of tuples, then shuffle it
        x = list(zip(comp_name, complk, comp_num, comp_logo, comp_pc, comp_rt,))
        random.shuffle(x)

        # Unzip the shuffled list into separate lists
        new_cn, new_ck, new_cm, new_cl, new_pc, new_rt = zip(*x)

        # Zip all the lists back together, including the y list
        new_x = list(zip(sr, new_cn, new_ck, new_cm, val, new_cl, new_pc, new_rt,))

        #fv = zip(sr, comp_name, complk.values(), comp_logo, val, comp_num.values())

        # for a, b, c, d in zip(sr, comp.keys(), comp.values(), val):
        #    fv.append([a, b, c, d])
        return render(request, 'index.html', {'fv': new_x, })

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
