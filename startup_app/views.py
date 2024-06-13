import django
from django.urls import reverse
from startup_app.models import Contact,FreeQuote,Subscribe
from django.shortcuts import redirect, render
from django.contrib import messages


def handle_subscription(request):
    if request.method == 'POST' and 'subscribe_form' in request.POST:
        email = request.POST.get('subscribe_email')
        Subscribe.objects.create(email=email)
        return render(request, 'startupcentre/home.html', {'subscribe_success': True})
    return None

def home(request):
    subscription_result = handle_subscription(request)
    if subscription_result:
        return subscription_result
    if request.method == 'POST' and 'quote_form' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('services')
        message = request.POST.get('message')
        new_quote = FreeQuote.objects.create(name=name, email=email, select_service=service, message=message)
        new_quote.save()
        return render(request, 'startupcentre/home.html', {'quote_success': True})
    return render(request, 'startupcentre/home.html')

def about(request):
    subscription_result = handle_subscription(request)
    if subscription_result:
        return subscription_result
    return render(request, 'startupcentre/about.html')

def services(request):
    subscription_result = handle_subscription(request)
    if subscription_result:
        return subscription_result
    return render(request, 'startupcentre/service.html')

def blog(request):
    subscription_result = handle_subscription(request)
    if subscription_result:
        return subscription_result
    return render(request, 'startupcentre/blog.html')

def career(request):
    subscription_result = handle_subscription(request)
    if subscription_result:
        return subscription_result
    return render(request, 'startupcentre/career.html')

def condition(request):
    return render(request,'startupcentre/conditions.html')

def testimonials(request):
    subscription_result = handle_subscription(request)
    if subscription_result:
        return subscription_result
    return render(request, 'startupcentre/testimonial.html')

def free_quote(request):
    subscription_result = handle_subscription(request)
    if subscription_result:
        return subscription_result
    if request.method == 'POST' and 'quote_form' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('services')
        message = request.POST.get('message')
        new_quote = FreeQuote.objects.create(name=name, email=email, select_service=service, message=message)
        new_quote.save()
        messages.success(request, "Your request for quote send succesfully!")
        return redirect('startup_app:home')
    return render(request, 'startupcentre/quote.html')

def contact(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        new_contact=Contact.objects.create(name=name,email=email,phone_number=mobile,message=message)  
        new_contact.save()
        messages.success(request, "Your message has been sent successfully!")
        return redirect('startup_app:contact')
    return render(request, 'startupcentre/contact.html')