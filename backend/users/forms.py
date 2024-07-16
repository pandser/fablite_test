from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


User = get_user_model()


class CreationForm(UserCreationForm):
    '''
        Форма для регистрации пользователя.
    '''

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ChangeForm(UserChangeForm):
    '''
        Форма для редактирования пользователя.
    '''

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
