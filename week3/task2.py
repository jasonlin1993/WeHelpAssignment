import bs4
import urllib.request as req
url = 'https://www.ptt.cc/bbs/movie/index.html'
movie_articles = []  # 用來存放抓取到的文章
count = 0

while count < 3:
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request = req.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    })
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

    # 解析原始碼，取得每篇文章的標題中的文字
    # 讓 BeautifulSoup 協助我們解析 HTML 格式文件
    root = bs4.BeautifulSoup(data, 'html.parser')

    # 尋找所有 class = 'title' 的 div 標籤
    titles = root.find_all('div', class_='title')

    # 推文數量
    likes = root.find_all('div', class_='nrec')

    # 上一頁
    previous_page = root.find(
        'div', 'btn-group btn-group-paging').find_all('a')[1]['href']

    # 確保 文章標題 和 推文數 有相同數量的元素
    min_len = min(len(titles), len(likes))

    for i in range(min_len):

        # 確保標題存在
        if titles[i].a is not None:
            movie_title = titles[i].a.string

            # 取得文章的URL
            article_url = 'https://www.ptt.cc' + titles[i].a['href']

            # 建立一個新的 Request 來獲取文章的頁面內容
            article_request = req.Request(article_url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
            })

            with req.urlopen(article_request) as article_response:
                article_data = article_response.read().decode('utf-8')
                article_root = bs4.BeautifulSoup(article_data, 'html.parser')

                # 文章發佈時間
                time = article_root.find_all(
                    'span', 'article-meta-value')[-1].string

            try:
                like_count = likes[i].span.text

            except AttributeError:
                like_count = '0'

            # 將 文章標題 和 推文數 加到 movie_articles 列表中
            movie_articles.append(movie_title + ',' + like_count + ',' + time)

        # 更新為上一頁
        url = "https://www.ptt.cc" + previous_page

    count += 1

with open("movie.txt", "w", encoding='utf-8') as f:
    for article in movie_articles:
        f.write(article + "\n")
