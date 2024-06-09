from django.db import models
from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-created_at']
        
        
class FreeQuote(models.Model):
    SERVICE_CHOICES = [
        ('web_design', 'Web Design'),
        ('seo', 'SEO'),
        ('digital_marketing', 'Digital Marketing'),
        ('content_writing', 'Content Writing'),
        ('app_development', 'App Development'),
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