from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login, name="Login"),
    path('about.html/', views.about, name="about"),
    path('services.html/', views.services, name="about"),
    path('contact.html/', views.contact, name="contact"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
