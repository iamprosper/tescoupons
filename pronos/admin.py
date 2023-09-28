from django.contrib import admin
from django.contrib.admin import AdminSite
from django.db.models import F

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

    def __init__(self, *args, **kwargs):
        super(CouponAdminForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            if instance.bookmaker == "1x":
                self.fields['code'].required = True
            else:
                self.fields['code'].required = False
                self.fields['code'].widget.attrs['disabled'] = 'disabled'

    # def clean(self):
    #     cleaned_data = super().clean()
    #     code = self.fields.get('code')
    #     bookmaker = cleaned_data.get('bookmaker')
    #     # bookmaker = self.cleaned_data.get('bookmaker')
    #     if bookmaker == '1x' and code:
    #         code.required = True
    #     elif code:
    #         code.required = False


class CouponAdmin(admin.ModelAdmin):
    form = CouponAdminForm
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

    def jour_pub_sort(self, obj):
        return obj.pub_date

    jour_pub.admin_order_field = F('pub_date')
    """
    def image_display(self, obj):
        return f'<img src="{obj.img.url}" width="100" height="100" />'

    #image_display.allow_tags = True
    image_display.short_description = "Image du coupon"
    """


# admin_site = PronosAdminSite(name="pronos_admin")
# admin_site.language = 'fr'

admin.site.register(Coupon, CouponAdmin)
