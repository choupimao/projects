from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(request.path)

def detail(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))


#展示链接的页面
def getTest1(request):

    return render(request,'booktest/getTest1.html')

#接收一键一值的情况
def getTest2(request):
    #根据键接收值
    a1=request.GET['a']
    b1=request.GET['b']
    c1=request.GET['c']
    #构造上下文
    context={'a':a1,'b':b1,'c':c1}
    #向模板中传递上下文，并调用模板进行渲染
    return render(request,'booktest/getTest2.html',context)

#接受一键多值的情况
def getTest3(request):
    a1=request.GET.getlist('a')
    context={'a':a1}
    return render(request,'booktest/getTest3.html',context)