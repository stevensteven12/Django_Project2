import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class K_Line_Raw(models.Model):
   # StockNO = models.ForeignKey(User)
    StockNO = models.CharField(max_length=20)

    trade_date = models.DateTimeField(default=timezone.now)
    tick_time = models.DateTimeField(default=timezone.now)
    HighValue = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    LowValue = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    RedGreen = models.CharField(max_length=1, default="E")
    TradeQty = models.DecimalField(max_digits=5, decimal_places=2, default= 0)

    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.StockNO

