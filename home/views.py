from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Skill, Project, Education, Certification, Initiative, Experience


def index(request):
    # technical_skills = Skill.objects.filter(skill_category__category_name='Technical').order_by('-skill_level')
    # communication_skills = Skill.objects.filter(skill_category__category_name='Communication').order_by('-skill_level')
    # miscellaneous_skills = Skill.objects.filter(skill_category__category_name='Miscellaneous').order_by('-skill_level')

    # projects = Project.objects.all().order_by('-date')

    # context = {
    #     'technical_skills': technical_skills,
    #     'communication_skills': communication_skills,
    #     'miscellaneous_skills': miscellaneous_skills,
    #     'projects': projects,
    # }

    # achievements = Achievement.objects.filter(hidden=False).order_by('-achievement_date')

    educations = Education.objects.filter(hidden=False).order_by('-date_issued')
    certs = Certification.objects.filter(hidden=False).order_by('-date_issued')
    experiences = Experience.objects.filter(hidden=False).order_by('-start_date')

    latest_blog_post = BlogPost.objects.filter(about_content=False, hidden=False).order_by('-date_published').first()

    context = {
        'educations': educations,
        'certs': certs,
        'experiences': experiences,
        'latest_blog_post': latest_blog_post,
    }

    return render(request, 'home/index.html', context=context)


def projects(request):
    projects = Project.objects.filter(hidden=False).order_by('-date')

    tag = request.GET.get('tag', None)
    if tag:
        projects=projects.filter(tags__slug=tag)

    context = {
        'projects': projects,
    }

    return render(request, 'home/projects.html', context=context)


def activism(request):
    tools = Project.objects.filter(hidden=False, is_activism_tool=True).order_by('-date')
    initiatives = Initiative.objects.filter(hidden=False).order_by('-date_introduced')

    context = {
        'tools': tools,
        'initiatives': initiatives,
    }
    return render(request, 'home/activism.html', context=context)


def blog(request):
    """
    Blog list view
    """
    posts = BlogPost.objects.filter(about_content=False, hidden=False).order_by('-date_published')

    tag = request.GET.get('tag', None)
    if tag:
        posts = posts.filter(tags__slug=tag)

    paginator = Paginator(posts, 6)
    page_num = request.GET.get('page', 1)

    get_params = request.GET.copy()
    if 'page' in get_params:
        del get_params['page']

    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'params': get_params.urlencode(),
    }

    return render(request, 'home/blog.html', context=context)


def blog_post(request, id=None, slug=None):
    # Blog detail view
    if id:
        post = get_object_or_404(BlogPost, id=id)
    else:
        post = get_object_or_404(BlogPost, slug=slug)

    if post.hidden:
        raise Http404()

    context = {
        'post': post
    }

    return render(request, 'home/blog_post.html', context=context)
