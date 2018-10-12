from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('skills/', views.skills_index, name='skills_index'),
    path('skills/create', views.SkillCreate.as_view(), name='skill_create'),
    path('skills/<int:skill_id>', views.skill_detail, name='skill_detail'),

    
]