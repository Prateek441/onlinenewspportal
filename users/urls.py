from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.sign_up, name='u_signup'),
    path('login/',views.login, name='u_login'),
    path('',views.dashboard, name='dashboard'),
    path('logout',views.logout, name='logout'),
    path('edit/<int:id>/', views.upro_edit, name='edit_upro'),
]
