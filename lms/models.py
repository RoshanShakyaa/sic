from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='courses', null=False, blank=False)
    credit_hour = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.name