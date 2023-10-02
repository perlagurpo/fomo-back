from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from event.models import Event


@receiver(post_save, sender=Event)
def generar_slug(sender, instance, **kwargs):
    if not instance.slug:  # Verifica si el slug no está definido
        base_slug = slugify(instance.event_name)
        instance.slug = f"{base_slug}-{instance.id}"
        instance.save()