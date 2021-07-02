from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from django.utils.translation import ugettext_lazy as _


class MyAccauntManager(BaseUserManager):
    def create_user(self, username, password, email=None):
        if not username:
            raise ValueError('User must have an username!')

        user = self.model(username=username)

        if email:
            # is_email_unique = not User.objects.filter(email=email).exists()

            # if not is_email_unique:
            #     raise ValueError('User with given email already exists')

            if User.objects.filter(email=email).exists():
                raise ValueError('User with given email already exists')
            else:
                user.email = self.normalize_email(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email=email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    username = models.CharField(_('username'), max_length=30, unique=True)
    email = models.EmailField(_('email'), max_length=50, blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('last login'), auto_now=True)
    is_admin = models.BooleanField(_('admin'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('super user'), default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccauntManager()

    def __str__(self) -> str:
        return f"{self.username} - {self.email}"