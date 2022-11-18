from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.questions),
    path('create-question/', views.create_question),
    path('question/<int:pk>/', views.question_detail),
    path('question/<int:pk>/update', views.question_update),
    path('question/<int:pk>/delete', views.question_delete),
    path('choices/', views.choices),
    path('question/<int:pk>/choice/', views.create_choice),
    path('forums/', views.forums),
    path('create-forum/', views.create_forum),
    path('forum/<int:pk>/update/', views.update_forum),
    path('forum/<int:pk>/delete/', views.delete_forum),
    path('forum/<int:pk>/comments/', views.get_comments),
    path('forum/<int:pk>/create-comment/', views.create_comment),
    path('forum/<int:pk>/count-comments/', views.get_comments_count),
    path('forum/<int:pk>/votes/', views.forum_get_votes),
    path('forum/<int:pk>/post-vote/', views.post_vote),
    path('forum/<int:pk>/count-votes/', views.get_vote_counts),





]

