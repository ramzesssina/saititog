from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from .models import Task

@receiver(post_save, sender=Task)
def post_save_task(created, **kwargs):
    instance = kwargs['instance']
    if created:
        print(f'Пользователь {instance.title} создан')
    else:
        print(f'Пользователь {instance.title} создан')

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_task(created, **kwargs):
    instance = kwargs['instance']
    if created:
        print(f'Пользователь {instance.username} создан')
    else:
        print(f'Пользователь {instance.username} обновлен')
