from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostDetailView, SearchView, competitionDetailView


urlpatterns = [
    path('',			            views.home,		                    name='home'),
    path('blogs/<int:pk>/', 		views.PostDetailView, 	        name='post-detail'),
    path('results/',                views.SearchView,                   name='search'),
    path('competition/',            views.competitionDetailView,        name='competition-detail')
]
if settings.DEBUG: 
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )