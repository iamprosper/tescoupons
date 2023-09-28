from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


# Create your models here.


class Coupon(models.Model):
    ONEWIN = "1w"
    ONEXBET = "1x"
    BOOKMAKER_CHOICES = [
        (ONEWIN, '1win'),
        (ONEXBET, '1xbet'),
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

    code = models.CharField(max_length=5,
                            help_text="Uniquement requis pour le bookmaker 1xbet",
                            blank=True)

    img = models.ImageField(upload_to='uploads/')
    status = models.CharField(
        max_length=1,
        choices=STATUT_CHOICES,
        default=ACCEPTED
    )

    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.bookmaker == "1x" and not self.code:
            raise ValidationError("Code requis pour 1x bet")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Coupon, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.bookmaker, self.code)


class MailParieur(models.Model):
    email = models.EmailField(max_length=254)
