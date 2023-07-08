from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "아이디/비밀번호를 다시 확인해주세요.",
        "inactive": "권한이 없는 접근입니다.",
    }
class UserBaseForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields = '__all__'

class UserCreateForm(UserBaseForm):
    password2=forms.CharField(widget=forms.PasswordInput())
    error_messages = {
        "invalid_login": "아이디/비밀번호를 다시 확인해주세요.",
        "inactive": "권한이 없는 접근입니다.",
    }
    class Meta(UserBaseForm.Meta):
        fields =['username','email','password']

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username','email']
