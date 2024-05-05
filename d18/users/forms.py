from django.contrib.auth.forms import AuthenticationForm, forms, UserCreationForm, UserChangeForm
from .models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'pessword']

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholer': 'Ввндите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholer': 'Ввндите фамилию'}))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholer': 'Ввндите email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholer': 'Ввндите пароль'}))
    # password2 = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control py-4',
    #     'placeholer': 'Повторите пароль'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholer': 'Введите имя пользователя'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', }))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', }))
    image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', }))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'image', 'username')
