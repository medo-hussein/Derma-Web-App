from django.db import models
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.core.validators import RegexValidator
class CustomUserManager(BaseUserManager):
    def create_user(self,first_name,last_name,e_mail,Phone,password,user_id,user_address,**extra_field):
        if not first_name or not last_name or not e_mail or not Phone or not password or not user_id or not user_address:
            raise ValueError("all fields shouldn't be empty")
        e_mail = self.normalize_email(e_mail)
        user    = self.model(first_name=first_name,last_name=last_name,e_mail=e_mail,Phone=Phone,user_id=user_id,user_address=user_address,**extra_field)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,first_name,last_name,e_mail,Phone,password,user_id,user_address,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get("is_superuser")is not True:
            raise ValueError("superuser must have is superuser=True")
        return self.create_user(first_name,last_name,e_mail,Phone,password,user_id,user_address,**extra_fields)
class User(AbstractBaseUser,PermissionsMixin):
    is_superuser= models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active =models.BooleanField(default=False)
    first_name = models.CharField(max_length=255,null=False, blank=False)
    last_name  = models.CharField(max_length=255,null=False, blank=False)
    Phone   = models.CharField(max_length=11,null=False, blank=False,validators=[RegexValidator("^[0-9]{11,11}$",message ='Enter valid Egyptian phone number')])
    e_mail  = models.EmailField(max_length=255,null=False, blank=False,unique=True)
    user_id = models.CharField(max_length=14,primary_key=True,null=False, blank=False,validators=[RegexValidator("^[0-9]{14,14}$",message ='Enter valid Egyptian national identity number')])
    user_address = models.CharField(max_length=255,null=False, blank=False)
    REQUIRED_FIELDS = ["first_name","last_name","Phone", "user_id","user_address"]
    USERNAME_FIELD = "e_mail"
    objects = CustomUserManager()

class diesease(models.Model):
    name=models.CharField(max_length=30)
    descript=models.TextField()