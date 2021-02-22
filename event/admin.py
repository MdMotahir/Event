from django.contrib import admin
from event.models import Category,Event,BookEvent
# Register your models here.
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(BookEvent)
