"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from MyDjangoWebProject.settings import file_location
# app
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def upload(request):
    """Renders the upload page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/upload.html',
        {
            'title':'Upload Your Project in GitHub',
            'year':datetime.now().year,
        }
    )

def console(request):
    """Renders the console page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/console.html',
        {
            'title':'Verify Your Account in Google Console',
            'year':datetime.now().year,
        }
    )

def more(request):
    """Renders the more page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/more.html',
        {
            'title':'To Know more about Web Development',
            'year':datetime.now().year,
        }
    )

# app/setup
def setup(request):
    """Renders the setup page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/setup/setup.html',
        {
            'content':'Learn How to SetUp Django in Your Application',
            'title':'Django Web Application Setup',
            'year':datetime.now().year,
        }
    )

def vs(request):
    """Renders the vs page."""
    #"settings1.py", "urls1.py", "wsgi1.py", "forms1.py", "tests1.py", "views1.py", "aurls1.py", "burls1.py", "basics.html"
    with open(file_location + 'files.txt', 'r') as file:
        files = file.read()
    t = '<p>'
    for j in range(0,len(files)):
        if files[j]=='~':
            t += '</p>~<p>'
        elif files[j]=='\n':
            t += '</p><p>'
        elif files[j]==' ':
            t += '&nbsp;'
        elif files[j]=='>':
            t += '&gt;'
        elif files[j]=='<':
            t += '&lt;'        
        else:
            t += files[j]
    files = t;
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/setup/vs.html',
        {
            'title':'Django Web Application Setup',
            'content':'Django Web Application Setup in Visual Studio 2019',
            'files':files,
            'year':datetime.now().year,
        }
    )

def vscode(request):
    """Renders the vscode page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/setup/vscode.html',
        {
            'title':'Django Web Application Setup',
            'content':'Django Web Application Setup in Visual Studio Code',
            'year':datetime.now().year,
        }
    )

def pycharm(request):
    """Renders the pycharm page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/setup/pycharm.html',
        {
            'title':'Django Web Application Setup',
            'content':'Django Web Application Setup in PyCharm',
            'year':datetime.now().year,
        }
    )

# app/host
def host(request):
    """Renders the setup page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/host/host.html',
        {
            'title':'Free Hosting Django Web Application with Various Websites',
            'year':datetime.now().year,
        }
    )
