from django.shortcuts import render
from django.http import HttpResponse
import requests


def homepage(request):
    editorvalue = "Enter your code here"
    return render(request, 'Home.html', {'editorvalue': editorvalue,'ind':1,'color':"black"})


def compileIt(request):
    convert = {'c_cpp': 'Cpp14', 'java': 'Java', 'python': 'Python'}
    convertInd = {'Cpp14':1,'Java':2,'Python':3}
    if (request.method == 'POST'):
        code = request.POST['codeForBackend']
        input = request.POST['input']
        lang = request.POST['language']
        lang = convert[lang]
        ind = convertInd[lang]
        url = "https://ide.geeksforgeeks.org/main.php"
        data = {
            'lang': lang,
            'code': code,
            'input': input,
            'save': False
        }
        r = requests.post(url, data=data)
        ret = r.json()
        print(ret)
        output = ""
        color = "black"
        if (ret['compResult'] == 'F'):
            output = "Compilation error:\n" + ret['cmpError']
            color = "red"
        elif(len(ret['rntError']) != 0):
            output = ret['rntError']
            color = "red"
        else:
            output = ret['output']
        print(code)
        editorvalue = code
        return render(request, 'Home.html', {'editorvalue': editorvalue, 'output': output, 'input': input,'ind':ind,'color':color})
    print(request)
    return render(request, 'Home.html')
