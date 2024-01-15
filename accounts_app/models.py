from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    AbstractUser,
    UserManager
)

from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('vendor', 'Vendor'),
        ('customer', 'Customer')
    )
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(
        unique = True,
        blank = True,
        null = True
    )
    role = models.CharField(
        _('Role'),
        max_length = 10,
        choices = ROLE_CHOICES,
        blank = True,
        null = True
    )

    is_admin = models.BooleanField(
        _("admin status"),
        default = False
    )
    is_superadmin = models.BooleanField(
        _("superadmin status"),
        default = False
    )

    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now = True
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if self.is_superuser != True:
            self.set_password(self.password)
        else:
            self.is_admin = True
            self.is_superadmin = True
        super().save(*args, **kwargs)
    
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    
    # def has_module_perms(self, app_label):
    #     return True
        

class Profile(models.Model):
    user = models.OneToOneField(
        to = 'User',
        on_delete = models.CASCADE,
        related_name = 'profile',
        blank = True,
        null = True
    )
    profile_picture = models.ImageField(
        upload_to = 'users/profile_pictures',
        blank = True,
        null = True
    )
    cover_picture = models.ImageField(
        upload_to = 'users/cover_pictures',
        blank = True,
        null = True
    )
    address_line1 = models.CharField(
        max_length = 200,
        blank = True,
        null = True
    )
    address_line2 = models.CharField(
        max_length = 200,
        blank = True,
        null = True
    )
    country = models.CharField(
        max_length = 20,
        blank = True,
        null = True
    )
    state = models.CharField(
        max_length = 20,
        blank = True,
        null = True
    )
    pincode = models.CharField(
        max_length = 6,
        blank = True,
        null = True
    )
    latitude = models.CharField(
        max_length = 20,
        blank = True,
        null = True
    )
    longitude = models.CharField(
        max_length = 20,
        blank = True,
        null = True
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        blank = True,
        null = True
    )
    updated_at = models.DateTimeField(
        auto_now = True,
        blank = True,
        null = True
    )
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ('-id', )



