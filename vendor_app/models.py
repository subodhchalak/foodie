from django.db import models
from accounts_app.models import (
    User,
    Profile
)

# Create your models here.



class Vendor(models.Model):
    user = models.OneToOneField(
        to = User,
        on_delete = models.CASCADE,
        related_name = 'vendor'
    )
    profile = models.OneToOneField(
        to = Profile,
        on_delete = models.CASCADE,
        related_name = 'vendor'
    )
    name = models.CharField(
        max_length = 100,
        blank = False,
        null = False
    )
    license_image = models.ImageField(
        upload_to = 'vendors/license_image',
        blank = True,
        null = True
    )
    is_approved = models.BooleanField(
        default = False
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-id', )