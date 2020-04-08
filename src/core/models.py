from django.db import models
from django.contrib.auth import get_user_model
# from django.core.validators import MinValueValidator

# Initilise Django inbuilt User Model.
User = get_user_model()


# Topic Table
class Topic(models.Model):
    topic_name = models.CharField(max_length = 64)
    objects = models.Manager()

    def __str__(self):
        return self.topic_name

# Tags Table
class Tag(models.Model):
    tag_name = models.CharField(max_length = 64, primary_key = True)
    objects = models.Manager()
    def __str__(self):
        return self.tag_name

# Company Table
class Company(models.Model):
    com_name = models.CharField(max_length = 64, primary_key = True)

    objects = models.Manager()
    def __str__(self):
        return self.com_name

# Subtopic Table
class SubTopic(models.Model):
    subtopic_name = models.CharField(max_length = 64, primary_key = True)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f"{self.topic} --> {self.subtopic_name}."
    
# Question Table 
class Question(models.Model):
    Q_text = models.TextField(max_length = 500, unique = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # com_id = models.ForeignKey(Company, on_delete = models.CASCADE, n)
    # topic_id = models.ForeignKey(Topic, on_delete = models.CASCADE)
    subtopic = models.ManyToManyField(SubTopic)
    com_tag = models.ManyToManyField(Company)
    tag = models.ManyToManyField(Tag)
    objects = models.Manager()

    def __str__(self):
        return f"{self.Q_text}  {self.user}  {self.com_tag}"

# Answer Table
class Answer(models.Model):
    A_text = models.TextField(max_length = 500)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_ans')
    Q_id = models.ForeignKey(Question, on_delete = models.CASCADE,)
    objects = models.Manager()

    def __str__(self):
        return f"{self.A_text}"

class Answer_comment(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    Answer_id = models.ForeignKey(Answer, on_delete = models.CASCADE)
    comment_text = models.TextField(max_length = 500)
    objects = models.Manager()

    def __str__(self):
        return f"{self.comment_text}  {self.Answer_id}  {self.user_id}"

class Question_like(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    Q_id = models.ForeignKey(Question, on_delete = models.CASCADE)
    objects = models.Manager()

class Answer_like(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    Answer_id = models.ForeignKey(Answer, on_delete = models.CASCADE)
    objects = models.Manager()