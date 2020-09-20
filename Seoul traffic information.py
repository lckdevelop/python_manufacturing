from selenium import webdriver
import matplotlib.pyplot as plt
import time

driver = webdriver.Firefox(executable_path='c:/gecko/geckodriver.exe')
driver.get('https://topis.seoul.go.kr')

def make_source():
    cnt = 0

    while (True):
        # 클롤링하여 파일에 쓰기
        f1 = open("C:/Users/leechaekyeong/Desktop/velocity.txt", 'a')

        seoul = driver.page_source
        seoul = seoul[seoul.index('<span class=\"txt-g\" id=\"spdStat1\">') + len('<span class=\"txt-g\" id=\"spdStat1\">'):]
        seoul = seoul[:seoul.index('</span>')]

        city = driver.page_source
        city = city[city.index('<span class=\"txt-y\" id=\"spdStat2\">') + len('<span class=\"txt-y\" id=\"spdStat2\">'):]
        city = city[:city.index('</span>')]
        print('서울시 전체속도')
        print(seoul)
        print('도심 전체속도')
        print(city)

        f1.write(seoul + '\n')
        f1.write(city + '\n')

        # 10개가 모이면(20라인) 파일을 읽어 그래프로 나타내기
        if cnt != 0 and cnt % 20 == 0:
            f2 = open("C:/Users/leechaekyeong/Desktop/velocity.txt", 'r')
            read_list = f2.readlines()[cnt - 20:cnt]  # 20라인까지 불러오기
            i_list = [float(i[0:4]) for i in read_list]  # 숫자만떼서 float으로 변환
            x_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # x축 지점의 값들
            seoul_value = [i_list[0], i_list[2], i_list[4], i_list[6], i_list[8], i_list[10],
                           i_list[12], i_list[14], i_list[16], i_list[18]]  # seoul y축 지점의 값들
            city_values = [i_list[1], i_list[3], i_list[5], i_list[7], i_list[9], i_list[11],
                           i_list[13], i_list[15], i_list[17], i_list[19]]  # city y축 지점의 값들
            plt.plot(x_values, seoul_value, marker='o', color='#5784ff')  # x축과 seoul_value 그래프 그리기
            plt.plot(x_values, city_values, marker='o', color='#ffe159')  # x축과 city_value 그래프 그리기
            plt.xlabel('Every Minute')
            plt.ylabel('seoul city, downtown velocity')
            plt.title('Seoul Velocity')
            plt.legend(['seoul', 'city'])
            plt.show()  # 그래프를 화면에 출력

            f2.close()
            i_list.clear()

        cnt += 2
        time.sleep(60)
        driver.refresh()

    f1.close()

if __name__ == '__main__':
    make_source()
