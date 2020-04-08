from django.contrib import admin
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

# Register your models here.
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Company)
admin.site.register(Answer_comment)
admin.site.register(Question_like)
admin.site.register(Answer_like)
admin.site.register(SubTopic)