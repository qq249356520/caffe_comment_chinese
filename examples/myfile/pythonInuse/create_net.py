#-*- coding: utf-8 -*-
"""
Spyder Editor
"""

from caffe import layers as L, params as P, to_proto
path = '/home/zsy/DeepLearning/caffe/examples/myfile/pythonInuse/netCreate/'
train_lmdb = path + 'train_db'
val_lmdb = path + 'val_db'
mean_file = path + 'mean.binaryproto'
train_proto = path + 'train.prototxt'
val_proto = path + 'val.prototxt'

train_list = path + 'train.txt'
val_list = path + 'val.txt'

#生成网络
def create_net(img_list, batch_size, include_acc = False):
	#创建第一层：数据层。向上传递两类数据：图片数据和对应的标签
	"""
	data, label = L.Data(source = lmdb, backend = P.Data.LMDB, 
		batch_size = batch_size, ntop = 2, 
		transform_param = dict(crop_size = 40, mean_file = mean_file, mirror = True))
	"""
	data, label = L.ImageData(source = img_list, batch_size = batch_size, 
		new_width = 48, new_height = 48, ntop = 2, 
		transform_param = dict(crop_size = 40, mirror = True))
	#创建第二层：卷积层
	conv1 = L.Convolution(data, kernel_size = 5, stride = 1, 
		num_output = 16, pad = 2, weight_filler = dict(type = 'xavier'))
	#创建激活函数
	relu1 = L.ReLU(conv1, in_place = True)
	#创建池化层
	pool1 = L.Pooling(relu1, pool = P.Pooling.MAX, kernel_size = 3, stride = 2)
	#第三个卷积层
	conv2 = L.Convolution(pool1, kernel_size = 3, stride = 1, 
		num_output = 32, pad = 1, weight_filler = dict(type = 'xavier'))
	relu2 = L.ReLU(conv2, in_place = True)
	pool2 = L.Pooling(relu2, pool = P.Pooling.MAX, kernel_size = 3, stride = 2)
	#创建一个全连接层
	fc3 = L.InnerProduct(pool2, num_output = 1024, weight_filler = dict(type = 'xavier'))
	relu3 = L.ReLU(fc3, in_place = True)
	#创建一个dropout层
	drop3 = L.Dropout(relu3, in_place = True)
	fc4 = L.InnerProduct(drop3, num_output =  10, weight_filler = dict(type = 'xavier'))
	#创建softmax层
	loss = L.SoftmaxWithLoss(fc4, label)

	if include_acc:     #训练阶段不需要accuracy层，但是在验证阶段需要
		acc = L.Accuracy(fc4, label)
		return to_proto(loss, acc)
	else:
		return to_proto(loss)

def write_net():
	#将以上的设置写入prototxt
	with open(train_proto, 'w') as f:
		f.write(str(create_net(train_list, batch_size = 64)))

	#写入配置文件
	with open(val_proto, 'w') as f:
		f.write(str(create_net(val_list, batch_size = 32, include_acc = True)))

if __name__ == '__main__':
	write_net()



