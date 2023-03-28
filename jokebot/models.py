from django.db import models

# Create your models here.

class noOfCalls(models.Model):
    user_id = models.CharField(max_length = 50)
    stupid = models.IntegerField(default = 0)
    fat = models.IntegerField(default = 0)
    dumb = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return self.user_id