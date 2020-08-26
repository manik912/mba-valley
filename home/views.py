from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-date_published')

    context = {
        'posts': posts
    }
    return render(request, 'home/home.html', context)

class SearchView(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'Post.objects.all'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Post.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result


class PostDetailView(DetailView):
    model = Post
