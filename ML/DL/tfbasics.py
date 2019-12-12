# As of tensorflow 2.0.0, eager execution has been enabled. That means we don't need sessions to run the computation.
# To disable the eager execution, uncomment the 5, 10 and 11th line.

import tensorflow as tf
# tf.compat.v1.disable_eager_execution()
x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1, x2)
# sess = tf.compat.v1.Session()
# print(sess.run(result))
print(result.numpy())
