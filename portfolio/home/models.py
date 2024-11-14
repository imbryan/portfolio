from django.db import models


class BlogPost(models.Model):
    date_published = models.DateTimeField('date field')
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    about_content = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.post_title

    def is_about_content(self):
        return self.about_content


class SkillCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Skill(models.Model):
    skill_title = models.CharField(max_length=200)
    skill_body = models.TextField(null=False, default='', blank=True)
    skill_level = models.IntegerField()
    skill_category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_title

    def level_text(self):
        if self.skill_level == 1: return "Basic knowledge"
        elif self.skill_level == 2: return "Novice"
        elif self.skill_level == 3: return "Intermediate"
        elif self.skill_level == 4: return "Advanced"
        elif self.skill_level == 5: return "Expert"


class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_role = models.CharField(max_length=200, null=False, default='', blank=True)  # Role in the project
    project_body = models.TextField()
    project_repository_url = models.URLField(null=False, default='', blank=True)
    project_demo_url = models.URLField(null=False, default='', blank=True)
    project_board_url = models.URLField(null=False, default='', blank=True)
    project_download_url = models.URLField(null=False, default='', blank=True)
    date = models.DateField(null=True, blank=True)
    hidden = models.BooleanField(default=False)
    is_activism_tool = models.BooleanField(default=False)

    def __str__(self):
        return self.project_title


class Achievement(models.Model):
    achievement_name = models.CharField(max_length=200)
    achievement_body = models.TextField(null=False, default='', blank=True)
    achievement_url = models.URLField(null=False, default='', blank=True)
    achievement_date = models.DateField()
    achievement_issuer = models.CharField(max_length=200, null=False, default='', blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.achievement_name


class Initiative(models.Model):
    initiative_name = models.CharField(max_length=200)
    initiative_alt_name = models.CharField(max_length=200, null=False, default='', blank=True)
    initiative_body = models.TextField(null=False, default='', blank=True)  # Description
    congress_url = models.URLField(null=False, default='', blank=True)
    petition_url = models.URLField(null=False, default='', blank=True)
    date_introduced = models.DateField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.initiative_name
