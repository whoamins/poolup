from django.urls import path
from pools.views import IndexView, VoteView, DetailView, ResultsView


app_name = 'pools'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:question_id>/', DetailView.as_view(), name='detail'),
    path('<int:question_id>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', VoteView.as_view(), name='vote')
]
