import bs4
import urllib.request as req
import threading
import queue

url = 'https://www.ptt.cc/bbs/movie/index.html'
movie_articles = []  # 用來存放抓取到的文章
article_urls = queue.Queue()  # 用來存放文章的 URL


def parse_html(url):
    request = req.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    })
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')
    return bs4.BeautifulSoup(data, 'html.parser')


def get_page_info(root):
    titles = root.find_all('div', class_='title')
    likes = root.find_all('div', class_='nrec')
    previous_page = root.find(
        'div', 'btn-group btn-group-paging').find_all('a')[1]['href']
    return titles, likes, previous_page


def collect_articles_info(titles, likes, previous_page, movie_articles, article_urls):
    min_len = min(len(titles), len(likes))
    for i in range(min_len):
        if titles[i].a is not None:
            movie_title = titles[i].a.string
            article_url = 'https://www.ptt.cc' + titles[i].a['href']
            article_urls.put((movie_title, article_url))  # 將標題與URL一起存入
            try:
                like_count = likes[i].span.text
            except AttributeError:
                like_count = '0'
            movie_articles.append([movie_title, like_count])


def add_article_time(title, url):
    article_root = parse_html(url)
    time = article_root.find_all('span', 'article-meta-value')[-1].string
    return [title, time]


def worker(article_urls, movie_articles):
    while not article_urls.empty():
        title, url = article_urls.get()  # 獲取標題與URL
        time_info = add_article_time(title, url)
        for article in movie_articles:
            if article[0] == time_info[0]:
                article.append(time_info[1])  # 加入時間
                break


for _ in range(3):
    root = parse_html(url)
    titles, likes, previous_page = get_page_info(root)
    collect_articles_info(titles, likes, previous_page,
                          movie_articles, article_urls)
    url = 'https://www.ptt.cc' + previous_page  # 更新 url 為上一頁的頁面

threads = []
for _ in range(10):  # 建立 10 個工作緒
    t = threading.Thread(target=worker, args=(article_urls, movie_articles))
    t.start()
    threads.append(t)

for t in threads:  # 等待所有的工作緒完成任務
    t.join()

with open("movie.txt", "w", encoding='utf-8') as f:
    for article in movie_articles:
        f.write(','.join(article) + "\n")
