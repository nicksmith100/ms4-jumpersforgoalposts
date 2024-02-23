from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import NewsletterForm
from profiles.models import UserProfile

def newsletter(request):
    """ Sign up to newsletter """
    
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully subscribed!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to subscribe. Please ensure the form is valid.')
    
    else:
        # Attempt to prefill the form with info from user profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                newsletter_form = NewsletterForm(initial={
                    'name': profile.user.get_full_name(),
                    'email': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                newsletter_form = NewsletterForm()
        else:
            newsletter_form = NewsletterForm()
    
        form = newsletter_form
    
    template = 'newsletter/newsletter.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
