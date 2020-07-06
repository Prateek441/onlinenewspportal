from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_dash1', views.admin_dash1, name='admin_dash1'),
    path('admin_dash2', views.admin_dash2, name='admin_dash2'),
    path('all_users', views.all_users, name='all_users'),
    path('add_user', views.add_user, name='add_user'),
    path('all_channels', views.all_channels, name='all_channels'),
    path('all_posts', views.all_posts, name='all_posts'),
    path('ad_add_post', views.ad_add_post, name='ad_add_post'),
    path('ad_add_newsch', views.ad_add_newsch, name='ad_add_newsch'),
    path('choice_dash', views.choice_dash, name='choice_dash'),
    path('ad_slider', views.ad_slider, name='ad_slider'),
    path('ad_media', views.ad_media, name='ad_media'),
    path('wel_msg', views.wel_msg, name='wel_msg'),
    path('ad_profile', views.ad_profile, name='ad_profile'),
    path('edit_adpro/<int:id>/', views.edit_adpro, name='edit_adpro'),
    path('ad_logout', views.ad_logout, name='ad_logout'),
    path('delete_user/<int:id>/', views.delete_user, name='del_user'),
    path('delete_ch/<int:id>/', views.delete_ch, name='del_ch'),
    path('delete/<int:id>/', views.delete_slider, name='del_slider'),
    path('del_media/<int:id>/', views.del_media, name='del_media'),
    path('edit/<int:id>/', views.edit_slider, name='edit_slider'),
    path('ad_edit_post/<int:id>/', views.ad_edit_post, name='ad_edit_post'),
    path('ad_del_post/<int:id>/', views.ad_del_post, name='ad_del_post'),
    path('edit_user/<int:id>/', views.edit_user, name='edit_user'),
    path('edit_wel_msg/<int:id>/', views.edit_wel_msg, name='edit_wel_msg'),
    path('edit_ch/<int:id>/', views.edit_ch, name='edit_ch'),
    path('edit_media/<int:id>/', views.edit_media, name='edit_media'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)