# coding: UTF-8
import tensorflow as tf

#MNIST手書き文字のダウンロードとインポート
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

sess = tf.InteractiveSession()                    #セッション作成

x = tf.placeholder(tf.float32, shape=[None, 784]) #入力データ
y_ = tf.placeholder(tf.float32, shape=[None, 10]) #教師データ
W = tf.Variable(tf.zeros([784,10]))               #重み
b = tf.Variable(tf.zeros([10]))                   #バイアス
sess.run(tf.global_variables_initializer())       #重み・バイアスの初期化
y = tf.nn.softmax(tf.matmul(x,W) + b)             #結果

#損失関数の定義
e=0.00000001
cross_entropy = tf.reduce_mean(-(y_ * tf.log(y+e)+(1.0-y_)*tf.log(1.0-y+e)))

#最適化方法
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#途中経過と正解率の定義
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#テストデータの取得
test_x, test_y = mnist.test.next_batch(1000)

#ラーニング実行
for i in range(1000):
    batch = mnist.train.next_batch(100)
    _ = sess.run(train_step,{x: batch[0], y_: batch[1]})

    if i % 100 == 0 or i==1000-1:
        print("step "+str(i)+", {0:3.1f}".format(sess.run(accuracy,{x: test_x, y_: test_y})*100.0)+" %")