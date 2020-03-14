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

class Event(models.Model):
    class Meta:
        verbose_name = "Подія"
        verbose_name_plural = "Події"
    action_text = models.CharField(max_length=200)
    event_date = models.DateTimeField('Дата та час події')
    notes = models.TextField(blank=True, verbose_name="Додаткова інформація")

    def event_planned(self):
        return self.event_date >= timezone.now('Europe/Kiev') - datetime.timedelta(days=1)

    def __str__(self):
        return self.action_text
