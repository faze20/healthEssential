from django.urls import path, include

from  .views import (
    HomePageView,
    OurServicesPageView,
    OurProductsPageView,
    GalleryPageView,
    ContactUsListView,
    ThankYouPageView,
    ManagerCreateView,
    ManagerUpdateView,
    ManagerDeleteView,
    ManagerDetailView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ourservices/', OurServicesPageView.as_view(), name='ourservices'),
    path('ourproducts/', OurProductsPageView.as_view(), name='ourproducts'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('contactus/', ContactUsListView.as_view(), name='contact'),  
    path('thankyou/', ThankYouPageView.as_view(), name='thankyou'), 
    path('manager/', ManagerCreateView.as_view(), name='manager'),  
    path('<int:pk>/edit/', ManagerUpdateView.as_view(), name='manager_edit'),
    path('<int:pk>/delete/', ManagerDeleteView.as_view(), name='manager_delete'),
    path('<int:pk>/', ManagerDetailView.as_view(), name='manager_detail'),

 

]