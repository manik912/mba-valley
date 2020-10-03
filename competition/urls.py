from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import competitionDetailView, CompetitionListView, submit, competitionRegister, competitionCreateView, awardregister, award_delete

urlpatterns = [
    path('competition/<int:pk>/detail/',            views.competitionDetailView,        name='competition-detail'),
    path('competition/<int:pk>/submit/',            views.submit,        name='submit'),
    path('competition/',                   views.CompetitionListView,                  name='competition'),
    path('competition/create/' , 			            competitionCreateView, 			name='competition-create'),
    # path('submit/',                        views.submit,                       name='submit')
    path('competition/<int:pk>/register/',   views.competitionRegister,      name='competition-register'),
    path('competition/<int:pk>/awards/',   views.awardregister,      name='award_register'),
    path('award-delete/<int:pk>/<int:a>/',   views.award_delete,      name='award_delete'),
]