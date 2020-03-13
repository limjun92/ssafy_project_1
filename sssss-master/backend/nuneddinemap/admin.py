from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model

admin.site.register(get_user_model())
admin.site.register(Menu)
admin.site.register(Studycafe)
admin.site.register(Library)
admin.site.register(Cafe)
admin.site.register(Comment)
admin.site.register(Place)
admin.site.register(Userreview)
admin.site.register(Placepicture)
# admin.site.register(Board)
# admin.site.register(com)
