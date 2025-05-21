from django.db import models

class EventType(models.TextChoices):
    PERSONAL = 'personal', 'Personal'
    PROFESSIONAL = 'professional', 'Professional'

class Visibility(models.TextChoices):
    PUBLIC = 'public', 'Public'
    PRIVATE = 'private', 'Private'
