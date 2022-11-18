from django.contrib import admin


# from django.contrib.auth.admin import UserAdmin
# from .models import User

from api.models import Choice, Question, Profile, Forum, ForumComment, ForumVote


# User = get_user_model()

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Profile)
admin.site.register(Forum)
admin.site.register(ForumComment)
admin.site.register(ForumVote)



