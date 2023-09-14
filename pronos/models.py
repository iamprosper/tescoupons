from django.db import models
from django.utils import timezone


# Create your models here.


class Coupon(models.Model):
    ONEWIN = "1w"
    ONEXBET = "1x"
    BOOKMAKER_CHOICES = [
        (ONEWIN, '1win'),
        (ONEWIN, '1xbet'),
    ]
    VALIDATED = "V"
    ACCEPTED = "N"
    LOST = "P"
    STATUT_CHOICES = [
        (VALIDATED, "Validé"),
        (ACCEPTED, "Accepté"),
        (LOST, "Perdu"),
    ]
    bookmaker = models.CharField(
        max_length=4,
        choices=BOOKMAKER_CHOICES,
        default=ONEXBET
    )
    code = models.CharField(max_length=5)
    img = models.ImageField(upload_to='uploads/%Y/%M/%d')
    status = models.CharField(
        max_length=1,
        choices=STATUT_CHOICES,
        default=ACCEPTED
    )
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {}".format(self.bookmaker, self.code)


class MailParieur(models.Model):
    email = models.EmailField(max_length=254)