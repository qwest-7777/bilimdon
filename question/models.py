import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from payments.models import BasePayment
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=False, unique=True)

    def __str__(self):
        return self.username


class Payment(BasePayment):
    pass

  

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    LANG_CHOICES = (
    ('uz', "O'zbekcha"),
    ('ru', 'Русский'),
    )
    question_language = models.CharField(max_length=2,
        choices=LANG_CHOICES,
        default="UZ",)

  

    def __str__(self):
        return self.question_text

    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    published_recently.admin_order_field = 'pub_date'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    result = models.BooleanField(default=False)
    
    def __str__(self):
        return self.choice_text


class Statistic(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    right_answer = models.IntegerField(default=0, blank=True)
    false_answer = models.IntegerField(default=0, blank=True)


class Answered(models.Model):
    answered_user = models.CharField(max_length=50, null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    failed_answer = models.BooleanField(null=True, default=False)
    answered_time = models.DateTimeField(auto_now_add=True)


def create_statistic_count(sender, instance, created, **kwargs):
    if created:
        Statistic.objects.create(user=instance)

post_save.connect(create_statistic_count, sender=CustomUser)
