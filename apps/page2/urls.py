# from django.urls import path
# from . import views  # or import your actual views

# urlpatterns = [
#     path('', views.home, name='home'),  # Example
#     path('about-us/', views.about_us_page, name='about_us_page'),
#     path('admin-dashboard/about-us/', views.custom_admin_about_us, name='custom_admin_about_us'),
# ]

from django.urls import path
from .views import HomeView, CustomAdminAboutUsView, AboutUsPageView, PagesView,ServiceEditView,ServicesPageView,ContactUsEdit,ServiceDetailView,CustomAdminContactUsView,ContactPageView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin-dashboard/about-us/', CustomAdminAboutUsView.as_view(), name='custom_admin_about_us'),
    path('about-us/', AboutUsPageView.as_view(), name='about_us_page'),
    path('apage/', PagesView.as_view(), name='about_us_page'),
    path('services/', ServicesPageView.as_view(), name='services_page'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('admin-dashboard/services/', ServiceEditView.as_view(), name='service_edit'),
    path('admin-dashboard/contact-us/', ContactUsEdit.as_view(), name='contact_edit'),
    path('admin-dashboard/contact-uss/', CustomAdminContactUsView.as_view(), name='contact_us'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
]
