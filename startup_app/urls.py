from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from .views import custom_404

handler404 = custom_404


app_name = 'startup_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('about',views.about, name="about"),
    path('services',views.services, name="services"),
    path('blog',views.blog, name="blog"),
    path('career',views.career,name="career"),
    path("condition", views.condition, name="condition"),
    path('testimonials',views.testimonials,name="testimonials"),
    path('free_quote',views.free_quote,name='free_quote'),
    path('contact',views.contact,name='contact'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)