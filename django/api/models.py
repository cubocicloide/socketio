from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None):
        user = self.model(
            username=self.normalize_email(email),
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.email)
