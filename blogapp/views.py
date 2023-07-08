from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone



from .models import Post,Comment
User = get_user_model()


def home(request):
    return render(request, 'index.html')

@login_required
def new(request):
    if request.method=='GET':
        return render(request, 'new.html')
    else:        
        title = request.POST.get('title')
        body = request.POST.get('body')
        writer = request.user
        Post.objects.create(
            headline = title,
            content = body,
            writer = writer,
        )
        return HttpResponseRedirect('/community')


def community(request):
    post_list = Post.objects.all()
    context = {"post_list":post_list}
    return render(request,'community.html',context)


@login_required
def mbtitest(request):
    if request.method=='POST':
        first = request.POST.get('first_question')
        second = request.POST.get('second_question')
        third = request.POST.get('third_question')
        fourth = request.POST.get('fourth_question')
        result=first+second+third+fourth
        print(result)
        request.user.mbti = result
        request.user.save()


        return HttpResponseRedirect('/')
    else:
        return render(request,'mbtitest.html')
#리다이렉션이란 웹 브라우저에서 요청한 url을 다른 url로 변경하여 새로운 페이지로 이동시키는 기능
# 웹 애플리케이션에서 리다이렉션을 사용하는 경우
# 1. 사용자가 요청한 페이지를 삭제한 경우
# 2. 사용자가 요청한 페이지의 URL이 변경된 경우
# 3. 사용자가 로그인 또는 로그아웃 등의 작업을 수행한 후, 
#    이전 페이지로 다시 이동시키기 위한 경우

# HttpResponseRedirect를 사용할 때, 인자로 전달하는 URL은 반드시 절대 경로여야 한다.
# 따라서, 'communty' 대신 '/communty'로 변경하여야
# 원하는 URL로 리다이렉션이 가능하다.

@login_required
def detail(request,post_id):
        post = get_object_or_404(Post, pk = post_id)
        if request.method=='GET':
            context = {"post":post,}
            return render(request,"detail.html",context)
        else:
            comment_text = request.POST.get('comment_text')


            is_secret=False
            secret_value = request.POST.get('secret')
            if secret_value:
                is_secret = secret_value == 'on'

            is_anonymous =False
            anonymous_value = request.POST.get('anonymous')
            if anonymous_value:
                is_anonymous = anonymous_value == 'on'

            created_at = timezone.now()
            Comment.objects.create(
            content = comment_text,
            writer = request.user,
            created_at = created_at,
            post = post,
            is_secret = is_secret,
            is_anonymous = is_anonymous
            )
            return HttpResponseRedirect(reverse("detail", args=(post_id,)))


@login_required
def edit(request,post_id):
    #post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, pk = post_id)
    if request.user != post.writer:
        return Http404('잘못된 접근입니다.')
    if request.method=='POST':
        headline = request.POST.get('headline')
        content = request.POST.get('content')
        post.content=content
        post.headline=headline
        post.save()
        return HttpResponseRedirect(reverse("detail", args=(post_id,)))
    else:    
        context = {'post':post,}
        return render(request,'edit.html',context)

@login_required    
def delete(request,post_id):
    post = get_object_or_404(Post, pk = post_id)
    if request.user != post.writer:
        return Http404('잘못된 접근입니다.')
    if request.method=='POST':
        post.delete()
        return HttpResponseRedirect('/community')
    else:    
        return render(request,'community.html')
    

@login_required
def edit_comment(request,comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    if request.user != comment.writer:
        return Http404('잘못된 접근입니다.')
    if request.method=='POST':  
        content =request.POST.get('edited_comment')  
        comment.content = content
        comment.save()
        return HttpResponseRedirect(reverse("detail", args=(comment.post.id,)))
    else:    
        post = get_object_or_404(Post,pk=comment.post.id)
        context = {'post':post,}
        return render(request,'detail.html',context)

@login_required    
def delete_comment(request,comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    if request.user != comment.writer:
        return Http404('잘못된 접근입니다.')
    if request.method=='POST':        
        comment.delete()
        return HttpResponseRedirect(reverse("detail", args=(comment.post.id,)))
    else:    
        post = get_object_or_404(Post,pk=comment.post.id)
        context = {'post':post,}
        return render(request,'detail.html',context)




