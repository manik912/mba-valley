from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post
from competition.models import competition

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-date_published')
    latest_popular = Post.objects.filter(latest_popular=True)
    mba_popular = Post.objects.filter(mba_popular=True)
    startup_popular = Post.objects.filter(startup_popular=True)
    latest_story = Post.objects.filter(latest_story=True)
    mba_story = Post.objects.filter(mba_story=True)
    startup_story = Post.objects.filter(startup_story=True)
    comp = competition.objects.filter(competition_popular=True)

    context = {
        'posts': posts,
        'latest_popular':latest_popular,
        'mba_popular':mba_popular,
        'startup_popular':startup_popular,
        'latest_story': latest_story,
        'mba_story': mba_story,
        'startup_story': startup_story,
        'comp':comp
    }
    return render(request, 'home/home.html', context)

def latest_story(request):
    posts = Post.objects.order_by('-date_published')
    latest_story = Post.objects.filter(latest_story=True)

    context = {
        'posts': posts,
        'latest_story': latest_story
    }

    return render(request, 'home/latest stories.html', context)

def mba_story(request):
    posts = Post.objects.order_by('-date_published')
    mba_story = Post.objects.filter(mba_story=True)

    context = {
        'posts': posts,
        'mba_story': mba_story
    }

    return render(request, 'home/mba stories.html', context)

def startup_story(request):
    posts = Post.objects.order_by('-date_published')
    startup_story = Post.objects.filter(startup_story=True)

    context = {
        'posts': posts,
        'startup_story': startup_story
    }

    return render(request, 'home/startup stories.html', context)

# class SearchView(ListView):
#     model = Post
#     template_name = 'search.html'
#     context_object_name = 'Post.objects.all'

#     def get_queryset(self):
#        result = super(SearchView, self).get_queryset()
#        query = self.request.GET.get('search')
#        if query:
#           postresult = Post.objects.filter(title__contains=query)
#           result = postresult
#        else:
#            result = None
#        return result

def SearchView(request):
    query = request.GET.get("search", None)
    qs = Post.objects.all()
    if query is not None:
        qs = qs.filter(title__icontains=query)
    context = {
        "posts": qs,
    }
    return render(request, 'home/search.html', context)



# class PostDetailView(DetailView):
#     model = Post

def PostDetailView(request, pk):

    post = Post.objects.filter(id=pk).first()
    
    context = {
        'post' : post,
    }

    return render(request, 'home/post_detail.html', context)

