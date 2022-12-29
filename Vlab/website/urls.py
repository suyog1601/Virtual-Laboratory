from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name = 'home'),
    path('plot',views.plot, name= 'plot'),
    path('courses',views.course,name='course'),
    path('DOM',views.DOM,name='DOM'),
    path('experiment',views.experiment,name='experiment'),
    path('DOMEXP1',views.DOMEXP1,name='DOMEXP1'),
    path('DOMEXP2',views.DOMEXP2,name='DOMEXP2'),
    path('DOMEXP3',views.DOMEXP3,name='DOMEXP3'),
    path('DOMEXP4',views.DOMEXP4,name='DOMEXP4'),
    path('DOMEXP5',views.DOMEXP5,name='DOMEXP5'),
    path('DOMEXP6',views.DOMEXP6,name='DOMEXP6'),
    path('DOMEXP7',views.DOMEXP7,name='DOMEXP7'),
    path('DOMEXP8',views.DOMEXP8,name='DOMEXP8'),
    path('DOMEXP9',views.DOMEXP9,name='DOMEXP9'),
    path('DOMEXP10',views.DOMEXP10,name='DOMEXP10'),
    path('DOMEXP11',views.DOMEXP11,name='DOMEXP11'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout, name = 'logout'),
    path('postlink',views.post_link, name='postlink')

]