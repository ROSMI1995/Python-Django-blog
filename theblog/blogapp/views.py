from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # used to view blogs
from .models import Post, Category, Comment
from .forms import PostForm, EditForm,CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import datetime
from django.core.paginator import Paginator



def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	#post.likes.add(request.user)
	#post.save()
	#return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))

def removeduplicate(request):
	postobj=Post.objects.raw('select author_id having count (author_id)>1')

	return render(request,'index.html',{"data":postobj})

def index(request):
    object_list = Post.objects.all()
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 8) # 6 employees per page


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'page_obj': page_obj})


class HomeView(ListView):
	model = Post
	context_object_name = 'posts'
	paginate_by = 8
	template_name = 'home.html'
	ordering = ['id']

    


	



	

	

class ArticleDetailView(DetailView):
	model = Post
	template_name ='post_details.html'

	#like and unlike function
	def get_context_data(self, *args, **kwargs):
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked =True
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name ='add_post.html'
	#fields = ('title', 'slug', 'author','body', 'status')


class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name ='add_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('article-details', kwargs={'pk':self.kwargs['pk']})



		

	#success_url= reverse_lazy('home')

class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name ='add_category.html'
	fields= ('name',)
	#fields = ('title', 'slug', 'author','body', 'status')

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'slug', 'body', 'status']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url= reverse_lazy('home')




	