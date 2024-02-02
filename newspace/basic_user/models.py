from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.contrib.auth import password_validation
from django import forms

class BasicUserManager(BaseUserManager):
    def create_user(self, email, password):
    # End User Account
        basic_user = self.model(
                email =  self.normalize_email(email)
            )
        
        basic_user.is_active = True
        basic_user.is_staff  = False
        basic_user.is_superuser = False

        basic_user.set_password(password)
        basic_user.save()

        return basic_user
    

    def create_superuser(self, email, password):
        basic_user = self.create_user(
            email = self.normalize_email(email),
            password = password,

        )
    
        basic_user.is_active = True
        basic_user.is_staff = True
        basic_user.is_superuser = True 
        basic_user.set_password(password)
        basic_user.save()
        return basic_user
    

class BasicUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name = "Email do Usuário",
        max_length = 194,
        unique=True,
    )


    is_active = models.BooleanField(
        verbose_name = "Usuário está ATIVO",
        default =  True,
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário é um empregado nosso",
        default = False,
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuário é um administrador",
        default = False,
    )

    USERNAME_FIELD = "email"
    objects = BasicUserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuário"
        db_table = "user"

    def clean(self):
        if self.password:
            try:
                password_validation.validate_password(self.password)

            except forms.ValidationError as error:
                raise forms.ValidationError('You need a stronger password.')


    def __str__(self):
        return self.email
    


        

        