import caffe
caffe.set_device(0)
caffe.set_mode_gpu()
solver = caffe.SGDSolver('/home/zsy/DeepLearning/caffe/examples/mnist/lenet_solver.prototxt')
