from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('ch_dash', views.ch_dash, name='ch_dash'),
    path('ch_login', views.ch_login, name='ch_login'),
    path('ch_logout', views.ch_logout, name='ch_logout'),
    path('ch_profile',views.ch_profile, name='ch_profile'),
    path('ch_dashboard',views.ch_dashboard, name='ch_dashboard'),
    path('ch_add_post',views.ch_add_post, name='ch_add_post'),
    path('ch_all_post',views.ch_all_post, name='ch_all_post'),
    path('ch_total_post',views.ch_total_post, name='ch_total_post'),
    path('ch_block_post',views.ch_block_post, name='ch_block_post'),
    path('delete/<int:id>/', views.delete_record, name='del_post'),
    path('edit/<int:id>/', views.edit_record, name='edit_post'),
    path('del_block_post/<int:id>/', views.del_block_post, name='del_block_post'),
    path('edit_block_post/<int:id>/', views.edit_block_post, name='edit_block_post'),
    path('del_post_t/<int:id>/', views.del_post_t, name='del_post_t'),
    path('edit_post_t/<int:id>/', views.edit_post_t, name='edit_post_t'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)