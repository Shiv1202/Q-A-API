from django.urls import path
from .views import (
    CompanyView, OneCompanyView,
    TagView, OneTagView,
    TopicView, OneTopicView,
    SubTopicView, OneSubTopicView,
    QuestionPostView,
    AnswerPostView,
    AnswerCommentPostView,
    QuestionLikePostView, AnswerLikePostView,
    OneQuestionView,
)

urlpatterns = [
    path('comapanies/', CompanyView.as_view(), name = "comapanies"),
    path('company/<int:pk>/', OneCompanyView.as_view(), name = "single_company"),
    path('tags/', TagView.as_view(), name = "tags"),
    path('tag/<int:pk>/', OneTagView.as_view(), name = "Single_tag"),
    path('topics/', TopicView.as_view(), name = "topics"),
    path('topic/<int:pk>/', OneTopicView.as_view(), name = "single_topic"),
    path('subtopics/', SubTopicView.as_view(), name = "subtopics"),
    path('subtopic/<int:pk>/', OneSubTopicView.as_view(), name = "single_subtopic"),
    path('question/', QuestionPostView.as_view(), name = "post_question"),
    path('writeanswer/', AnswerPostView.as_view(), name = "post_answer"),
    path('postcomment/', AnswerCommentPostView.as_view(), name = 'post_comment'),
    path('likequestion/', QuestionLikePostView.as_view(), name = 'like_question'),
    path('likeanswer/', AnswerLikePostView.as_view(), name = 'like_answer'),
    path('question/<int:pk>/', OneQuestionView.as_view(), name = 'single_question'),
]