from django.urls import path
from . import views
from .views import *
# PostList, PostText, PostAdd, PostUpdate, PostDelete, CategoryAdd

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('', views.main, name='main'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('crypto/', views.crypto, name='crypto'),
    path('crypto_all/', views.crypto_all, name='crypto_all'),

    path('post_list/', PostList.as_view(), name='post_list'),
    path('post_text/<int:pk>/', PostText.as_view(), name='post_text'),
    path('post_add/', PostAdd.as_view(), name='post_add'),
    path('post_text/edit/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('post_text/<int:pk>/remove/', PostDelete.as_view(), name='post_delete'),
    path('category_add/', CategoryAdd.as_view(), name='category_add'),

    # path('post_list/', views.post_list, name='post_list'),
    # path('post_text/<int:pk>/', views.post_text, name='post_text'),
]
