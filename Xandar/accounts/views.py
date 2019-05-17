import random

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from accounts.forms import UserRegisterForm
from core.models import Customer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def login_page(request):
    return render(request, 'accounts/login.html')


def user_register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['first_name'] + form.cleaned_data['last_name'] + str(random.randint(1, 100))
            username = username.lower()
            while Customer.objects.filter(username=username).exists():
                username = form.cleaned_data['first_name'] + form.cleaned_data['last_name'] + str(random.randint(1, 100))
            form.instance.username = username
            form.save()

            messages.success(request, 'You are now registered')


            html_content = render_to_string('accounts/email_confirmation.html')

            text_content = strip_tags(html_content)

            msg = EmailMultiAlternatives('You are now registered', text_content,
                                         'amulya.sharma@tothenew.com', [form.cleaned_data['email']])
            msg.attach_alternative(html_content, "text/html")
            msg.send()



            # send_mail(
            #     'You are now registered',
            #     'Thank you ' + form.cleaned_data['first_name'] + ' for registering with us.',
            #     'amulya.sharma@tothenew.com',
            #     [form.cleaned_data['email']],
            #     fail_silently=False
            # )
            return redirect('loginapp')
        else:
            errors = form.errors
            messages.error(request, 'Password not valid. It must contain at least 8 letters.')
            return redirect('registration')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html')




