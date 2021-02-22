from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

@receiver(post_save,sender=get_user_model())
def assign_group(sender,instance,created,**kwargs):
    if created:
        Organiser=Group.objects.get(name='Organiser')
        Member=Group.objects.get(name='Member')
        if instance.category == 'Organiser':
            instance.groups.add(Organiser)
        else:
            instance.groups.add(Member)