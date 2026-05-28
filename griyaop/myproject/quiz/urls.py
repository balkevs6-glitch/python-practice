from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz_page, name='quiz'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('player_name/', views.student_id, name='student_id'),
    path('easy/', views.easy_level, name='easy'),
    path('medium/', views.medium_level, name='medium'),
    path('hard/', views.hard_level, name='hard'),
]



'''urlpatterns = [
    path('', views.home, name='home'),  # main menu

    path('player-name/', views.player_name, name='player_name'),
    path('difficulty/', views.select_difficulty, name='difficulty'),

    path('easy/', views.easy_level, name='easy'),
    path('medium/', views.medium_level, name='medium'),
    path('hard/', views.hard_level, name='hard'),

    path('result/', views.result, name='result'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]'''