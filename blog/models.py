# coding:utf-8


from django.db import models
#导入Django自带用户模块
from django.contrib.auth.models import User 
# 载入富文本类
from DjangoUeditor.models import UEditorField
from mdeditor.fields import MDTextField
# Create your models here.

class Category(models.Model):
	"""
	文章分类表
	"""
	name = models.CharField('分类', max_length=100)
	index = models.IntegerField(default=999, verbose_name='分类排序')

	class Meta:
		verbose_name = '分类'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class Tag(models.Model):
	"""
	文章标签表
	"""
	name = models.CharField('标签', max_length=30)

	class Meta:
		verbose_name = '标签'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

class Tui(models.Model):
	"""
	推荐表
	"""
	name = models.CharField('推荐', max_length=30)

	class Meta:
		verbose_name = '推荐'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class Banner(models.Model):
	"""
	幻灯图片
	"""
	text_info = models.CharField('图片信息', max_length=100, default='')
	img = models.ImageField('轮播图', upload_to='banner/')
	link_url = models.URLField('图片链接', max_length=100)
	is_active = models.BooleanField('是否激活', default=False)

	
	def __str__(self):
		return self.text_info

	class Meta:
		verbose_name = '轮播图'
		verbose_name_plural = verbose_name


class Link(models.Model):
	"""
	友情链接表
	"""
	name = models.CharField('链接名称',max_length=70)
	link_url = models.URLField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '友情链接'
		verbose_name_plural = verbose_name


class Article(models.Model):

	title = models.CharField(verbose_name='标题', max_length=100)
	excerpt = models.TextField(verbose_name='摘要', max_length=256, blank=True)
	#使用外键关联分类表与分类是一对多关系
	category = models.ForeignKey(Category, on_delete=models.CASCADE, 
		verbose_name='分类', blank=True, null=True)
	#使用外键关联标签表与标签是多对多关系
	tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True,)
    
	img = models.ImageField(upload_to='article_img/%Y/%m/%d/', 
		verbose_name='文章封面图片', blank=True, null=True)

	# body = models.TextField(verbose_name='文章内容')
	# 替换成富文本。
	# imagePath="upimg/", filePath="upfile/" 
	# 这两个是图片和文件上传的路径，我们上传文件，
	# 会自动上传到项目根目录media文件夹下对应的upimg和upfile目录里
	# 
	# body = UEditorField('内容', width=800, height=500, 
	# 	toolbars="full", imagePath="upimg/", filePath="upfile/",
	# 	upload_settings={"imageMaxSize": 1204000},
	# 	settings={}, command=None, blank=True,
	# 	)
	# 	
	# 使用MarkDown富文本	
	body = MDTextField(verbose_name='文章内容')

	"""
     文章作者，这里User是从django.contrib.auth.models导入的。
     这里我们通过 ForeignKey 把文章和 User 关联了起来。
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
     
	views = models.PositiveIntegerField(verbose_name='阅读量', default=0)

	tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, 
		verbose_name='推荐位', blank=True, null=True)
    
	created_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
	modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = '文章'

	def __str__(self):
		return self.title
