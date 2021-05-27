from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import datetime

class Thing1(models.Model):
    attr = models.CharField(max_length=30)

class Thing2(models.Model):
    attr = models.CharField(max_length=30)
    file = models.FileField(max_length=30)

    def save(self, *args, **kwargs):
        attr = "Save method run " + datetime.now().strftime("%H:%M:%S")
        print(attr)
        super().save(*args, **kwargs)

def post_save_function(sender, instance, created, **kwargs):
    attr = "Post save method run " + datetime.now().strftime("%H:%M:%S")
    print(attr)

post_save.connect(post_save_function, sender=Thing2)
