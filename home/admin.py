from django.contrib import admin
from .models import BlogPost, Skill, Project, SkillCategory, Achievement, Initiative, Education, Certification


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
        ('Project content', {'fields': ['project_title', 'project_role','project_body', 'project_repository_url', 'project_demo_url', 'project_board_url', 'project_download_url', 'date']}),
        ('Flags', {'fields': ['is_activism_tool', 'hidden']})
    ]


class AchievementAdmin(admin.ModelAdmin):
    """
    Deprecated model
    """
    fieldsets = [
        ('Achievement content', {'fields': ['achievement_name', 'achievement_body', 'achievement_issuer', 'achievement_url', 'achievement_date']}),
        ('Flags', {'fields': ['hidden']})
    ]


class EducationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Education content', {'fields': ['degree', 'major', 'issuer', 'date_issued', 'description', 'url', 'credential_id']}),
        ('Flags', {'fields': ['hidden']})
    ]


class CertificationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Certification content', {'fields': ['cert_name', 'cert_level', 'issuer', 'date_issued', 'expiration_date', 'description', 'url', 'credential_id']}),
        ('Flags', {'fields': ['hidden']})
    ]

class InitiativeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Initiative content', {'fields': ['initiative_name', 'initiative_alt_name', 'initiative_body', 'congress_url', 'petition_url', 'date_introduced']}),
        ('Flags', {'fields': ['hidden']})
    ]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Certification, CertificationAdmin)
