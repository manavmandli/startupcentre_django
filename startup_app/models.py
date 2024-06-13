from django.db import models
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-created_at']
        
        
class FreeQuote(models.Model):
    SERVICE_CHOICES = [
        ('Business Consultancy', 'Business Consultancy'),
        ('Certification', 'Certification'),
        ('Government Grants', 'Government Grants'),
        ('Funding', 'Funding'),
    ]
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    select_service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
        verbose_name="Selected Service"
    )
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    class Meta:
        verbose_name = "Free Quote"
        verbose_name_plural = "Free Quotes"
        ordering = ['-created_at']
        
class Subscribe(models.Model):
    email = models.EmailField(verbose_name="Email", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
        
    def __str__(self):
        return self.email