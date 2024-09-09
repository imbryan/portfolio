from django.shortcuts import render
from .models import BlogPost, Skill, Project


def index(request):
    technical_skills = Skill.objects.filter(skill_category__category_name='Technical').order_by('-skill_level')
    communication_skills = Skill.objects.filter(skill_category__category_name='Communication').order_by('-skill_level')
    miscellaneous_skills = Skill.objects.filter(skill_category__category_name='Miscellaneous').order_by('-skill_level')

    projects = Project.objects.all().order_by('-date')

    context = {
        'technical_skills': technical_skills,
        'communication_skills': communication_skills,
        'miscellaneous_skills': miscellaneous_skills,
        'projects': projects,
    }

    return render(request, 'home/index.html', context=context)


def blog(request):
    posts = BlogPost.objects.filter(about_content=False).order_by('-date_published')

    context = {
        'posts': posts,
    }

    return render(request, 'home/blog.html', context=context)
