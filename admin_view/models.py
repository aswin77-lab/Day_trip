from django.db import models

# Create your models here.
class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    TRIP_TYPES = (
        ('AD', 'Adventure'),
        ('BE', 'Beach'),
        ('CU', 'Cultural'),
        ('CR', 'Cruise'),
        ('EC', 'Eco'),
        ('FD', 'Food & Drink'),
        ('HI', 'Hiking'),
        ('SA', 'Safari'),
        ('SI', 'Sightseeing'),
        ('WE', 'Wellness'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    trip_type = models.CharField(max_length=2, choices=TRIP_TYPES)
    duration = models.PositiveIntegerField(help_text="Duration in days",default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    capacity = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    difficulty = models.CharField(
        max_length=1,
        choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')],
        default='M')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/trips/')
    def __str__(self):
        return f"{self.name} ({self.location})"


class TourGuide(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128) 
    bio = models.TextField()
    languages = models.CharField(max_length=200)
    years_experience = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name