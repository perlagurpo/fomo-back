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



    def save(self, *args, **kwargs):
        if not self.pk:
            # La instancia no se ha guardado en la base de datos todavía, así que generamos el slug
            self.slug = slugify(f'{self.event_name}')
        else:
            # La instancia ya existe en la base de datos, actualizamos el slug si el nombre del evento cambió
            original_instance = MyModel.objects.get(pk=self.pk)
            if original_instance.event_name != self.event_name:
                self.slug = slugify(f'{self.event_name}')
        
        super(MyModel, self).save(*args, **kwargs)