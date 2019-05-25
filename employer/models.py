from django.db import models
from datetime import datetime
from users.models import CustomUser
from PIL import Image
# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key = True)
    company_name = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=127, default='')
    street = models.CharField(max_length=127, blank=True, null=True, default='')
    house_number = models.CharField(max_length=20, default='')
    flat_number = models.CharField(max_length=20, blank=True, null=True, default='')
    email = models.CharField(max_length=127, default='')
    description = models.CharField(max_length=255, default='')
    creation_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='gallery_pics/%Y/%m/%d/', default = 'default.png')
    user = models.ForeignKey(CustomUser, models.DO_NOTHING)

    def __str__(self):
        return str(self.company_name)
    
    def save(self, *args, **kwargs):
        super(Company, self).save(*args, **kwargs)
        # img = Image.open(self.image.path)
        # output_size = (400, 400)
        # img.thumbnail(output_size)
        # img.save(self.image.path)
