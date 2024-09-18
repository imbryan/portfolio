from django.contrib import admin
from .models import BlogPost, Skill, Project, SkillCategory, Achievement


class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post content', {'fields': ['post_title', 'post_body']}),
        ('Date information', {'fields': ['date_published']}),
        ('Flags', {'fields': ['about_content', 'hidden']}),
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
        ('Project content', {'fields': ['project_title', 'project_role','project_body', 'project_repository_url', 'project_demo_url', 'project_board_url', 'date', 'hidden']})
    ]


class AchievementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Achievement content', {'fields': ['achievement_name', 'achievement_body', 'achievement_issuer', 'achievement_url', 'achievement_date', 'hidden']})
    ]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Achievement, AchievementAdmin)
