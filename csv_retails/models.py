from django.db import models

class Fashion(models.Model):
    Customer_Reference_ID = models.IntegerField(primary_key=True, unique=True)
    Item_Purchased = models.CharField(max_length=100)
    Purchase_Amount = models.FloatField()
    Review_Rating = models.FloatField()
    Payment_Method = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Customer_Reference_ID} - {self.Item_Purchased}"
