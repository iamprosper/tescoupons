from django.db.models import Count, Q, F
from django.db.models.functions import TruncWeek, TruncDay
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
    # print(days)
    # print(type(days))
    coupons_day_list = [coupon_day for coupon_day in days.values()]
    # print(coupons_day_list)
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
    # print(coupons_stats)
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

    obj_by_weeks = Coupon.objects.filter(pub_date__month=datetime.now().month).annotate(
        week=TruncWeek('pub_date'),
        day=TruncDay('pub_date'),
    ).values('week', 'day', 'code').filter(status='V').order_by('week')

    coupons_validated_img = {}
    for obj in obj_by_weeks:
        week = obj['week'].date().isocalendar().week
        day = obj['day'].strftime('%A')
        img = obj['code']

        if week not in coupons_validated_img:
            coupons_validated_img[week] = {}

        if day not in coupons_validated_img[week]:
            coupons_validated_img[week][day] = []

        coupons_validated_img[week][day].append(img)

    print(coupons_validated_img)

    for k, v in coupons_validated_img.items():
        print("Key {}, Value {}".format(k, v))
        print(v['Tuesday'])
    # ids=[]

    validated_coupon = Coupon.objects.filter(pub_date__month=datetime.now().month).annotate(
        week=TruncWeek('pub_date'),
        day=TruncDay('pub_date'),
    ).values('week', 'day').annotate(
        total=Count('id'),
        validated_count=Count('id', filter=Q(status='V'))
    ).annotate(
        percentage=100.0 * F('validated_count') / F('total'),
    ).order_by('week', 'day')

    coupon_validated_percentage = {}

    # print(validated_coupon)

    for item in validated_coupon:
        week = item['week'].isocalendar().week
        day = item['day'].strftime("%A")
        percentage = int(item['percentage'])
        # model_id = item['id']

        if week not in coupon_validated_percentage:
            coupon_validated_percentage[week] = {}

        if day not in coupon_validated_percentage[week]:
            coupon_validated_percentage[week][day] = percentage

        # coupon_validated_percentage[week][day].append(percentage)

    print(coupon_validated_percentage)

    # print(obj_by_weeks)

    data_by_week_and_day = {}

    weeks_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # for obj in obj_by_weeks:
    #     week = obj['week']
    #     day = obj['day']
    #     total = obj['total']
    #     validated_count = obj['validated_count']
    #     week_key = week.date().isocalendar().week
    #     day_key = day.strftime("%A")
    #     if validated_count > 0:
    #         if week_key not in data_by_week_and_day:
    #             data_by_week_and_day[week_key] = {}
    #         if day_key not in data_by_week_and_day[week_key]:
    #             data_by_week_and_day[week_key][day_key] = {'percentage': 0, 'coupons': []}
    #         percentage = int((validated_count / total) * 100)
    #         data_by_week_and_day[week_key][day_key]['percentage'] = percentage
    #         data_by_week_and_day[week_key][day_key]['coupons'].append(obj)
    # week_list = [obj for obj in data_by_week_and_day.keys()]
    # print(data_by_week_and_day.values())

    # for items in data_by_week_and_day.items():
    #     print("Values: {}".format(items))

        # print("Key: {}, Value: {}".format(k, v))
        # for kk, vv in data_by_week_and_day[v]:
        #     print("Key: {}, Value: {}".format(kk, vv))


    # print(week_list)
    # print(day_list)

    # for week in week_list:
    #     print(week)


    # week_list = [week.date() for week in week_list]
    # day_list = [day.date() for day in day_list]
    # obj_details = Coupon.objects.filter(
    #     # pub_date__in=[
    #     #     obj.pub_date
    #     #     for obj in Coupon.objects.all()
    #     #     if datetime.strftime(obj.pub_date, "%U") in map(str, week_list)
    #     # ]
    #     Q(status='V')
    # )

    # res = [obj.pub_date for obj in Coupon.objects.all() if datetime.strftime(obj.pub_date, "%U") in map(str, week_list)]
    # print(res)
    # print(obj_details)
    # for obj in obj_details:
    #     print(obj.pub_date.isocalendar().week)
    # for k, v in data_by_week_and_day.items():
    #     print(k, v)
    # # print(data_by_week_and_day)
    # print(data_by_week_and_day.keys())

    return render(
        request,
        'pronos/index.html',
        {
            'onexbet_coupons': onexbet_coupons,
            'onewin_coupons': onewin_coupons,
            'total_onewin': total_onewin,
            'total_onexbet': total_onexbet,
            # 'weeks': weeks,
            # 'days': days.values(),
            'coupons_per_day': dict_stats.values(),
            'coupons_stats': coupons_stats,
            'datas': data_by_week_and_day,
            "weeks_day": weeks_days,
            'coupons_percentages': coupon_validated_percentage,
            'coupons_imgs': coupons_validated_img,
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



