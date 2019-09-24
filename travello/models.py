from django.db import models

# inital model without database
# # Create your models here.
# class Destination:
#     id : int
#     name : str
#     img : str
#     desc : str
#     price : int
#     offer : bool # For specifying True/False

# model with database

class Destination(models.Model):

    name = models.Varchar(max_length = 50)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField
    offer = models.BooleanField(default = False)