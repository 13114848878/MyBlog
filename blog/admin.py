from django.contrib import admin
from blog.models import Category, Tag, Banner, Link, Tui, Article
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	"""docstring for ArticleAdmin"""
	# 后台想要下显示的字段
	list_display = ('id','category', 'title', 'tui', 'user', 'created_time')
	list_per_page = 50 # 每页显示的文章数
	ordering = ('-created_time',) # 数据排列方式
	list_display_links = ('id', 'title') # 点击那些字段可以进入编辑页面

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'index')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
	list_display = ('id', 'name','link_url')