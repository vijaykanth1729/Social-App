from django.contrib.auth.models import User
from .models import Profile, RelationShip
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=RelationShip)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'accepted':
        # extending friends list based on invitation..
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()
