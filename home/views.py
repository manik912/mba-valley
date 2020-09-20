from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-date_published')
    popular = Post.objects.filter(popular=True)

    context = {
        'posts': posts,
        'popular':popular
    }
    return render(request, 'home/home.html', context)

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

