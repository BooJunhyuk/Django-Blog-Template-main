from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager

# db로 쿼리를 보낼때 제공해주는 인터페이스?

class UserManager(DjangoUserManager):
     def _create_user(self, username, email, password, **extra_fields):
         '''if not email:
             raise ValueError('이메일은 필수 값입니다.')''' # 만약 이메일 필수값이면
         user = self.model(username=username, email=email, **extra_fields)
         user.set_password(password) #암호화해서 넣어(해싱처리)
         user.save(using=self._db)
         return user
         
     def create_user(self, username, email=None, password=None, **extra_fields): # email 필요없
         extra_fields.setdefault('is_staff', False)
         extra_fields.setdefault('is_superuser',False)
         return self._create_user(username, email,password,**extra_fields)
     
     def create_superuser(self, username, email=None, password=None, **extra_fields):     
         extra_fields.setdefault('is_staff', True)
         extra_fields.setdefault('is_superuser',True)
         return self._create_user(username, email,password,**extra_fields)

class User(AbstractUser):
    mbti = models.CharField(verbose_name='MBTI',max_length=5)
    
    objects = UserManager()


