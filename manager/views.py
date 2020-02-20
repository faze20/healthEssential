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


class GalleryPageView(ListView):
    model = Manager
    template_name = 'gallery.html'


class ContactUsListView(CreateView):
    model = ContactUs
    template_name = 'contact.html'
    fields = ['name','email','phone','query', 'message',]
    success_url = reverse_lazy('thankyou')

class ThankYouPageView(TemplateView):
    model = ContactUs
    template_name = 'thankyoupage.html'



class ManagerCreateView(CreateView):
    model = Manager
    template_name = 'manager.html'
    fields = ['author','name','price','description', 'product_photo']
    success_url = reverse_lazy('gallery')


class ManagerUpdateView(UpdateView):
    model = Manager
    fields = ('name', 'price','product_photo','description',)
    template_name = 'update.html'

class ManagerDeleteView(DeleteView):
    model = Manager
    template_name  = 'manager_delete.html'
    success_url = reverse_lazy('gallery')

class ManagerDetailView(DetailView):
    model = Manager
    template_name = 'manager_detail.html'

