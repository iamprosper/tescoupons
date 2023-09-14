from django.contrib import admin
from .models import Coupon


# Register your models here.
class CouponAdmin(admin.ModelAdmin):
    list_display = ('bookmaker', 'code', 'img', 'status')

    """
    def image_display(self, obj):
        return f'<img src="{obj.img.url}" width="100" height="100" />'

    #image_display.allow_tags = True
    image_display.short_description = "Image du coupon"
    """


admin.site.register(Coupon, CouponAdmin)
