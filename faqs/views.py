from django.shortcuts import render

from .models import Faq

def all_faqs(request):
    """
    View to return all FAQs
    """

    faqs = Faq.objects.all()
    context = {
        'faqs': faqs,
    }

    return render(request, 'faqs/faqs.html', context)
