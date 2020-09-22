from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import competitionDetailView, CompetitionListView, submit

urlpatterns = [
    path('competition-detail/',            views.competitionDetailView,        name='competition-detail'),
    path('competition/',                   views.competition,                  name='competition'),
    path('submit/',                        views.submit,                       name='submit')
]