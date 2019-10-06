from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Category
from markdown import markdown
from django.template.loader import get_template
# Create your views here.

# def index(request):
# 	return HttpResponse('Hello World!')

# def index(request):
# 	#对Article进行声明并实例化，然后生成对象allarticle
# 	allarticle = Article.objects.all()
# 	#把查询到的对象，封装到上下文
# 	context = {
# 		'allarticle': allarticle,
# 		}
# 	#把上传文传到模板页面index.html里
# 	return render(request,'blog/index.html',context)

#首页
#从models里导入Category类
def index(request):
	pass
	
#列表页
def list(request):
	allarticle = Article.objects.all()
	# print(allarticle)
	# allarticle.body = markdown.markdown(allarticle.body)
	#把查询出来的分类封装到上下文里
	context = {'articles': allarticle,}
	return render(request, 'blog/list.html', context)#把上下文传到index.html页面


#内容页
def show(request, sid):
	article = Article.objects.get(id=sid)
	article.body = markdown(article.body.replace("\r\n", '  \n'),
		extensions=['markdown.extensions.extra',
		'markdown.extensions.codehilite',
		'markdown.extensions.toc',],
		safe_mode=True,enable_attributes=False)
	context = {'article': article,}
	# template = get_template('blog/show.html')
	# return_dict = {'title': article.title, 'category': article.category, 
	# 'user':article.user, 'date': article.created_time, 
	# 'body': markdown(article.body.replace("\r\n", '  \n'),
	# 	extensions=['markdown.extensions.extra',
	# 	'markdown.extensions.codehilite',
	# 	'markdown.extensions.toc',],
	# 	safe_mode=True,enable_attributes=False),
	# 	} # 此处文章的内容转化成html
	# return HttpResponse(template.render(return_dict, request))
	return render(request, 'blog/show.html', context)
	

#标签页
def tag(request, tag):
	pass

# 搜索页
def search(request):
	pass
# 关于我们
def about(request):
	pass