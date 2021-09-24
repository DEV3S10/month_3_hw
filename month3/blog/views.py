import random
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.views import generic
from rest_framework.generics import ListAPIView
# Create your views here.
from django.shortcuts import render, redirect

from .forms import BlogSerializer
from .models import Student, Blog, Comment


class BlogView(generic.ListView):
    template_name = "index.html"
    queryset = Blog.objects.all()
    context_object_name = "posts"


class BlogDetailView(generic.DetailView):
    template_name = "detail-post.html"
    queryset = Blog.objects.all()
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        blog_id = self.kwargs['pk']
        comments = Comment.objects.filter(blog_id=blog_id)
        context['comments'] = comments
        return context

    def post(self, request, *args, **kwargs):
        Comment.objects.create(
            blog_id=kwargs['pk'],
            text=request.POST['comment']
        )
        return redirect(f'/blog/{kwargs["pk"]}/')


def date_view(request):
    today = datetime.now()
    return HttpResponse(f"Now {str(today)}")


def random_number(request):
    num = random.randint(1, 1000)
    num2 = random.randint(1, num)
    num3 = random.randint(1, num2)
    num4 = random.randint(1, num3)
    context = {'num': num, 'numbers': [num2, num3, num4]}
    return render(request, 'random.html', context)


def image_view(request):
    path = settings.BASE_DIR / 'static' / '123.jpg'
    file = open(path, 'rb')
    return FileResponse(file)


def student_view(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)


def create_post(request):
    if request.method == "POST":
        form = request.POST
        title = form['title']
        description = form['description']
        hashtag = form['hashtag']
        image = request.FILES['image']
        Blog.objects.create(title=title, description=description, hashtags=hashtag, image=image)
        return redirect('/blog')
    if request.method == "GET":
        return render(request, "create-post.html")


class BlogListApiView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
