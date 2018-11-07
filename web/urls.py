from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('',views.Index,name='index'),
    path('markdowntest/',views.MarkDownTest,name='markdowntest'),
    path('articletest/',views.ArticleTest,name='articletest'),
    path('login',views.Login,name='login'),
    path('logincheck/',views.LoginCheck,name='logincheck'),
    path('sign', views.Sign, name='sign'),
    path('signcheck/', views.SignCheck, name='signcheck'),

    # banbenkongzhi
    path('svnindex/', views.SVNIndex, name='svnindex'),
    # blogsystem
    path('djangoblogindex/', views.DjangoBlogIndex, name='djangoblogindex'),
    path('djangoblogshow/', views.DjangoBlogShow, name='djangoblogshow'),
]