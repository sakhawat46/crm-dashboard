from django.views.generic import TemplateView, ListView
from web_project import TemplateLayout
from django.contrib.auth import get_user_model
from apps.authentication.models import Avater
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.views.generic import View
from django.urls import reverse
from django.contrib import messages

User = get_user_model()


class UserView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

class UserListView(ListView):
    model = User
    template_name = 'user_list_basic.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Initialize your TemplateLayout if needed
        context = TemplateLayout.init(self, context)

        # Add additional pagination context
        if context.get('page_obj'):
            context['users'] = context['page_obj']
        return context


class UserCreateView(UserView):
    template_name = 'user_create_basic.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        avatar = request.FILES.get('avatar')
        try:
            user = User.objects.create_user(email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.username =username
            user.user_type = user_type
            user.save()
            if avatar and user:
                Avater.objects.create(user=user, avatar=avatar)
            return redirect(reverse('user_create_success', kwargs={'pk': user.pk}))
        except Exception as error:
            context = self.get_context_data()
            context["error"] = error
            return self.render_to_response(context)

class UserCreateSuccessView(UserView):
    template_name = 'user_create_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        context['created_user'] = user
        return context



class UserUpdateView(UserView):
    template_name = 'user_update_basic.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        context = self.get_context_data()
        context['user'] = user
        try:
            context['avatar'] = user.avater
        except:
            context['avatar'] = None
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        avatar = request.FILES.get('avatar')

        try:
            user.email = email
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.user_type = user_type

            if password:  # Only update password if a new one was provided
                user.set_password(password)

            user.save()

            if avatar:
                # Delete old avatar if exists
                Avater.objects.filter(user=user).delete()
                # Create new avatar
                Avater.objects.create(user=user, avatar=avatar)

            return redirect(reverse('user-list'))
        except Exception as error:
            context = self.get_context_data()
            context["error"] = error
            context['user'] = user
            return self.render_to_response(context)



class UserDeleteView(UserView):
    template_name = 'user_confirm_delete.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        user = self.get_object()
        context['user'] = user
        context["object"] = user

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        try:
            username = user.username
            user.delete()
            messages.success(request, f'User "{username}" was deleted successfully.')
            return redirect(reverse('user-list'))
        except Exception as error:
            messages.error(request, f'Error deleting user: {error}')
            return redirect(reverse('user-list'))
