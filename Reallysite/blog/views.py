from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator
# Create your views here.
def index(request):
	objs = Article.objects.all()
	paginator = Paginator(objs, 3)
	page_number = request.GET.get('page')	
	context = {
		# 'Article':objs,
		'page_obj':paginator.get_page(page_number),
		'page_number':page_number,
	}
	return render(request, 'blog/blogs.html', context)

def article(request, pk):
	obj = Article.objects.get(pk=pk)
	context = { 
		'Article': obj
	}
	return render(request, 'blog/article.html', context)
