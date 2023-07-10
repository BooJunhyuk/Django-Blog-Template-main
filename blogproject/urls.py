from django.contrib import admin
from django.urls import path, include, re_path
from blogapp import views
from django.contrib.auth import views as auth_views


from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title = "Swagger 타이틀 작성",
        default_version = "v1",
        description = "Swagger를 사용한 API 문서입니다",
    ),
    public=True,
    permission_classes=(AllowAny,),
)






urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('new/', views.new, name = 'new'),
    path('community/', views.community, name = 'community'),
    path('mbtitest/', views.mbtitest, name = 'mbtitest'),
    path('detail/<int:post_id>', views.detail, name = 'detail'),
    path('edit/<int:post_id>', views.edit, name = 'edit'),
    path('delete/<int:post_id>', views.delete, name = 'delete'),
    path('edit_comment/<int:comment_id>', views.edit_comment, name = 'edit_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name = 'delete_comment'),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('accounts/', include('allauth.urls')),
   #path('main/', include('your_app.urls', namespace='your_app')),
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]