from django.contrib import admin
from blogapp.models import Post
from blogapp.models import Comment

class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','author','body','status','created','updated','publish')
	list_filter=('status','author')
	raw_id_fields=('author',)
	search_fields=('title','body','author')
	prepopulated_fields={'slug':('title',)}
	ordering=['status','publish']

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','email','post','body','created','updated','active')
	list_filter = ('active','created','updated')
	search_fields = ('name','email','body')
	
admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)

