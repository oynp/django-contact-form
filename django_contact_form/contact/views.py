from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ContactView(TemplateView):
    template_name='contact.html'

    def get(self, request):
        return render(request, self.template_name, {})
