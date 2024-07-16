from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    PasswordChangeView, PasswordResetView, PasswordResetConfirmView
)
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, redirect

from users.forms import CreationForm, ChangeForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:index')
    template_name = 'users/signup.html'


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'


class PasswordReset(PasswordResetView):
    success_url = reverse_lazy('users:password_reset_done')
    template_name = 'users/password_reset_form.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')
    template_name = 'users/password_reset_confirm.html'


class ListUserView(View):
    def get(self, request):
        users = User.objects.select_related().filter(is_staff=False)
        context = {
            'users': users
        }
        return render(request, 'users/index.html', context)
    

class UserView(View):
    template_name='users/detail.html'

    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        form = ChangeForm(
            instance=user,
        )
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user = get_object_or_404(User, id=request.user.id)
        form = ChangeForm(
            request.POST,
            instance=user,
        )
        if form.is_valid():
            form.save()
            return redirect('users:index')
       
        
def delete(request):
    user = get_object_or_404(User, id=request.user.id)
    user.delete()
    return redirect('users:index')
