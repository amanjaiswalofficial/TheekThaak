from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Customer

# Create your views here.


def login_page(request):
    return render(request, 'accounts/login.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        gender = request.POST.get('gender')
        phone_number = request.POST['phone_number']

        # Checks whether both passwords are same
        if password1 == password2:

            # Checks if given email already exists or not
            if Customer.objects.filter(username=username).exists():
                messages.error(request, 'This username already exists')
                return redirect('registration')
            else:
                if Customer.objects.filter(email=email).exists():
                    messages.error(request, 'This email already exists')
                    return redirect('registration')
                else:
                    user = Customer.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                        email=email, password=password1, gender=gender,
                                                        phone_number=phone_number)
                    user.save()
                    messages.success(request, 'You are now registered')
                    send_mail(
                        'You are now registered',
                        'Thank you ' + first_name + ' for registering with us.',
                        'amulya.sharma@tothenew.com',
                        [email],
                        fail_silently=False
                    )
                    return redirect('loginapp')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('registration')
    else:
        return render(request, 'accounts/register.html')

