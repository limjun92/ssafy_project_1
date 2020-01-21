


from django.shortcuts import render
import requests
import json

#임준형 rest => dcec71e023f9c1ef32498ea45540e114, script => 

# Create your views here.
def index(request):
    return render(request, 'map/index.html')
    ##

def test(request):
    if request.method == 'POST':
        data = request.POST.get('name')
        url = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+data
        urlc = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+data+" 카페"
        urll = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+data+" 도서관"
        urlsc = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+data+" 스터디카페"
        headers = {"Authorization": "KakaoAK dcec71e023f9c1ef32498ea45540e114"}
        result = requests.get(url, headers=headers)
        resultc = requests.get(urlc, headers=headers)
        resultl = requests.get(urll, headers=headers)
        resultsc = requests.get(urlsc, headers=headers)
        addr = json.loads(str(result.text))
        addrc = json.loads(str(resultc.text))
        addrl = json.loads(str(resultl.text))
        addrsc = json.loads(str(resultsc.text))
        #  print("##############################################")

        # for i in range(len(addr['documents'])):
        #     print(addr['documents'][i])
        # print()
        context = {
            'addr':addr['documents'],
            'addrc':addrc['documents'],
            'addrl':addrl['documents'],
            'addrsc':addrsc['documents'],
            'data':data
        }
       # print(context)

       # print("**********************************************")
    return render(request, 'map/result.html', context)

def test2(request):
    if request.method == 'POST':
        data = request.POST.get('name')
        url = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+data
        urlc = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+data+" 카페"
        urll = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+data+" 도서관"
        urlsc = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+data+" 스터디카페"
        headers = {"Authorization": "KakaoAK dcec71e023f9c1ef32498ea45540e114"}
        result = requests.get(url, headers=headers)
        resultc = requests.get(urlc, headers=headers)
        resultl = requests.get(urll, headers=headers)
        resultsc = requests.get(urlsc, headers=headers)
        addr = json.loads(str(result.text))
        addrc = json.loads(str(resultc.text))
        addrl = json.loads(str(resultl.text))
        addrsc = json.loads(str(resultsc.text))
        #  print("##############################################")

        # for i in range(len(addr['documents'])):
        #     print(addr['documents'][i])
        # print()
        context = {
            'addr':addr['documents'],
            'addrc':addrc['documents'],
            'addrl':addrl['documents'],
            'addrsc':addrsc['documents'],
            'data':data
        }
       # print(context)

       # print("**********************************************")
    return render(request, 'map/aaa.html', context)

def search(request):
    if request.method == 'POST':
        data = request.POST.get('name')
        url = "https://dapi.kakao.com/v2/local/search/keyword.json?query="+data
        headers = {"Authorization": "KakaoAK dcec71e023f9c1ef32498ea45540e114"}
        result = requests.get(url, headers=headers)
        addr = json.loads(str(result.text))

        context = {
            'addr':addr['documents'],
            'data':data
        }
       # print(context)

       # print("**********************************************")
    return render(request, 'map/search.html', context)

def many(request):
    return render(request, 'map/many.html')

def mylocate(request):
    return render(request, 'map/mylocate.html')