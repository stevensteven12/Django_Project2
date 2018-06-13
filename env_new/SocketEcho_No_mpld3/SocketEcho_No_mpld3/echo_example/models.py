from django.db import models


class tbIndexTable(models.Model):
    StockNO = models.CharField(blank=False, max_length=20)
    TradeDate = models.CharField(blank=False, max_length=20)
    TickTime = models.CharField(blank=False, max_length=20)
    P_Open = models.DecimalField(max_digits=10, decimal_places=2)
    P_High = models.DecimalField(max_digits=10, decimal_places=2)
    P_Low = models.DecimalField(max_digits=10, decimal_places=2)
    P_Close = models.DecimalField(max_digits=10, decimal_places=2)
    TradeQty = models.DecimalField(max_digits=10, decimal_places=2)
    Ave_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Red = models.CharField(max_length=4)

    def __unicode__(self):
        return self.name


class tbTradeRecord(models.Model):
    StockNO = models.CharField(blank=False, max_length=20)
    TradeDate = models.CharField(blank=False, max_length=20)
    TickTime = models.CharField(blank=False, max_length=20)
    BuyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    SellPrice = models.DecimalField(max_digits=10, decimal_places=2)
    TradePrice = models.DecimalField(max_digits=10, decimal_places=2)
    Qty = models.DecimalField(max_digits=8, decimal_places=0)
    AveP = models.DecimalField(max_digits= 10, decimal_places=2)
    BuyQty = models.DecimalField(max_digits=8, decimal_places=0)
    SellQty = models.DecimalField(max_digits=8, decimal_places=0)
    TickQty = models.DecimalField(max_digits=8, decimal_places=0)
    AllQty = models.DecimalField(max_digits=8, decimal_places=0)
    TickNO = models.DecimalField(max_digits=10, decimal_places=0)


    def __unicode__(self):
        return self.title
