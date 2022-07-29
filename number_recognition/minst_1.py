# minst_1파일은 머신을 학습 시키는 파일
import tensorflow as tf
# MNIST데이터 가져오기
from tensorflow.examples.tutorials.mnist import input_data

# 입력
# 해당 경로에 데이터 생성
# images파일에는 배열, labels파일에는 결과가 들어있다.

# mnist의 데이터를 읽어 들이는 메서드 /tmp/data : 데이터가 저장될 위치 , 데이터에 레이블을 지정하는 방식
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# 모델
x = tf.placeholder(tf.float32, [None, 784]) # placeholder: 연산 그래프가 실행될 때 제공되어야 하는 값

W = tf.Variable(tf.zeros([784, 10])) # variable: 연산 과정에서 조작되는 값
b = tf.Variable(tf.zeros([10]))

y_model = tf.matmul(x, W) + b # 예측 모델

# 라벨
y = tf.placeholder(tf.float32, [None, 10]) # 정답 라벨

# 손실함수(loss)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=y_model))
# 손실 함수의 값을 최소화 하는 방법
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)  # learning_rate = 0.01

# 세션
sess = tf.Session()

sess.run(tf.global_variables_initializer())

for epoch in range(25):
    avg_cost = 0.

    total_batch = int(mnist.train.num_examples / 100)
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs, y: batch_ys})
        avg_cost += c / total_batch

    print("Epoch:", '%04d' % (epoch + 1), "cost=", "{:.9f}".format(avg_cost))

print("최적화 완료")

correct_prediction = tf.equal(tf.argmax(y_model, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("Accuracy:", sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))

# 모델 파라미터 저장
# 학습 된 결과의 파일의 경로(모델 파라미터를 저장할 경로와 파일 이름)
model_path = "/tmp/model.saved"
saver = tf.train.Saver()

save_path = saver.save(sess, model_path)
print("Model saved in file: %s" % save_path)

sess.close()
