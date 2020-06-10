from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    FACULTY = [
        ('Faculty of science', 'Faculty of science'),
        ('Faculty of education', 'Faculty of education'),
        ('Faculty of law', 'Faculty of law'),
        ('Faculty of agric', 'Faculty of agric'),
        ('Faculty of arts', 'Faculty of arts'),
    ]

    matric_no = models.CharField(_('Matric Number'), max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    faculty = models.CharField(max_length=30, null=True, choices=FACULTY)
    Department = models.CharField(max_length=30, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    is_superuser = models.BooleanField(_('superuser'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)




    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('username')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)



class Poll(models.Model):
    name = models.CharField(max_length=20, null=True, default=1)

    def __str__(self):
        return self.name

class Option(models.Model):


    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name










class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()