#ExTensorflow.py

import tensorflow as tf
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
res = sess.run(result)
print('result:',res)