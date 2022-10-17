from imakesproject1 import settings
from . import views
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
    # path('inner-page/', views.innerpage, name='inner-page'),
    # path('contact/', views.contact, name='contact')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)