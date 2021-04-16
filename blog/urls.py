from django.urls import path
from . import views
from .views import PostList, PostText, PostAdd

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('', views.main, name='main'),
    path('portfolio/', views.portfolio, name='portfolio'),
    # path('post_list/', views.post_list, name='post_list'),
    # path('post_text/<int:pk>/', views.post_text, name='post_text'),

    path('post_list/', PostList.as_view(), name='post_list'),
    path('post_text/<int:pk>/', PostText.as_view(), name='post_text'),
    path('post_add/', PostAdd.as_view(), name='post_add'),
            
    path('crypto/', views.crypto, name='crypto'),
]
