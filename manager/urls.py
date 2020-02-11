from django.urls import path, include

from  .views import ( HomePageView,OurServicesPageView,
OurProductsPageView,GalleryPageView, ContactUsListView,ThankYouPageView,ManagerListView, ManagerUpdateView)




urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ourservices/', OurServicesPageView.as_view(), name='ourservices'),
    path('ourproducts/', OurProductsPageView.as_view(), name='ourproducts'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('contactus/', ContactUsListView.as_view(), name='contact'),  
    path('thankyou/', ThankYouPageView.as_view(), name='thankyou'), 
    path('manager/', ManagerListView.as_view(), name='manager'),  
    path('update/',  ManagerUpdateView.as_view(), name='update'),  

]