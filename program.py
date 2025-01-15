import json
import requests as rq

client_id = '4hJQIuLLzXlG4QoLCztG'
client_secret = '_qhIt9gWWf'

keyword = '경제'
display_amount = 100
start_pos = 1

url = f'https://openapi.naver.com/v1/search/news.json?query={keyword}&display={display_amount}&start={start_pos}'

# 헤더에 Client ID와 Client Secret를 보냄 
header = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret':client_secret}

res = rq.get(url, headers=header)

print(res.status_code)

my_json = json.loads(res.text)

print(my_json.keys())

# 검색 결과 아이템들을 출력해 본다.
count = 1
for x in my_json['items']:
    if 'n.news.naver' in x.get('link'):                     # 네이버 뉴스만 가져온다!
        print('Count :' + str(count))
        print("Title : " + x.get('title'))
        print("Link : " + x.get('link'))
        print("Description : " + x.get('description'))
        print()
        count += 1