from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, mail, name, lastname, password=None):
        if not name or not lastname or not mail:
            raise ValueError("Missing informations")
        user = self.model(mail=self.normalize_email(mail), lastname=lastname, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, mail, name, lastname, password):
        user = self.create_user(mail, name, lastname, password=password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, mail, name, lastname, password):
        user = self.create_user(mail, name, lastname, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    def create_user_from_dict(self, data: dict):
        return self.create_user(
            mail=data['mail'],
            name=data['name'],
            lastname=data['lastname'],
            password=data['password']
        )


class User(AbstractBaseUser):
    mail = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['name', 'lastname']

    def get_full_name(self):
        return self.mail

    def get_short_name(self):
        return self.mail

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    def __str__(self):
        return self.mail

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_adin(self):
        return self.admin
