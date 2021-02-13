from django.db import models
from django.utils import timezone
from django.db import transaction
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

class UserManager(BaseUserManager):
 
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
 
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length = 40,
        unique = True,
        null = False
    )
    name = models.CharField(max_length = 30, null = False)
    city = models.CharField(max_length = 30, null = False)
    age = models.IntegerField(default = 0)
    visitors = models.IntegerField(default = 0)
    verified = models.CharField(max_length = 30, default = False)
    GENRE_CHOICES = [
        ('F', 'FEMALE'),
        ('M', 'MALE'),
    ]
    genre = models.CharField(
        max_length = 1,
        choices = GENRE_CHOICES,
        null = False
    )
    FEELINGS_CHOICES = [
        ('H', 'HAPPY'),
        ('A', 'ANGRY'),
        ('S', 'SAD'),
        ('M', 'MOTIVATED'),
        ('B', 'BORED')
    ]
    feeling = models.CharField(
        max_length = 1,
        choices = FEELINGS_CHOICES,
        blank = True
    )
    # friends = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_created = models.DateTimeField(default = timezone.now)
    date_modified = models.DateTimeField(null = True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
