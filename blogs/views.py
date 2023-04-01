from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post, Comment
from .forms import PostForm,CommentForm

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

def author_only(view_func):
    """
    Decorator that checks if the user performing the CRUD operation is the author of the post.
    """
    def wrapper(request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if post.author.id == request.user.id:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to perform this action.")
    return wrapper        




# class HomeView(ListView):
#     model = Post
#     paginate_by = 4
#     template_name = 'blogs/home.html'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(title__icontains=query) | Q(body__icontains=query)
#             )
#         return queryset

def home(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    posts = Post.objects.filter(
        Q(title__icontains=search_query) | Q(body__icontains=search_query)    
    )

    page = request.GET.get('page')
    results = 2
    paginator = Paginator(posts,results)
    
    try:        
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages    
        posts = paginator.page(page)


    context={'posts':posts,'search_query':search_query,'paginator':paginator}
    return render(request,'blogs/home.html',context)


# class ArticleDetailView(DetailView):
#     model = Post
#     template_name = 'blogs/detail-article.html'

# @method_decorator(login_required(login_url='login'), name='dispatch')
# class ArticleCommentView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'blogs/detail-article.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class ArticleCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/create-article.html'
    # fields = '__all__'   

    
@method_decorator(login_required(login_url='login'), name='dispatch')
class ArticleUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/update-article.html'

    @method_decorator(author_only)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)    

@method_decorator(login_required(login_url='login'), name='dispatch')
class ArticleDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    template_name = 'blogs/delete-article.html'
    success_url = reverse_lazy('home')

    @method_decorator(author_only)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)      

@login_required(login_url='login')
def UserBlogsView(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    context = {'posts' : posts}       

    return render(request,'blogs/home.html',context)



def BlogPost(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        comment = Comment.objects.create(
            name = request.user,
            post = post,
            body = request.POST.get('comment')
        )
        return redirect('detail-article',pk=post.id)
    
    context = {'post' : post}       

    return render(request,'blogs/detail-article.html',context)


@login_required(login_url='login')
def editComment(request,pk):
    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)

    if request.user != comment.name:
        return HttpResponse('you are not allowed here!!')

    if request.method == 'POST':
        comment.body = request.POST.get('body')
        comment.save()
        return redirect('detail-article',pk=comment.post.id)

    context = {'form':form,'comment':comment}
    return render(request,'blogs/edit-comment.html',context)

@login_required(login_url='login')
def deleteComment(request,pk):
    comment = Comment.objects.get(id=pk)
    if request.user != comment.name:
        return HttpResponse('you are not allowed here!!')

    if request.method == 'POST':
        comment.delete()
        return redirect('detail-article',pk=comment.post.id)

    context = {'comment':comment}
    return render(request,'blogs/delete-article.html',context)