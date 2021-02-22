from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    slug=models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)

class Event(models.Model):
    name=models.CharField(max_length=250)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='event/')
    organiser=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create_date=models.DateTimeField(auto_now_add=True)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    vanue=models.CharField(max_length=250)
    maximum_participants=models.PositiveIntegerField()
    description=models.TextField()
    slug=models.SlugField(blank=True)
    slot_booked=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def remaining_slot(self):
        remain=self.maximum_participants-self.slot_booked
        return remain

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)

class BookEvent(models.Model):
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)