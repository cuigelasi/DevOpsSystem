from django.shortcuts import render
from .models import AccountInformation, Article
from django.utils import timezone
from markdown import markdown

#导入Paginator,EmptyPage和PageNotAnInteger模块
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def Index(request):
    return render(request, 'web/index.html')

def MarkDownTest(request):
    markdown_data = '''
# markdown测试
## 二级标签
### 三级标签
- 列表1
- 列表2
```python
#encoding=utf-8

def Login(request):
    error_data = "Login"
    return render(request, 'web/login.html',{"error_data":error_data})
```
'''
    markdown_data = markdown(markdown_data.replace("\r\n", '  \n'),extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ],safe_mode=True,enable_attributes=False)
    return render(request, 'web/markdowntest.html', {'markdown_data': markdown_data})


def ArticleTest(request):
    article_data = Article.objects.get(title='导读：知其然知其所以然')
    article_content_data = markdown(article_data.content)
    return render(request, 'web/articletest.html', {'article_content_data': article_content_data,'article_data':article_data})

def Login(request):
    error_data = "Login"
    return render(request, 'web/login.html',{"error_data":error_data})

def LoginCheck(request):
    username = request.GET['username']
    password = request.GET['password']
    if len(AccountInformation.objects.filter(username=username)) > 0:
        username_password_check = AccountInformation.objects.get(username=username)
        username_check =  username_password_check.username
        password_check = username_password_check.password
        if username_check == username and password_check == password:
            return render(request, 'web/index.html')
        else:
            error_data = "密码信息错误有误，请重新登陆！"
            return render(request, 'web/login.html',{"error_data":error_data})
    else:
        error_data = "该账号不存在，请联系管理员注册！"
        return render(request, 'web/login.html',{"error_data":error_data})

def Sign(request):
    error_data = "Sign in"
    return render(request, 'web/sign.html',{"error_data":error_data})

def SignCheck(request):
    username = request.GET['username']
    password = request.GET['password']
    password_again = request.GET['password_again']
    if len(AccountInformation.objects.filter(username=username)) == 0 and password == password_again :
        new_user = AccountInformation(username=username, password=password,pub_date=timezone.now())
        new_user.save()
        error_data = "Login"
        return render(request,  'web/login.html',{"error_data":error_data})
    else:
        error_data = "用户名已注册或两次输入的密码不一致"
        return render(request, 'web/sign.html',{'error_data':error_data})



def SVNIndex(request):
    return render(request, 'web/banbenkongzhi/svnindex.html')

def DjangoBlogIndex(request):
    articledata = Article.objects.all()



    # 生成paginator对象,定义每页显示条记录
    paginator = Paginator(articledata, 4)  # Show 25 contacts per page
    # 从前端获取当前的页码数
    page = request.GET.get('page',1)
    try:
        # 获取当前页码的记录
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        # 如果用户输入的页码不是整数时,显示第1页的内容
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        contacts = paginator.page(paginator.num_pages)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)
    return render(request, 'web/blogsystem/index.html',{'contacts':contacts,'paginator':paginator,'currentPage':currentPage})

def DjangoBlogShow(request):
    id = request.GET['id']
    articledata = Article.objects.get(id=id)
    article_content_data = markdown(articledata.content)
    return render(request, 'web/blogsystem/show.html',{'articledata':articledata,'article_content_data':article_content_data})