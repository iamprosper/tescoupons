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
    validated = 0
    for dd in dict_days:
        days = dd
    print(days)
    print(type(days))
    coupons_day_list = [coupon_day for coupon_day in days.values()]
    print(coupons_day_list)
    stats_coupon = {}
    day = 0
    coupons_stats = []
    for coupons_day in coupons_day_list:
        count = 0
        stat = ""
        # coupons_validated = []
        for coupon in coupons_day[:]:
            if coupon.status != "V":
                coupons_day.remove(coupon)
            else:
                # coupons_validated.append(coupon)
                count += 1
        if dict_stats["{}".format(day)] > 0 and count > 0:
            stat = "{}%".format((count * 100) // dict_stats["{}".format(day)])
        else:
            if dict_stats["{}".format(day)] > 0:
                stat = "0%"
            else:
                stat = 'No posts'
        stats_coupon["{}".format(day)] = {
            stat: coupons_day
        }
        coupons_stats.append([stat, coupons_day])
        day += 1
    # for item in coupons_stats:
    #     print(item)
    print(coupons_stats)
    # print(stats_coupon)
    # for day_stat in stats_coupon:
    #     print("{} - {}".format(day_stat, stats_coupon[day_stat]))
    # print(coupons_day_list)
    # print("..................")
    # days_stats = [item for item in stats_coupon.values()]
    # print(days_stats)
    # print(type(days_stats))
    # for day_stat in days_stats:
    #     print("{}".format(day_stat.items()))
    #     print(type(day_stat.items()))
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
            'coupons_per_day': dict_stats.values(),
            'coupons_stats': coupons_stats,
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

    return weeks, dict_stats



