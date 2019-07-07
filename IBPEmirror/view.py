from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def search(request):
    context = {}
    if 'q' in request.GET and request.GET['action'] == 'google':
        context['items'] = []
        context['action'] = 'google'
        for i in range(5):
            response = requests.get("https://www.google.com/"+"search?q="+request.GET['q']+"&start="+str(10*i-10)).text
            soup = BeautifulSoup(response, 'lxml')
            # links = soup.find_all('a')
            # for link in links:
            #     if link.find('div') and not link['href'].find("/url?q=") == -1 and not link.text == "":
            #         item = [link.text[:link.text.find("http")],
            #                 link['href'].strip("/url?q=")[:link['href'].strip("/url?q=").find("&sa=")]]
            #         context['items'].append(item)
            divs = soup.find_all('div')
            for div in divs:
                a = div.find('a')
                if a and len(div.find_all('span')) == 2 and len(div.find_all('div')) == 11:
                    if not a['href'].find("/url?q=") == -1 and not a.text == "":
                        item = {}
                        # item['title'] = a.text[:a.text.find("http")]
                        item['title'] = div.find('div').find('div').find_all('div')[0].text
                        item['subtitle'] = div.find('div').find('div').find_all('div')[1].text
                        item['link'] = a['href'].strip("/url?q=")[:a['href'].strip("/url?q=").find("&sa=")]
                        item['date'] = div.find_all('span')[0].text
                        item['preview'] = div.find_all('div')[-1].text.strip(item['date']).strip(div.find_all(
                            'span')[1].text)
                        context['items'].append(item)

    return render(request, 'search.html', context)