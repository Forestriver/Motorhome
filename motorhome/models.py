import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    class Meta:
        verbose_name = "Профіль користувача"
        verbose_name_plural = "Профілі користувачів"
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = "Замовник")
    car_model = models.CharField(max_length=30, blank=True, verbose_name = "Модель авто")
    prod_year = models.CharField(max_length=30, blank=True, verbose_name = "Рік виробництва")
    notes = models.TextField(blank=True, verbose_name=u"Додаткова інформація")

    def __str__(self):
        return self.user.username

class Подія(models.Model):
    class Meta:
        verbose_name = "Подія"
        verbose_name_plural = "Події"
    action_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    notes = models.TextField(blank=True, verbose_name="Додаткова інформація")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
