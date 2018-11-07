from django.contrib import admin
from .models import AccountInformation,Article
# Register your models here.


class AccountInformationAdmin(admin.ModelAdmin):
    list_display = ('username','password', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['username']
admin.site.register(AccountInformation, AccountInformationAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','tags', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
admin.site.register(Article, ArticleAdmin)