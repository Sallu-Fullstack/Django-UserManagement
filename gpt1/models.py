from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    user_id = models.IntegerField(unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            max_id = User.objects.all().aggregate(models.Max('user_id'))['user_id__max'] or 0
            self.user_id = max_id + 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['user_id']

        