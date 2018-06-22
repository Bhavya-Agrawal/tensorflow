#!/usr/bin/python3

import tensorflow as tf

# taking 2 constant values
x = tf.constant([5])
y = tf.constant([6])

# adding the above 2 nos using tensorflow
z = tf.add(x,y)

# creating session for processing and visualising tensor
session = tf.Session()

# maintaing a session for the output and then closing it automatically after the work is done using "with" statement
with tf.Session() as session:

	# for visualising the work graphically storing the graph in a directory that is not already present in the pwd like(tensor_graphs) and using method called graph of  instance of session and run this via tensorboard
	tf.summary.FileWriter('tensor_graphs',session.graph)

	# for printing the output value
	print(session.run(z))