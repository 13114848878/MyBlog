# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Article, Category
from markdown import markdown, Markdown
from django.template.loader import get_template
from django.core.paginator import Paginator
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
	
	return render(request,'blog/index.html')
	
#列表页
def list(request):
	allarticle = Article.objects.all()
	# print(allarticle)
	# allarticle.body = markdown.markdown(allarticle.body)
	#把查询出来的分类封装到上下文里
	
	# 设置每页显示几篇文章
	paginator = Paginator(allarticle, 2)

	# page_range is like range(1,2)
	page_range = paginator.page_range
	
	# a = [i for i in page_range]
	
	# 获取 url 中的页码
	page = request.GET.get('page')
	# print(page)
	#
	# 将导航对象相应的页码内容返回给 articles, 当page不是数字的时候返回第一页
	articles = paginator.get_page(page)
	# print(articles.number, type(articles.number))
	# for i in range(1,2):
	# 	print(i, type(i))

	context = {'articles': articles, 
	"page_range":page_range, 
	"current_num":int(articles.number),# 需要转换数据类型，在前端并不是int型
	} 
	return render(request, 'blog/list.html', context)


#内容页
def show(request, sid):
	article = get_object_or_404(Article, pk=sid)
	# article = Article.objects.get(id=sid)
	# 此处使用了Markdown替换了之前的markdown 
	md = Markdown(extensions=['markdown.extensions.extra',
	 	'markdown.extensions.codehilite',
	 	'markdown.extensions.toc',],)

	article.body = md.convert(article.body.replace("\r\n", '  \n'),)

	context = {'article': article, "toc":md.toc}
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

# 关于我们
def source(request):

	return render(request, 'blog/source.html')