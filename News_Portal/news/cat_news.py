import requests


def read_news_online_entertainment():
    news = []
    # Construct the URL dynamically based on the category
    url = "https://www.onmanorama.com/entertainment.html"
    # url = "https://www.onmanorama.com/topic/general-topics/76/health.html"

    res = requests.get(url).text.split('<div class="storylist-item-in video-preview">')
    print(res)
    print(len(res))
    for i in range(1, len(res)):
        try:

            srslink = 'https://www.onmanorama.com' + res[i].split('<a href="')[1].split('"')[0]
            # Extract image URL
            img = res[i].split('data-src="')[1].split('"')[0]

            # Extract headline and summary content
            mc = res[i].split('<h2 class="listing-title-002">')[1].split('target="_self">')

            head = mc[1].split('</a>')[0]
            sc = mc[2].split('</a>')[0]

            # Print extracted data for debugging
            print(img)
            print(head)
            print('---------------------------', sc)

            # Append the data to the news list
            news.append([img, head, sc,srslink])
        except Exception as e:
            # Handle any parsing issues gracefully
            print(f"Error parsing article {i}: {e}")
            continue
    return news

def read_news_online_health():
    news = []
    # Construct the URL dynamically based on the category
    # url = "https://www.onmanorama.com/entertainment.html"
    url = "https://www.onmanorama.com/topic/general-topics/76/health.html"


    res = requests.get(url).text.split('<div class="storylist-item-in">')
    print(res)
    print(len(res))
    for i in range(1, len(res)):
        try:

            srslink = 'https://www.onmanorama.com' + res[i].split('<a href="')[1].split('"')[0]
            # Extract image URL
            img = res[i].split('data-src="')[1].split('"')[0]

            # Extract headline and summary content
            mc = res[i].split('<h2 class="listing-title-002">')[1].split('target="_self">')

            head = mc[1].split('</a>')[0]
            sc = mc[2].split('</a>')[0]

            # Print extracted data for debugging
            print(img)
            print(head)
            print('---------------------------', sc)

            # Append the data to the news list
            news.append([img, head, sc,srslink])
        except Exception as e:
            # Handle any parsing issues gracefully
            print(f"Error parsing article {i}: {e}")
            continue
    return news
def read_news_online_sports():
    news = []

    url = "https://www.onmanorama.com/sports.html"

    res = requests.get(url).text.split('<div class="storylist-item-in video-preview">')
    print(res)
    print(len(res))
    for i in range(1, len(res)):
        try:

            srslink = 'https://www.onmanorama.com' + res[i].split('<a href="')[1].split('"')[0]
            # Extract image URL
            img = res[i].split('data-src="')[1].split('"')[0]

            # Extract headline and summary content
            mc = res[i].split('<h2 class="listing-title-002">')[1].split('target="_self">')

            head = mc[1].split('</a>')[0]
            sc = mc[2].split('</a>')[0]

            # Print extracted data for debugging
            print(img)
            print(head)
            print('---------------------------', sc)

            # Append the data to the news list
            news.append([img, head, sc,srslink])
        except Exception as e:
            # Handle any parsing issues gracefully
            print(f"Error parsing article {i}: {e}")
            continue
    return news


def read_news_online_world():
    news = []

    url = "https://www.onmanorama.com/topic/general-topics/43/world.html"

    res = requests.get(url).text.split('<div class="storylist-item-in">')
    print(res)
    print(len(res))
    for i in range(1, len(res)):
        try:

            srslink = 'https://www.onmanorama.com' + res[i].split('<a href="')[1].split('"')[0]
            # Extract image URL
            img = res[i].split('data-src="')[1].split('"')[0]

            # Extract headline and summary content
            mc = res[i].split('<h2 class="listing-title-002">')[1].split('target="_self">')

            head = mc[1].split('</a>')[0]
            sc = mc[2].split('</a>')[0]

            # Print extracted data for debugging
            print(img)
            print(head)
            print('---------------------------', sc)

            # Append the data to the news list
            news.append([img, head, sc,srslink])
        except Exception as e:
            # Handle any parsing issues gracefully
            print(f"Error parsing article {i}: {e}")
            continue
    return news



def read_news_online_kerala():
    news = []

    url = "https://www.onmanorama.com/news/kerala.html"

    res = requests.get(url).text.split('<div class="section-topstory-itemin">')
    print(res)
    print(len(res))
    for i in range(1, len(res)):
        try:

            srslink = 'https://www.onmanorama.com' + res[i].split('<a href="')[1].split('"')[0]
            # Extract image URL
            img = res[i].split('data-src="')[1].split('"')[0]

            # Extract headline and summary content
            mc = res[i].split('<h2 class="listing-title-002">')[1].split('target="_self">')

            head = mc[1].split('</a>')[0]
            sc = mc[2].split('</a>')[0]

            # Print extracted data for debugging
            print(img)
            print(head)
            print('---------------------------', sc)

            # Append the data to the news list
            news.append([img, head, sc,srslink])
        except Exception as e:
            # Handle any parsing issues gracefully
            print(f"Error parsing article {i}: {e}")
            continue
    return news


# print(read_news_online_kerala("health"))