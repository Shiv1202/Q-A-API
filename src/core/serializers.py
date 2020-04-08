# Impport form Rest FrameWork
from rest_framework import serializers

# Importing Models.
from .models import (
    Topic,
    Question,
    Answer,
    Tag,
    Company,
    Answer_comment,
    Question_like,
    Answer_like,
    SubTopic
)

# Defining Serializers For various Models.
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class SubTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTopic
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'Q_text',
            'com_tag',
            'subtopic',
            'tag',
            'user'
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'A_text',
            'Q_id',
            'user',
        ]

class AnswerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer_comment
        fields = [
            'Answer_id',
            'user_id',
            'comment_text',
        ]

class QuestionLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question_like
        fields = '__all__'

class AnswerLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer_like
        fields = '__all__'