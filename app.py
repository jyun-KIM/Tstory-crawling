import requests
from bs4 import BeautifulSoup

base_url = 'https://k-jyun.tistory.com/'  # 실제 크롤링하려는 URL로 변경

# 크롤링할 페이지 범위 설정 (예: 1~5 페이지)
for page_number in range(1, 9):
    url = f'{base_url}?page={page_number}'  # 페이지 번호를 URL에 삽입
    headers = {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = soup.select('#main > div > div:nth-child(2) > ul > li > div > div.box_contents > a.link_title > strong')
    
    # 추출된 제목들 출력
    print(f"Page {page_number}:")
    for idx, title in enumerate(titles, 1):
        print(f"Title {idx}: {title.get_text()}")
    print("\n")
