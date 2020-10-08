from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *

try:
    from ..blog.models import Profile
except (ValueError, ImportError):
    from blog.models import Profile


class UserRegistration(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditLoginSettings(UpdateView):
    form_class = EditLoginSettingsForm
    template_name = 'registration/edit_login_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    # form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserProfile(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfile, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class EditUserProfile(UpdateView):
    model = Profile
    template_name = 'registration/edit_user_profile.html'
    fields = ['bio', 'profile_pic', 'instagram_url']
    success_url = reverse_lazy('home')


class CreateUserProfile(CreateView):
    model = Profile
    form_class = CreateUserProfileForm
    template_name = 'registration/create_user_profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

