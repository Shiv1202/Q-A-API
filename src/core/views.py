from django.shortcuts import render
from django.http import Http404

# Importing form Django Rest FrameWork.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Importing Serializers.
from .serializers import (
    CompanySerializer,
    TagSerializer,
    TopicSerializer,
    SubTopicSerializer,
    QuestionSerializer, QuestionLikeSerializer,
    AnswerSerializer, AnswerCommentSerializer, AnswerLikeSerializer,
)
# Importing Models.
from .models import (
    Company,
    Tag,
    Topic,
    Question,
    Answer,
    Answer_comment,
    Question_like,
    Answer_like,
    SubTopic
)

"""
    Class Based Views For Various Function.
    ModelView --> For extracting whole database.
    OneMoledView --> For single Object.
"""

class CompanyView(APIView):
    def get(self, request, *args, **kwargs):
        data = (Company.objects.all())
        s = CompanySerializer(data, many = True)
        return Response(s.data)

    def post(self, request, *args, **kwargs):
        serializers = CompanySerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class OneCompanyView(APIView):

    def get_object(self, pk):
        # try:
        #     return Company.objects.get(pk = pk)
        # except Company.DoesNotExist:
        #     raise Http404
        return Company.objects.get(pk = pk)
    
    def get(self, request, pk, format = None):
        company = self.get_object(pk)
        s = CompanySerializer(company)
        return Response(s.data)
    
    def put(self, request, pk, format = None):
        company = self.get_object(pk)
        s = CompanySerializer(company, data = request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        company = self.get_object(pk)
        company.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class TagView(APIView):
    def get(self, request, *args, **kwargs):
        data = (Tag.objects.all())
        s = TagSerializer(data, many = True)
        return Response(s.data)

    def post(self, request, *args, **kwargs):
        serializers = TagSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class OneTagView(APIView):

    def get_object(self, pk):
        # try:
        #     return Tag.objects.get(pk = pk)
        # except Tag.DoesNotExist:
        #     return Http404
        return Tag.objects.get(pk = pk)

    def get(self, request, pk, format = None):
        tag = self.get_object(pk)
        t = TagSerializer(tag)
        return Response(t.data)

    def put(self, request, pk, format = None):
        tag = self.get_object(pk)
        t = TagSerializer(tag, data = request.data)
        if t.is_valid():
            t.save()
            return Response(t.data)
        return Response(t.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        tag = self.get_object(pk)
        tag.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class TopicView(APIView):

    def get(self, request, *args, **kwargs):
        data = Topic.objects.all()
        s = TopicSerializer(data, many = True)
        return Response(s.data)

    def post(self, request, *args, **kwargs):
        serializers = TopicSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class OneTopicView(APIView):

    def get_object(self, pk):
        # try:
        #     return Topic.objects.get(pk = pk)
        # except Topic.DoseNotExist:
        #     return Http404
        return Topic.objects.get(pk = pk)

    def get(self, request, pk, format = None):
        topic = self.get_object(pk)
        t = TopicSerializer(topic)
        return Response(t.data)

    def put(self, request, pk, format = None):
        topic = self.get_object(pk)
        t = TopicSerializer(topic, data = request.data)
        if t.is_valid():
            t.save()
            return Response(t.data)
        return Response(t.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        topic = self.get_object(pk)
        topic.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class SubTopicView(APIView):

    def get(self, request, *args, **kwargs):
        data = SubTopic.objects.all()
        s = SubTopicSerializer(data, many = True)
        return Response(s.data)

    def post(self, request, *args, **kwargs):
        serializers = SubTopicSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class OneSubTopicView(APIView):

    def get_object(self, pk):
        # try:
        #     return SubTopic.objects.get(pk = pk)
        # except SubTopic.DoseNotExist:
        #     return Http404
        return SubTopic.objects.get(pk = pk)
    
    def get(self, request, pk, foramt = None):
        subtopic = self.get_object(pk)
        st = SubTopicSerializer(subtopic)
        return Response(st.data)
    
    def put(self, request, pk, format = None):
        subtopic = self.get_object(pk)
        st = SubTopicSerializer(subtopic, data = request.data)
        if st.is_valid():
            st.save()
            return Response(st.data)
        return Response(st.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        st = self.get_object(pk)
        st.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class QuestionPostView(APIView):

    def post(self, request, *args, **kwargs):
        serializers = QuestionSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            x = Question.objects.get(Q_text = serializers.data.get('Q_text'))
            return Response(x.id)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class AnswerPostView(APIView):

    def post(self, request, *args, **kwargs):
        serializers = AnswerSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            x = Answer.objects.get(A_text = serializers.data.get('A_text'))
            return Response(x.id)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class AnswerCommentPostView(APIView):

    def post(self, request, *args, **kwargs):
        serializers = AnswerCommentSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            x = Answer_comment.objects.get(comment_text = serializers.data.get('comment_text'))
            return Response(x.id)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class QuestionLikePostView(APIView):

    def post(self, request, *args, **kwargs):
        serializers = QuestionLikeSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class AnswerLikePostView(APIView):

    def post(self, request, *args, **kwargs):
        serializers = AnswerLikeSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
"""
    Below class is associated for getting single Question.
    Input : Primary Key 
    Output : Serialized.
"""
class OneQuestionView(APIView):

    # Function for get the comment on various answers.
    def get_comment(self, ans_id):
        x = Answer_comment.objects.filter(Answer_id = ans_id)
        z = []
        for j in x:
            # y = {
            #     'comment_text' : j.comment_text,
            #     # 'user_id' : j.user_id,
            #     'Answer_id' : ans_id
            # }
            y = AnswerCommentSerializer(j)
            z.append(y.data)
        return z

    # Function for get the Company name from database for related questions.
    def get_company(self, com_id):
        ans = []
        for i in com_id:
            x = Company.objects.get(pk = i)
            ans.append(x.com_name)
        return ans

    # Function for get the Tag name associated to the question.
    def get_tag(self, tag_id):
        ans = []
        for i in tag_id:
            x = Tag.objects.get(pk = i)
            ans.append(x.tag_name)
        return ans

    # Function for get the Answer Related to the Question.
    def get_answers(self, pk):
        x = Answer.objects.filter(Q_id = pk)
        ans = []
        for i in x:
            y = {
                'answer_text' : i.A_text,
                # 'user-id' : i.user_id,
                'likes' : Answer_like.objects.filter(Answer_id = i.id).count(),
                'comment' : self.get_comment(i.id)
            }
            ans.append(y)
        return ans
    
    # Main Function for get Request to get single Question.
    def get(self, request, pk, format = None):
        x = Question.objects.get(pk = pk)
        data = {
            'question_text' : x.Q_text,
            'answers' : self.get_answers(pk),
            'likes' : Question_like.objects.filter(Q_id = pk).count(),
            'companies' : self.get_company(x.com_tag.all()),
            'tags' : self.get_tag(x.tag.all()),
        }
        return Response(data)
