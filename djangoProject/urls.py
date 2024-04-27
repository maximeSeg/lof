from django.contrib import admin
from django.urls import path
from djangoProject.views import *
from . import views

urlpatterns = [
    path('', accueil, name='accueil'),
    path('admin/', admin.site.urls),
    path('a-propos/', a_propos, name='a_propos'),
    path('contact/', contact, name='contact'),
    path('accueil/', views.accueil, name='accueil'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('un-v-un/', views.un_v_un, name='1v1'),
    path('creer-une-equipe/', views.creer_une_equipe, name='creer_une_equipe'),
    path('mon-compte/', views.mon_compte, name='mon_compte'),
    path('connection/', views.page_connection, name='page_connection'),
    path('inscription/', views.page_inscription, name='page_inscription'),
    path('creer-user/', views.creer_user_form, name='creer_user'),
]
