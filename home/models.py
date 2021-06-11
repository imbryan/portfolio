from django.db import models


class BlogPost(models.Model):
    date_published = models.DateTimeField('date field')
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    about_content = models.BooleanField(default=False)

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
    skill_body = models.TextField(null=True, blank=True)
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
    project_body = models.TextField()
    project_repository_url = models.URLField(null=True, blank=True)
    project_demo_url = models.URLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.project_title
