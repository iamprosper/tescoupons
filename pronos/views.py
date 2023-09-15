from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Coupon


# Create your views here.


def index(request):
    coupons = Coupon.objects.all()
    onewin_coupons = Coupon.objects.filter(bookmaker="1w")
    onexbet_coupons = Coupon.objects.filter(bookmaker="1x")
    # counter = 0
    total_onewin = onewin_coupons.count()
    total_onexbet = onexbet_coupons.count()
    # template = loader.get_template("pronos/index.html")
    # return HttpResponse(template.render(None, request))
    return render(
        request,
        'pronos/index.html',
        {
            'onexbet_coupons': onexbet_coupons,
            'onewin_coupons': onewin_coupons,
            'total_onewin': total_onewin,
            'total_onexbet': total_onexbet
        }
    )

