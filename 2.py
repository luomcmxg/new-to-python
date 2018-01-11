import tensorflow as tf
import sys
sess=tf.Session()
a=tf.constant(10)
print(sess.run(a+a),end="")
hello=tf.constant("Hello world!")
print(" ",sess.run(hello).decode('utf-8'))
print(sys.path)
print \
(type(a))