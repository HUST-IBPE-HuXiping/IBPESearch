from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Home Page
def index(request):
    return HttpResponse(requests.get("https://www.google.com").text.replace("search", "google"))

# Search Google
def google(request):
    if 'q' in request.GET:
        response=requests.get("https://www.google.com/"+"search?q="+request.GET['q']).text

        soup = BeautifulSoup(response, 'lxml')
        response=response.replace(str(soup.find_all('a')[0]), "IBPE专用 Google搜索引擎")

        soup = BeautifulSoup(response, 'lxml')
        print(str(soup.find_all('div', id="main")[0].find_all("div")[0]))
        response=response.replace(str(soup.find_all('div', id="main")[0].find_all("div")[0]), "132445555555555555555555555566666666666666666666")
        # print(response.replace(str(soup.find_all('div', id="main")[0].find_all("div")[0]), "1324"))
        return HttpResponse(response)

