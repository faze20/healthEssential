from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import ContactUs, Manager


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class OurServicesPageView(TemplateView):
    template_name = 'ourservices.html'

class OurProductsPageView(TemplateView):
    template_name = 'ourproducts.html'


class GalleryPageView(TemplateView):
    template_name = 'gallery.html'


class ContactUsListView(CreateView):
    model = ContactUs
    template_name = 'contact.html'
    fields = ['name','email','phone','query', 'message',]
    success_url = reverse_lazy('thankyou')

class ThankYouPageView(TemplateView):
    model = ContactUs
    template_name = 'thankyoupage.html'


'''class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html' '''


class ManagerListView(CreateView):
    model = Manager
    template_name = 'manager.html'
    fields = ['author','name','price','description', 'product_image','service_image']
    success_url = reverse_lazy('update')


class ManagerUpdateView(TemplateView):
    model = Manager
    template_name = 'update.html'