from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.utils.translation import gettext_lazy as _
from orders.models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver


# from django.contrib.auth.models import AbstractUser


# class UserProfile(AbstractUser):
#     middle_name = models.CharField(_('first name'), max_length=30, blank=True)
#     phone = PhoneField(_('phone number'), help_text='Contact phone number', unique=True)
#     destination_address = models.TextField(_('destination address'), blank=True, null=True)
#     birth_date = models.DateField(_('birthday'), null=True, blank=True)
#     profile_picture = models.ImageField(_('profile picture'), upload_to='profile_pics', blank=True)
#

class CustomerProfile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)

    middle_name = models.CharField(_('first name'), max_length=30, blank=True)
    phone = PhoneField(_('phone number'), help_text='Contact phone number')
    birth_date = models.DateField(_('birthday'), null=True, blank=True)
    destination_address = models.TextField(_('destination address'), blank=True, null=True)
    profile_picture = models.ImageField(_('profile picture'), upload_to='profile_pics', blank=True)
    orders = models.ManyToManyField(Order, related_name='ordered_by')

    def __str__(self):
            return self.user.username


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    instance.customerprofile.save()

