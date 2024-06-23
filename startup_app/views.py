import django
from django.urls import reverse
from startup_app.models import Contact,FreeQuote,Subscribe
from django.shortcuts import redirect, render
from django.contrib import messages


def handle_subscription(request):
	if request.method == 'POST' and 'subscribe_form' in request.POST:
		email = request.POST.get('subscribe_email')
		if Subscribe.objects.filter(email=email).exists():
			messages.success(request, "You are already subscribed")
			return redirect('startup_app:home')
		Subscribe.objects.create(email=email)
		messages.success(request, "Thanks For the Subscription")
		return redirect('startup_app:home')
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
		messages.success(request, "Thank you for your quote request. We will connect with you soon.")
		return redirect('startup_app:home')
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
	subscription_result = handle_subscription(request)
	if subscription_result:
		return subscription_result
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
		messages.success(request, "Thank you for your quote request. We will connect with you soon.")
		return redirect('startup_app:home')
	return render(request, 'startupcentre/quote.html')

def contact(request):
	subscription_result = handle_subscription(request)
	if subscription_result:
		return subscription_result 
	if request.method == 'POST' and 'contact_form' in request.POST:
		name = request.POST.get('name')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		message = request.POST.get('message')
		new_contact=Contact.objects.create(name=name,email=email,phone_number=mobile,message=message)  
		new_contact.save()
		messages.success(request, "Your message has been sent successfully!")
		return redirect('startup_app:home')
	return render(request, 'startupcentre/contact.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)