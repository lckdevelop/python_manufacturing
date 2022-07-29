from urllib.request import urlopen  # 파이썬 3의 경우 from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from openpyxl import Workbook
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# openpyxl을 이용해 엑셀 파일로 저장하기 위한 준비 과정
excell = Workbook(write_only=True)
ws = excell.create_sheet()
ws.append(['score', 'title', 'writer', 'date', 'review', 'senti_score'])

# 웹 페이지 불러오기
url = 'https://www.imdb.com/title/tt4154756/reviews?ref_=tt_ql_3'
print(url)
webpage = urlopen(url)
source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')

review_list = source.findAll('div', {'class': 'imdb-user-review'})

sid = SentimentIntensityAnalyzer()  # VADER 감정분석기 준비

sum_review = ''  # wordcloud 띄워줄때 쓸 리뷰 텍스트를 합칠 문자열

# 전체 리뷰
for review in review_list:
    # 리뷰 내에서 태그, 클래스 이용해서 정보 뽑아내는 부분
    list1 = []
    score = review.find('span').get_text()
    title = review.find('a').get_text().replace('\n', '')
    writer = review.find('span', {'class': 'display-name-link'}).get_text()
    date = review.find('span', {'class': 'review-date'}).get_text()
    content = review.find('div', {'class': 'text show-more__control'}).get_text()

    # 엑셀 파일에 저장하기 위해 list에 각 정보를 추가
    list1.append(score)
    list1.append(title)
    list1.append(writer)
    list1.append(date)
    list1.append(content)
    sum_review = sum_review + content

    lines_list = tokenize.sent_tokenize(content)  # 리뷰 텍스트를 문장별로 쪼개는 tokenize 함수

    sum = 0  # 한 리뷰의 문장마다의 점수를 합쳐줄 변수
    for sent in lines_list:  # 한 리뷰의 각 문장마다 감정 점수 계산
        ss = sid.polarity_scores(sent)
        print(ss['compound'])
        sum = sum + ss['compound']
    sum1 = str(sum / len(lines_list))  # 문장들의 평균점수가 그 리뷰의 감정 점수
    list1.append(sum1)
    ws.append(list1)  # 전처리과정과 점수합산의 데이터를 append

excell.save('anal_review.xlsx')  # 지금까지 append한 데이터들을 엑셀파일에 저장

def generate_wordcloud(text):  # 워드클라우드 만드는 부분
    wordcloud = WordCloud(font_path='framd.ttf',
                          width=2400, height=1800,
                          ranks_only=None,
                          relative_scaling=0.8,
                          stopwords=set(STOPWORDS)
                          ).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()  # 화면에 띄워주기 위한 matplotlib 함수

generate_wordcloud(sum_review)