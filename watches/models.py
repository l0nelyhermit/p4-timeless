from django.db import models
import uuid

# Create your models here.


class Watch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    watch_brand = models.CharField(max_length=255, blank=False)
    watch_model = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    watch_price = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.watch_brand
