from django.urls import path
from info_app import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'info_app'

urlpatterns = [
    path('about/',views.view_about.as_view(),name='about'),
    path('signup/',views.view_signup.as_view(),name='signup'),
    path('cars/',views.view_carslist.as_view(),name='carlist'),
    path('cars/<int:pk>/',views.view_cardetails.as_view(),name='cardetails'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
