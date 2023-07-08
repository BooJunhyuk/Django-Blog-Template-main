from django.db import models
from django.contrib.auth import get_user_model # 추가
# from django.contrib.auth.models import AbstractUser # user 커스텀하면 필요?




class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

User = get_user_model() # 사용자 모델 장고에서 만들어줌 -> 


# user 커스텀 방법도 있는데 일단 확장으로 진행?
'''class UserInfo(models.Model):
    mbti = models.CharField(verbose_name='MBTI',max_length=5)
    user = models.ForeignKey(to='User',on_delete=models.CASCADE)
   ''' 
 
        
# 커뮤니티 게시판 
class Post(models.Model):
    # 게시판: 제목, 내용, 작성일, 조회수, 작성자 ForeignKey, 그리고 뭐가 더 필요할까?
    
    # image = models.ImageField(verbose_name='이미지',null=True, blank=True) # 게시글 이미지 저장 필드  -- 이미지는 일단 보류
    
    headline = models.CharField(verbose_name='제목',max_length=200) # 제목
    content = models.TextField(verbose_name='내용') # 게시글 내용 저장 필드 
    created_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True) # 작성 시간
    view_count = models.IntegerField(verbose_name='조회수',default=0)  # 조회수   
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE, null=True, blank=True) # 작성자
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)    
    def __str__(self):
        return self.headline
    # post의 이름을 post 제목으로 바꾸기 위해 변경
    

# 댓글 모델
class Comment(models.Model): # 일대다 구조
    
    # 댓글 : 댓글 내용, 작성일, 게시물 ForeignKey, 작성자 ForeignKey 
    
    content = models.TextField(verbose_name='내용')
    created_at =models.DateTimeField(verbose_name='작성일')
    post = models.ForeignKey(to = 'Post',on_delete=models.CASCADE)# CASCADE -> Post삭제되면 comment도 같이 삭제
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True) # 사용자랑 연결 ,사용자모델은 장고에서 만들어줌-> User = get_user_model() 
    is_secret = models.BooleanField(verbose_name='비밀글',default=False) # 비밀글인지
    is_anonymous = models.BooleanField(verbose_name='익명글',default=False) # 익명글인지
    def __str__(self):
        return self.content
    #comment의 이름을 comment 내용으로 바꾸기 위해 변경


class Refly(models.Model): # 일대다 구조
    
    # 댓글 : 댓글 내용, 작성일, 게시물 ForeignKey, 작성자 ForeignKey 
    
    content = models.TextField(verbose_name='내용')
    created_at =models.DateTimeField(verbose_name='작성일')
    post = models.ForeignKey(to = 'Post',on_delete=models.CASCADE)# CASCADE -> Post삭제되면 comment도 같이 삭제
    comment = models.ForeignKey(to = 'Comment',on_delete=models.CASCADE)# CASCADE -> Post삭제되면 comment도 같이 삭제
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True) # 사용자랑 연결 ,사용자모델은 장고에서 만들어줌-> User = get_user_model() 
    def __str__(self):
        return self.content
    #comment의 이름을 comment 내용으로 바꾸기 위해 변경

'''
모델 추가 및 수정 후 migration 필요

python manage.py makemigrations 실행
0002_post_comment.py 파일 생성됨
ex) ->  Migrations for 'blogapp':
            blogapp\migrations\0002_post_comment.py 
                - Create model Post
                - Create model Comment
그리고 
python manage.py migrate 실행
ex) ->  Operations to perform:
            Apply all migrations: admin, auth, blogapp, contenttypes, sessions
        Running migrations:
            Applying blogapp.0002_post_comment... OK

sqlite 설치해서 확인해보면 데이터 확인 가능
'''
