from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.quote