from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("",views.index,name='home'),

    path("t20_ranking",views.t20_ranking,name='t20_ranking'),
    path("oneday_ranking",views.oneday_ranking,name='oneday_ranking'),
    path("test_ranking",views.test_ranking,name='test_ranking'),
    path("ipl_ranking",views.ipl_ranking,name='ipl_ranking'),

    path("t20_ranking_batsman1",views.t20_ranking_batsman1,name='t20_ranking_batsman1'),
    path("t20_ranking_bowler1",views.t20_ranking_bowler1,name='t20_ranking_bowler1'),

    path("oneday_ranking_batsman2",views.oneday_ranking_batsman2,name='oneday_ranking_batsman2'),
    path("oneday_ranking_bowler2",views.oneday_ranking_bowler2,name='oneday_ranking_bowler2'),

    path("test_ranking_batsman3",views.test_ranking_batsman3,name='test_ranking_batsman3'),
    path("test_ranking_bowler3",views.test_ranking_bowler3,name='test_ranking_bowler3'),

    path("ipl_ranking_batsman4",views.ipl_ranking_batsman4,name='ipl_ranking_batsman4'),
    path("ipl_ranking_bowler4",views.ipl_ranking_bowler4,name='ipl_ranking_bowler4'),

    path('login',views.login,name='login'),
    path("contact",views.contact,name='contact'),
    path("players",views.players,name='players'),
    path('matches',views.matches,name='matches'),
    path('match',views.match,name='match'),
     
]