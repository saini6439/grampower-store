from django.db import models

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=250)
    products = models.CharField(max_length=250)
    cover = models.FileField(upload_to= 'cover/')
    lang = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lot = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self):
        return self.name

class PostImage(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.store.name
#
class StoreOpening(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, default=None, on_delete=models.CASCADE)
    sunday_from_hour = models.TimeField()
    monday_from_hour = models.TimeField()
    tuesday_from_hour = models.TimeField()
    wednesday_from_hour = models.TimeField()
    thrusday_from_hour = models.TimeField()
    friday_from_hour = models.TimeField()
    saturday_from_hour = models.TimeField()
    sunday_to_hour = models.TimeField()
    monday_to_hour = models.TimeField()
    tuesday_to_hour = models.TimeField()
    wednesday_to_hour = models.TimeField()
    thrusday_to_hour = models.TimeField()
    friday_to_hour = models.TimeField()
    saturday_to_hour = models.TimeField()

    def __str__(self):
        return self.store.name
