from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('channels',views.channels, name='channels'),
    path('contact',views.contact, name='contact'),
    path('portal/<int:id>/',views.portal, name='portal'),
    path('details/<int:id>/',views.details, name='details'),
    path('state_news/<int:id>/',views.state_news, name='state_news'),
    path('cate_news/<int:id>/',views.cate_news, name='cate_news'),





]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)