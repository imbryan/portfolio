from django.contrib import admin
from .models import BlogPost, Skill, Project, SkillCategory


class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post content', {'fields': ['post_title', 'post_body']}),
        ('Date information', {'fields': ['date_published']}),
        ('About flag', {'fields': ['about_content']}),
    ]


class SkillCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Skill category', {'fields': ['category_name']})
    ]


class SkillAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Skill content', {'fields': ['skill_title', 'skill_body', 'skill_level']}),
        ('Category', {'fields': ['skill_category']}),
    ]


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project content', {'fields': ['project_title', 'project_body', 'project_repository_url', 'project_demo_url', 'date']})
    ]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
