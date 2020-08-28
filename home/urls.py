from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostDetailView, SearchView


urlpatterns = [
    path('',			views.home,		name='home'),
    path('blogs/<int:pk>/', 		PostDetailView.as_view(), 	name='post-detail'),
    path('results/', views.SearchView, name='search'),
]
if settings.DEBUG: 
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )