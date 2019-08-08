#!/usr/bin/env python
# coding: utf-8

# ## 데이터획득
# 
# * api 사용
# * naver open api를 활용
# * urllib.request 모듈을 사용하여 통신처리 후 JSON 피싱을 통한 데이터 추출

# In[3]:


import urllib.request
import os
import sys


# #### naver API 사용을 위한 키(KEY)

# In[4]:


Client_ID     = 'q9NEpl6niEE2RxMRkhpS'
Client_Secret = 'yHqi17quim'


# * 통신할 URL 정의
# * parameter 정의 ( get 방식 or post 방식에 맞춰 구성 )
# * header에 위에서 정의한 키 및 응답 데이터 포멧에 대한 구성 추가
# * 통신 -> 응답 코드를 확인 : 200번 경우 (통신성공코드) -> 응답데이터에서 json 데이터획득
# * json 데이터에서 [ 가공 및 전처리는 일단 배제 ] 데이터를 적제(csv 혹은 xis 혹은 database)

# In[5]:


# 네이버 통합 검색어 트렌드 조회 URL
url = "https://openapi.naver.com/v1/datalab/search"
url


# In[6]:


body = '{"startDate":"2019-07-09","endDate":"2019-08-06","timeUnit":"month","keywordGroups":[{"groupName":"대한민국","keywords":["대한민국","korean"]},{"groupName":"일본","keywords":["일본","japan"]}],"device":"pc","ages":["3","4"],"gender":"f"}';
body


# In[7]:


# 통신 객체 생성
request = urllib.request.Request(url)
# 헤더 설정
request.add_header("X-Naver-Client-Id",Client_ID)
request.add_header("X-Naver-Client-Secret",Client_Secret)
request.add_header("Content-Type","application/json")


# In[8]:


# 실제 통신 : post방식
# 한글 데이터를 그대로 전송하면 오류 발생 => body.encode("utf-8") 처리
response = urllib.request.urlopen(request, data=body.encode("utf-8"))


# In[9]:


response


# In[10]:


# 응답 코드가 정상이면

rescode = response.getcode()
if(rescode==200):
    # 실제 응답 데이터를 획득
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


# In[ ]:





# In[11]:


# 뉴스 검색
news_url = 'https://openapi.naver.com/v1/search/news.json'
news_url


# In[12]:


# 파라미터
keyword = urllib.parse.quote('테니스')
news_param = 'query=%s&display=%s&start=%s&sort=%s' % (keyword, 10, 1, 'date')
news_param


# In[13]:


url = '%s?%s' %(news_url, news_param)
url


# In[14]:


# 통신 객체 생성
request = urllib.request.Request(url)
# 헤더 설정
request.add_header("X-Naver-Client-Id",Client_ID)
request.add_header("X-Naver-Client-Secret",Client_Secret)


# In[15]:


# 실제 통신
response = urllib.request.urlopen(request)


# In[16]:


# 응답 코드가 정상이면

rescode = response.getcode()
if(rescode==200):
    # 실제 응답 데이터를 획득
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


# In[17]:


response_body.decode('utf-8')


# In[18]:


tmp  = type(response_body.decode('utf-8'))
tmp


# In[19]:


# 원하는 데이터를 추출 ==> 파싱 ==> xml, json 같은 형식을 취해야한다.


# In[20]:


response = urllib.request.urlopen(request)


# In[21]:


import json


# In[22]:


tmp = json.load(response)
tmp 


# In[23]:


type(tmp)


# In[24]:


# 순서 >> 리스트 안에 목록 출력
tmp['items']


# In[25]:


# for문을 통해 리스트 안의 item값 출력
for item in tmp['items']:
    print(item)


# In[ ]:





# In[26]:


# title이 키인 딕셔너리 출력
for item in tmp['items']:
    print(item['title'])


# In[27]:


[ item['title'] for item in tmp['items'] ]


# In[ ]:





# In[ ]:




