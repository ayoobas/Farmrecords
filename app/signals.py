from django.contrib.auth.models import User
from .models import Staff
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def save_staff_profile(sender, instance, created, **kwargs):
    if created:
        # create staff profile automatically for new users
        Staff.objects.create(staff=instance)
    else:
        # only save if staff record exists
        if hasattr(instance, 'staff'):
            instance.staff.save()