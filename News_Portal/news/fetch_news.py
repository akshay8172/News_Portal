import requests

def read_news_online():
    news=[]
    res=requests.get("https://www.onmanorama.com/content/mm/en/kerala.html").text.split('<li class="storylist-item storylist-large">')

    for i in range(1,len(res)):
        # print(res[i])

        srslink='https://www.onmanorama.com'+res[i].split('<a href="')[1].split('"')[0]
        img=res[i].split('data-src="')[1].split('"')[0]

        mc=res[i].split('<h2 class="listing-title-002">')[1].split('target="_self">')

        head=mc[1].split('</a')[0]
        sc=mc[2].split('</a')[0]
        print(img)
        print(head)
        print(sc)
        print(srslink)
        news.append([img,head,sc,srslink])

    return news


