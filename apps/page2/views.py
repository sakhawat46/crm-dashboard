
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import AboutUs,ContactUs
from .forms import AboutUsForm,ContactUsForm
from django.views.generic import UpdateView, ListView
from django.views.generic.edit import CreateView, DeleteView
from web_project import TemplateLayout
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages
from django.views.generic.detail import DetailView
class BaseUpdateView(UpdateView):
    template_name = 'edit.html'
    def get_success_url(self):
        return self.request.path_info

    def form_valid(self, form):
        messages.success(self.request, f"{ self.get_object(self) } Update successful.")
        return super().form_valid(form)

    URL_MAPPING = {
        'settings_dashboard': reverse_lazy('settings_dashboard'),
        'header_footer_dashboard': reverse_lazy('header_footer_dashboard'),
        'seo': reverse_lazy('seo'),
    }


    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

    def get_object(self, queryset=None):
        obj, created = self.model.objects.get_or_create(pk=1)
class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello! This is the home page.")

class PagesView(TemplateView):
    template_name = 'pages_misc_under_maintenance.html'
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context
    

class CustomAdminAboutUsView(PagesView):
    template_name = 'about_us_edit.html'

    def get(self, request):
        about_us, _ = AboutUs.objects.get_or_create(pk=1)
        form = AboutUsForm(instance=about_us)
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request):
        about_us, _ = AboutUs.objects.get_or_create(pk=1)
        form = AboutUsForm(request.POST, instance=about_us)
        context = self.get_context_data()
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('custom_admin_about_us')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

    
   
    
class AboutUsPageView(PagesView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()
        return context


from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service
from .forms import ServiceForm

class ServiceEditView(BaseUpdateView):

    form_class=ServiceForm
    model=Service



class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'  # Replace with your actual template
    context_object_name = 'service'  

from django.views.generic import TemplateView
from .models import Service

class ServicesPageView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class ContactUsEdit(BaseUpdateView):

    form_class=ContactUsForm
    model=ContactUs

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()  # Get the instance to update
    #     form = self.form_class(request.POST, instance=self.object)

    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         # Optionally modify the instance here
    #         # instance.modified_by = request.user
    #         instance.save()
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class CustomAdminContactUsView(PagesView):
    template_name = 'contact_us_edit.html'

    def get(self, request):
        contact_us, _ = ContactUs.objects.get_or_create(pk=1)
        form = ContactUsForm(instance=contact_us)
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request):
        contact_us, _ = ContactUs.objects.get_or_create(pk=1)
        form = ContactUsForm(request.POST, instance=contact_us)
        context = self.get_context_data()
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('custom_admin_about_us')
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context


from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import ContactUs
from .forms import ContactForm

class ContactPageView(TemplateView):
    template_name = 'contact_page.html'

    def get(self, request, *args, **kwargs):
        self.contact_info, _ = ContactUs.objects.get_or_create(pk=1)
        self.form = ContactForm()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.contact_info, _ = ContactUs.objects.get_or_create(pk=1)
        self.form = ContactForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return redirect('contact_page')  # Change to your url name
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['contact_info'] = self.contact_info
        context['form'] = self.form
        return context
