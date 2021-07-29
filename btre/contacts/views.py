from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contacts
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email= request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(listing_id = listing_id, user_id = user_id)

            if has_contacted:
                messages.error(request, 'You already made an inquery for this listing')

        else:
            contact = Contacts(listing = listing, listing_id = listing_id, name = name, email = email, message = message, user_id = user_id, realtor_email = realtor_email)
            contact.save()
            messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')

            send_mail(
            'Property Listing Inqiury',
            'There has been an inquiry for' + listing + '. Sign into admin panel for more info',
            'maryrahhh@gmail.com',
            [realtor_email, 'maryam_rahdaran@yahoo.com'],
            fail_silently=False
             )


        return redirect('/listings/'+listing_id)


