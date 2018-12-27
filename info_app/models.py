from django.db import models

# Create your models here.
# Create your models here.
class model_cars(models.Model):
    model = models.CharField(max_length=128)
    make = models.CharField(max_length=128)
    year = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    mileage = models.CharField(max_length=128)
    engine = models.CharField(max_length=128)
    transmission = models.CharField(max_length=128)
    vin = models.CharField(max_length=128)
    MSRP = models.CharField(max_length=128)
    savings = models.CharField(max_length=128)
    moreinfo = models.TextField(max_length=2048)
    headpic = models.ImageField()

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("info_app:detail",kwargs={'pk':self.pk})

class model_carspic(models.Model):
    pic = models.ImageField()
    car = models.ForeignKey(model_cars,models.CASCADE,related_name='carpic')
