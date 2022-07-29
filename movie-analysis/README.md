### 영화리뷰 감정분석

***

* 주요 기능 
1. BeautifulSoup을 이용한 웹 페이지 리뷰 크롤링

2. NLP에 쓰이는 nltk 라이브러리의 tokenize함수를 통해 전처리

3. nltk의 모듈 중 하나인 VADER(사전에 기반한 감정분석 툴)을 통해 감정 분석

4. 전처리과정이 끝난 데이터들을 엑셀에 저장

5. wordcloud를 통한 시각화


***

* 엑셀 파일

![image](https://user-images.githubusercontent.com/59947533/94016518-2a78f980-fde9-11ea-8ceb-0b24579e5d5b.png)


* wordcloud 결과

<img width="387" alt="wordcloud" src="https://user-images.githubusercontent.com/59947533/93694141-4ce9e900-fb43-11ea-9b6c-73d1e7647231.PNG">


***
#### VADER 아쉬운 점

감정분석을 사전을 기반으로 분석하다보니 예를들어 '이 영화는 미쳤다'!(미쳤다 : 최상의 기분을 표현하는 경우), '악당'의 단어가 들어가는 경우 긍정적인 리뷰인 경우에도 부정이라고 판단하는 결과를 낼 수 있다. 
