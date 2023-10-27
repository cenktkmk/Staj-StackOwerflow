from django.contrib import admin
from .models import * 




admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Answer)
admin.site.register(Comments)
admin.site.register(Comments2)
admin.site.register(PostLikes)
admin.site.register(PostDislike)
admin.site.register(AnswerLikes)
admin.site.register(AnswerDislike)