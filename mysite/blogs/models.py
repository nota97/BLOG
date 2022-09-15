from django.db import models

# Create your models here.
class blogs(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'db_blogs'