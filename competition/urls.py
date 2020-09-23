from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import competitionDetailView, CompetitionListView, submit, competitionRegister

urlpatterns = [
    path('competition/<int:pk>/detail/',            views.competitionDetailView,        name='competition-detail'),
    path('competition/<int:pk>/submit/',            views.submit,        name='submit'),
    path('competition/',                   views.CompetitionListView,                  name='competition'),
    # path('submit/',                        views.submit,                       name='submit')
    path('competition/<int:pk>/register/',   views.competitionRegister,      name='competition-register'),
]