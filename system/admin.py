from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Take)
admin.site.register(Component_in_Module)
admin.site.register(ComponentText)
admin.site.register(ComponentImage)