from django.db import models  

class OptionChainSnapshot(models.Model): # Use models.Model here
    symbol = models.CharField(max_length=20)
    expiry_date = models.DateField()
    strike_price = models.FloatField()
    option_type = models.CharField(max_length=2) 
    last_price = models.FloatField()
    open_interest = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} - {self.strike_price} {self.option_type}"