from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostDetailView, SearchView


urlpatterns = [
    path('',			            views.home,		                    name='home'),
    path('blogs/<int:pk>/', 		views.PostDetailView, 	        name='post-detail'),
    path('results/',                views.SearchView,                   name='search'),
    path('lateststories/',			views.latest_story,		                    name='latest-stories'),
    path('startupstories/',			views.startup_story,		                    name='startup-stories'),
    path('mbastories/',			views.mba_story,		                    name='mba-stories'),
]
if settings.DEBUG: 
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )