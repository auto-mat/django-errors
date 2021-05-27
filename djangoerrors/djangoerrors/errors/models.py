from django.db import models

class Thing1(models.Model):
    attr = models.CharField(max_length=30)

class Thing2(models.Model):
    attr = models.CharField(max_length=30)
    file = models.FileField(max_length=30)

    def save(self, *args, **kwargs):
        from datetime import datetime
        attr = "foo" + datetime.now().strftime("%H:%M:%S")
        print(attr)

