from django.contrib import admin
from .models import *
# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    max_num = 5  # optional: limit to 5 images

class ClientLogoInline(admin.TabularInline):
    model = ClientLogo
    extra = 1
    max_num = 5  # optional: limit to 5 logos

admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(ClientLogo)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(BlogPost)
admin.site.register(Education)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'bio', 'role']  # 🔥 this will raise error if name doesn’t exist

