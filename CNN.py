# coding: UTF-8
import tensorflow as tf

#よく使うものは、メソッド化
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
      return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

#MNIST手書き文字のダウンロードとインポート
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

sess = tf.InteractiveSession()#セッション作成

x = tf.placeholder(tf.float32, shape=[None, 784])#入力データ
y_ = tf.placeholder(tf.float32, shape=[None, 10])#教師データ

#レイヤー1
x_image = tf.reshape(x, [-1,28,28,1])#入力データ変形
W_conv1 = weight_variable([5, 5, 1, 16])#重み
b_conv1 = bias_variable([16])#バイアス
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)#畳み込み
h_pool1 = max_pool_2x2(h_conv1)#プーリング

#レイヤー2
W_conv2 = weight_variable([5, 5, 16, 32])#重み
b_conv2 = bias_variable([32])#バイアス
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)#畳み込み
h_pool2 = max_pool_2x2(h_conv2)#プーリング

#レイヤー3
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*32])#テンソルを整形
W_fc1 = weight_variable([7 * 7 * 32, 512])#重み
b_fc1 = bias_variable([512])#バイアス
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)#重みをかけてバイアスを足す
keep_prob = tf.placeholder(tf.float32)#ドロップアウトの率
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)#ドロップアウト

#レイヤー4
W_fc2 = weight_variable([512, 10])#重み
b_fc2 = bias_variable([10])#バイアス
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)#結果


#損失関数の定義
e=0.00000001
cross_entropy = tf.reduce_mean(-(y_ * tf.log(y_conv+e)+(1.0-y_)*tf.log(1.0-y_conv+e)))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

sess.run(tf.global_variables_initializer())#重み・バイアスの初期化

#途中経過と正解率の定義
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))*100.0

#テストデータの取得
test_x, test_y = mnist.test.next_batch(1000)

#ラーニング実行
for i in range(1000):
  batch = mnist.train.next_batch(50)
  if i%100 == 0 or i==1000-1:
    train_accuracy = sess.run(accuracy,{x:batch[0], y_: batch[1], keep_prob: 1.0})
    print("step {0}, {1:3.1f}".format(i,sess.run(accuracy,{x: test_x, y_: test_y, keep_prob: 1.0}))+" %")
  _=sess.run(train_step,{x: batch[0], y_: batch[1], keep_prob: 0.5})

