from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .forms import UserCreateForm, SignUpForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method=='GET':
        #form = UserCreateForm
        form = SignUpForm
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #form.cleaned_data.get 함수는 폼의 입력값을 개별적으로 얻고 싶은 경우에 사용하는 함수로
            #여기서는 인증시 사용할 사용자명과 비밀번호를 얻기 위해 사용했다.
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)  
            # authenticate : 사용자 인증 담당
            # login(request,user) 
            # 자동 로그인 기능
            return redirect('accounts:login')
        else:
            messages.add_message(request, messages.WARNING, form.error_messages)
            print("error_message : "+str(form.error_messages))
            return render(request,'accounts/signup.html',{'form':form})
        
        
def user_login(request):
    if request.method =='GET':
        return render(request,'accounts/login.html',{'form':LoginForm()})
    else:
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            login(request,form.user_cache)
            if form.user_cache.mbti:
                return redirect('home')
            print(form.user_cache.mbti)
            return redirect('mbtitest')
            
        else:
            messages.add_message(request, messages.WARNING,form.error_messages)
            return render(request, 'accounts/login.html',{'form':form})
        

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')
       