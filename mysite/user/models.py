from django.db import models

# Create your models here.
class user(models.Model):
    user = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    token = models.CharField(verbose_name="TOKEN", max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'db_user'