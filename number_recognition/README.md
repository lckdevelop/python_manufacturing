### Tensorflow와 MNIST데이터베이스를 활용한 숫자(손 글씨) 인식 프로그램

***

#### MNIST데이터베이스 : 필기체 숫자 이미지 데이터베이스

각 숫자에 대해 근거를 계산할 방법을 알려주는 가중치를 찾는 과정으로 이루어짐

mnist_1.py : 머신을 학습시키는 파일

: mnist데이터를 토대로 학습

mnist_2.py : 손 글씨를 인식시켜 결과 도출하는 파일

: 손 글씨 이미지(0-9.png) => 데이터의 흑백화(image_0-9.png) => 컴퓨터가 알아듣는 배열 데이터로 변경(b_0-9.png)

***
![result](https://user-images.githubusercontent.com/59947533/94332305-16164600-000f-11eb-8159-a9a084fcb20f.png)
