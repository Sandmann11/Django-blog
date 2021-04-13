from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # path('home/', views.homepage, name='main'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_text/<int:pk>/', views.post_text, name='post_text'),
    path('admin/', views.admin, name='admin')
]
