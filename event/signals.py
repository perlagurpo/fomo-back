from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from event.models import Event
from datetime import datetime
from django.utils import timezone

@receiver(post_save, sender=Event)
def generar_slug(sender, instance, **kwargs):
    if not instance.slug:  # Verifica si el slug no está definido
        base_slug = slugify(instance.event_name)
        instance.slug = f"{base_slug}-{instance.id}"
        instance.save()



    # for date in instance.date_to_repeat.all():
    #     fecha_inicio = datetime.combine(date.fecha, datetime.min.time())
    #     fecha_fin = datetime.combine(date.fecha, datetime.max.time())
    #     event_qs = Event.objects.filter(slug__contains=instance.slug.split('-')[0], start_date__range=(fecha_inicio, fecha_fin))
    #     if not event_qs.exists():
    #         try:
    #             data = instance.__dict__.copy()
    #             fecha_aware = timezone.now()
    #             difference = data['start_date'] - data['end_date']
    #             new_date = date.fecha
    #             print(1)
    #             new_date = datetime(new_date.year, new_date.month, new_date.day, data['start_date'].hour, data['start_date'].minute, 0)
    #             print(2)
    #             data['start_date'] = new_date
    #             print(3)
    #             data['end_date'] = new_date - difference
    #             print(4)
    #             try:
    #                 data.pop('_state')
    #             except:
    #                 pass
    #             try:
    #                 data.pop('id')
    #             except:
    #                 pass
    #
    #             Event.objects.create(
    #                 **data
    #             )
    #         except Exception as error:
    #             print(error)

