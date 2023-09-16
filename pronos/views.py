from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Coupon
from datetime import datetime


def index(request):
    coupons = Coupon.objects.all()
    onewin_coupons = Coupon.objects.filter(bookmaker="1w")
    onexbet_coupons = Coupon.objects.filter(bookmaker="1x")
    # counter = 0
    total_onewin = onewin_coupons.count()
    total_onexbet = onexbet_coupons.count()
    (test_coupons, dict_stats) = stats()
    weeks = test_coupons.keys()
    dict_days = test_coupons.values()
    days = {}
    for dd in dict_days:
        days = dd

    # for day in days:

    # days = test_coupons.values()
    # template = loader.get_template("pronos/index.html")
    # return HttpResponse(template.render(None, request))
    return render(
        request,
        'pronos/index.html',
        {
            'onexbet_coupons': onexbet_coupons,
            'onewin_coupons': onewin_coupons,
            'total_onewin': total_onewin,
            'total_onexbet': total_onexbet,
            'weeks': weeks,
            'days': days.values(),
            'coupons_per_day': dict_stats.values()
        }
    )


def stats():
    month_coupon = Coupon.objects.filter(pub_date__month=datetime.now().month)
    verbose_weeks = "Semaine {}"
    days = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
    }
    weeks = {}
    weeks_stats = {}
    dict_stats = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
    }
    # Fetching last 4 weeks bets
    for coupon in month_coupon:
        week_number = verbose_weeks.format(coupon.pub_date.date().isocalendar()[1])
        day_number = str(coupon.pub_date.date().isoweekday() - 1)
        if not week_number in weeks.keys():
            weeks[week_number] = days
            weeks_stats[week_number] = dict_stats
            # weeks[week_number][day_number] = 1
        # else:
        #     if not day_number in weeks[week_number].keys():
        #         weeks[week_number][day_number] = 1
        #     else:
        #         weeks[week_number][day_number] += 1
        dict_stats[day_number] += 1
        weeks[week_number][day_number].append(coupon)

    return  weeks, dict_stats



