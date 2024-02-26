from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import NewsletterForm
from profiles.models import UserProfile


def newsletter(request):
    """ Sign up to newsletter """

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            form_email = form.cleaned_data['email']
            print(form_email)
            messages.success(request, f'Successfully subscribed! \
            A confirmation email has been sent to {form_email}')
            send_mail(
                "Newsletter signup confirmation",
                render_to_string('newsletter/emails/confirmation.txt'),
                settings.DEFAULT_FROM_EMAIL,
                [form_email],
                fail_silently=False,
            )
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to subscribe. \
            Please ensure the form is valid.')

    else:
        # Attempt to prefill the form with info from user profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                newsletter_form = NewsletterForm(initial={
                    'name': profile.default_full_name,
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
