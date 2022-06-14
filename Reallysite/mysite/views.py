from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def index(request):
	objs = Article.objects.all()[:3]
	content  = {
		'title': 'test',
		'articles': objs,
		}

	return render(request, 'mysite/index.html', content)


# def login(request):
# 	context = {}

# 	if request.method == "POST":
# 		context['req'] = request.POST
# 		print(context['req'])
# 	return render(request, 'mysite/login.html', context)


class login(LoginView):
	template_name = 'mysite/auth.html'
	
	def form_valid(self, form):
		messages.success(self.request, 'ログイン完了!!')
		return super().form_valid(form)

	def form_invalid(self, form):
		messages.error(self.request, 'ログイン失敗!!')
		return super().form_invalid(form)

def signup(request):
	context = {}
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			# user.is_active = False
			user.save()
			messages.success(request, '登録完了!!')
			return redirect('/')
	return render(request, 'mysite/auth.html', context)
