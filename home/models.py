from bs4 import BeautifulSoup
from django.db import models
from tinymce.models import HTMLField


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    date_published = models.DateTimeField('date field')
    post_title = models.CharField(max_length=200)
    post_body = HTMLField()  # Caution, check best practices
    preview_text = models.TextField(null=True, blank=True)
    about_content = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.post_title

    def is_about_content(self):
        return self.about_content
    
    def save(self, *args, **kwargs):
        if not self.preview_text:
            soup = BeautifulSoup(self.post_body, 'html.parser')
            words = soup.get_text().split()
            self.preview_text = ' '.join(words[:50])
            if len(words) > 50:
                self.preview_text += "…"
        super().save(*args, **kwargs)


class SkillCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=200)
    project_role = models.CharField(max_length=200, null=True, blank=True)  # Role in the project
    project_body = models.TextField()
    project_repository_url = models.URLField(null=True, blank=True)
    project_demo_url = models.URLField(null=True, blank=True)
    project_board_url = models.URLField(null=True, blank=True)
    project_download_url = models.URLField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    hidden = models.BooleanField(default=False)
    is_activism_tool = models.BooleanField(default=False)

    def __str__(self):
        return self.project_title


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    employer = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.position} at {self.employer}"


class Achievement(models.Model):
    """
    Deprecated class. See Credential instead.
    """
    id = models.AutoField(primary_key=True)
    achievement_name = models.CharField(max_length=200)
    achievement_body = models.TextField(null=False, default='', blank=True)
    achievement_url = models.URLField(null=False, default='', blank=True)
    achievement_date = models.DateField()
    achievement_issuer = models.CharField(max_length=200, null=False, default='', blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.achievement_name
    

class Credential(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_issued = models.DateField()
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    credential_id = models.CharField(max_length=200, null=True, blank=True)
    hidden = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Education(Credential):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    degree = models.CharField(max_length=200)
    major = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.name = f"{self.degree}, {self.major}"
        super().save(*args, **kwargs)

class Certification(Credential):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    cert_name = models.CharField(max_length=200)
    cert_level = models.CharField(max_length=200, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.cert_level:
            self.name = f"{self.cert_name}, {self.cert_level}"
        else:
            self.name = self.cert_name
        super().save(*args, **kwargs)


class Initiative(models.Model):
    id = models.AutoField(primary_key=True)
    initiative_name = models.CharField(max_length=200)
    initiative_alt_name = models.CharField(max_length=200, null=False, default='', blank=True)
    initiative_body = models.TextField(null=False, default='', blank=True)  # Description
    congress_url = models.URLField(null=False, default='', blank=True)
    petition_url = models.URLField(null=False, default='', blank=True)
    date_introduced = models.DateField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.initiative_name
