import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

sess = tf.InteractiveSession()


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1,shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding="SAME")


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")


n_input = 784
n_output = 10


x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])
x_image = tf.reshape(x, [-1, 28, 28, 1])


W_conv1 = weight_variable([5, 5, 1, 30])
b_conv1 = bias_variable([30])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)


W_conv2 = weight_variable([5, 5, 30, 15])
b_conv2 = bias_variable([15])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)


W_conv3 = weight_variable([3, 3, 15, 64])
b_conv3 = bias_variable([64])
h_conv3 = tf.nn.relu(conv2d(h_conv2, W_conv3) + b_conv3)
h_pool3 = max_pool_2x2(h_conv3)

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_pool3_flat = tf.reshape(h_pool3, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool3_flat, W_fc1) + b_fc1)


keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)


W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
pred = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

loss = tf.reduce_mean(-tf.reduce_sum(y * tf.log(pred), reduction_indices=[1]))
# loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y,logits=pred)

optimizer = tf.train.AdamOptimizer(0.001).minimize(loss)

accuracy = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
acc = tf.reduce_mean(tf.cast(accuracy, tf.float32))

tf.global_variables_initializer().run()

training_epochs = 8000
batch_size = 100
display_step = 2
list_for_result = []

for i in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)
    batch = mnist.train.next_batch(batch_size)
    optimizer.run(feed_dict={x: batch[0], y: batch[1], keep_prob: 0.4})
    avg_cost += sess.run(loss,
                         feed_dict={x: batch[0], y: batch[1], keep_prob: 1.0}) / total_batch
    if i % display_step == 0:
        train_accuracy = acc.eval(
            feed_dict={x: batch[0], y: batch[1], keep_prob: 1.0})
        test_accuracy = acc.eval(
            feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0})
        print("step: %d  cost: %.9f TRAIN ACCURACY: %.5f TEST ACCURACY: %.5f" %
              (i, avg_cost, train_accuracy, test_accuracy))
    list_for_result.append(test_accuracy)
a=max(list_for_result)
print("THE BEST SCORE IS: %.5f AND %.5f" % (a,1-a))