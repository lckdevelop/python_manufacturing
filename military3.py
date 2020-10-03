import tensorflow as tf
import numpy as np
import random

x_source = np.array([[180, 75], [190, 80], [170, 50], [185, 45], [175, 65], [178, 70], [165, 80], [160, 95], [170, 100], [185, 70]])
y_source = np.array([[0, 1], [0, 1], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [0, 1],])

height = 0
weight = 0

test_source = [height, weight]

for i in range(0, 100):
    height = random.randrange(160, 190+1)
    weight = random.randrange(50, 100+1)

    x_source = np.append(x_source, test_source)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_uniform([2, 10], -1., 1.))
W2 = tf.Variable(tf.random_uniform([10, 2], -1., 1.))

b1 = tf.Variable(tf.zeros([10]))
b2 = tf.Variable(tf.zeros([2]))

L1 = tf.add(tf.matmul(X, W1), b1)
L1 = tf.nn.relu(L1)

model = tf.add(tf.matmul(L1, W2), b2)

cost = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=model))

optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(1000):
    sess.run(train_op, feed_dict={X: x_source, Y: y_source})

    if (step + 1) % 10 == 0:
        print(step + 1, sess.run(cost, feed_dict={X: x_source, Y: y_source}))
prediction = tf.argmax(model, 1)
target = tf.argmax(Y, 1)

print('예측:', sess.run(prediction, feed_dict={X: x_source}))
print('결과:', sess.run(target, feed_dict={Y: y_source}))

print('test데이터', test_source)
print('test데이터 예측:', sess.run(prediction, feed_dict={X: test_source}))


is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_source, Y: y_source}))