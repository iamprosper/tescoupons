from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Coupon
from django import forms
from django.utils.translation import gettext  as _


class PronosAdminSite(AdminSite):
    site_title = _("Interface d'administration")
    site_header = _("Administration")


class CouponAdminForm(forms.ModelForm):
    class Meta:
        model = Coupon
        exclude = ['pub_date', 'updated_at']


class CouponAdmin(admin.ModelAdmin):
    list_display = ('bookmaker', 'code', 'img', 'status', 'jour_pub')

    def jour_pub(self, obj):
        pub_clean_date = obj.pub_date.strftime(str(_('%A, %d %B %Y at %Hh %Mmin')))
        days = {
            "Monday": "Lundi",
            "Tuesday": "Mardi",
            "Wednesday": "Mercredi",
            "Thursday": "Jeudi",
            "Friday": "Vendredi",
            "Saturday": "Samedi",
            "Sunday": "Dimanche",
        }
        months = {
            "January": "Janvier",
            "February": "Février",
            "Mars": "Mars",
            "April": "Avril",
            "May": "Mai",
            "June": "Juin",
            "July": "Juillet",
            "August": "Août",
            "September": "Septembre",
            "October": "Ocotbre",
            "November": "Novembre",
            "December": "Décembre",
        }

        for day in days:
            if day in pub_clean_date:
                pub_clean_date = pub_clean_date.replace(day, days[day])
                break

        for month in months:
            if month in pub_clean_date:
                pub_clean_date = pub_clean_date.replace(month, months[month])
                break

        return pub_clean_date

    jour_pub.short_description = _("Date de publication")
    """
    def image_display(self, obj):
        return f'<img src="{obj.img.url}" width="100" height="100" />'

    #image_display.allow_tags = True
    image_display.short_description = "Image du coupon"
    """


# admin_site = PronosAdminSite(name="pronos_admin")
# admin_site.language = 'fr'
admin.site.register(Coupon, CouponAdmin)
