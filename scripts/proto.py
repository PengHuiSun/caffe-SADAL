TMPL_TRAIN_PROTO = '''name: "VGG_ILSVRC_16_layers"
layer {
  name: "data"
  type: "ImageData"
  top: "data"
  top: "label"

  include {
    phase: TRAIN
  }
  transform_param {
      mirror: true
    crop_size: 224
  }
  image_data_param {
    source: "%(train_file)s"
    root_folder: "%(image_root)s"
    batch_size: 64
    new_height: 256
    new_width: 256
  }
}
layer {
  name: "data"
  type: "ImageData"
  top: "data"
  top: "label"

  include {
    phase: TEST
  }
  transform_param {
      mirror: false
    crop_size: 224
  }
  image_data_param {
    source: "%(test_file)s"
    root_folder: "%(image_root)s"
    batch_size: 1
    new_height: 256
    new_width: 256
  }
}
layer {
  bottom: "data"
  top: "conv1_1"
  name: "conv1_1"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 64
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv1_1"
  top: "conv1_1"
  name: "relu1_1"
  type: "ReLU"
}
layer {
  bottom: "conv1_1"
  top: "conv1_2"
  name: "conv1_2"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 64
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv1_2"
  top: "conv1_2"
  name: "relu1_2"
  type: "ReLU"
}
layer {
  bottom: "conv1_2"
  top: "pool1"
  name: "pool1"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool1"
  top: "conv2_1"
  name: "conv2_1"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 128
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv2_1"
  top: "conv2_1"
  name: "relu2_1"
  type: "ReLU"
}
layer {
  bottom: "conv2_1"
  top: "conv2_2"
  name: "conv2_2"

 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 128
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv2_2"
  top: "conv2_2"
  name: "relu2_2"
  type: "ReLU"
}
layer {
  bottom: "conv2_2"
  top: "pool2"
  name: "pool2"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool2"
  top: "conv3_1"
  name: "conv3_1"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 256
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv3_1"
  top: "conv3_1"
  name: "relu3_1"
  type: "ReLU"
}
layer {
  bottom: "conv3_1"
  top: "conv3_2"
  name: "conv3_2"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 256
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv3_2"
  top: "conv3_2"
  name: "relu3_2"
  type: "ReLU"
}
layer {
  bottom: "conv3_2"
  top: "conv3_3"
  name: "conv3_3"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 256
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv3_3"
  top: "conv3_3"
  name: "relu3_3"
  type: "ReLU"
}
layer {
  bottom: "conv3_3"
  top: "pool3"
  name: "pool3"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool3"
  top: "conv4_1"
  name: "conv4_1"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }

  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv4_1"
  top: "conv4_1"
  name: "relu4_1"
  type: "ReLU"
}
layer {
  bottom: "conv4_1"
  top: "conv4_2"
  name: "conv4_2"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv4_2"
  top: "conv4_2"
  name: "relu4_2"
  type: "ReLU"
}
layer {
  bottom: "conv4_2"
  top: "conv4_3"
  name: "conv4_3"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }

  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv4_3"
  top: "conv4_3"
  name: "relu4_3"
  type: "ReLU"
}
layer {
  bottom: "conv4_3"
  top: "pool4"
  name: "pool4"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool4"
  top: "conv5_1"
  name: "conv5_1"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }

  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv5_1"
  top: "conv5_1"
  name: "relu5_1"
  type: "ReLU"
}
layer {
  bottom: "conv5_1"
  top: "conv5_2"
  name: "conv5_2"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv5_2"
  top: "conv5_2"
  name: "relu5_2"
  type: "ReLU"
}
layer {
  bottom: "conv5_2"
  top: "conv5_3"
  name: "conv5_3"
  type: "Convolution"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv5_3"
  top: "conv5_3"
  name: "relu5_3"
  type: "ReLU"
}
layer {
  bottom: "conv5_3"
  top: "pool5"
  name: "pool5"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool5"
  top: "fc6"
  name: "fc6"
 param {
    lr_mult: 10
    decay_mult: 1
  }
  param {
    lr_mult: 20
    decay_mult: 0
  }
  type: "InnerProduct"
  inner_product_param {
    num_output: 4096
  }
}
layer {
  bottom: "fc6"
  top: "fc6"
  name: "relu6"
  type: "ReLU"
}
layer {
  bottom: "fc6"
  top: "fc6"
  name: "drop6"
  type: "Dropout"
  dropout_param {
    dropout_ratio: 0.5
  }
}
layer {
  bottom: "fc6"
  top: "fc7"
  name: "fc7"
 param {
    lr_mult: 10
    decay_mult: 1
  }
  param {
    lr_mult: 20
    decay_mult: 0
  }
  type: "InnerProduct"
  inner_product_param {
    num_output: 4096
  }
}
layer {
  bottom: "fc7"
  top: "fc7"
  name: "relu7"
  type: "ReLU"
}
layer {
  bottom: "fc7"
  top: "fc7"
  name: "drop7"
  type: "Dropout"
  dropout_param {
    dropout_ratio: 0.5
  }
}
layer {
  bottom: "fc7"
  top: "quad_expand"
  name: "quad_expand"
  type: "QuadExpand"
}
layer {
  bottom: "quad_expand"
  top: "my_FC_1"
  name: "my_FC_1"
  type: "InnerProduct"
  inner_product_param {
    num_output: 4096
    weight_filler { type: "gaussian" std: 0.01}
    bias_filler { type: "constant" value: 0 }
  }
}
layer {
  bottom: "my_FC_1"
  top: "my_FC_2"
  name: "my_FC_2"
  type: "InnerProduct"
  inner_product_param {
    num_output: 4096
    weight_filler { type: "gaussian" std: 0.01}
    bias_filler { type: "constant" value: 0 }
  }
}
layer {
  bottom: "fc7"
  bottom: "my_FC_2"
  bottom: "label"
  top: "gen_loss"
  name: "gen_loss"
  type: "GeneratorLoss"
}
layer {
  bottom: "fc7"
  bottom: "my_FC_2"
  top: "quad_merge"
  name: "quad_merge"
  type: "QuadMerge"
}
layer {
  bottom: "quad_merge"
  top: "quadruplet_fc"
  name: "quadruplet_fc"
  type: "InnerProduct"
  inner_product_param {
    num_output: 4096
    weight_filler { type: "gaussian" std: 0.01}
    bias_filler { type: "constant" value: 0 }
  }
}
layer {
  bottom: "quadruplet_fc"
  bottom: "label"
  top: "quadruplet_loss"
  name: "quadruplet_loss"
  type: "QuadrupletLoss"

  loss_param {
    normalization: NONE
  }
}
'''

TMPL_TEST_PROTO = '''name: "VGG_ILSVRC_16_layers"
layer {
	name: "data"
	type: "ImageData"
	top: "data"
	top: "label"
	include {
		phase: TRAIN
	}
	transform_param {
    	mirror: true
		crop_size: 224
	}	
    image_data_param {
		source: "%(test_file)s"
		root_folder: "%(image_root)s"
		batch_size: 64
		new_height: 256
		new_width: 256
	}
}
layer {
	name: "data"
	type: "ImageData"
	top: "data"
	top: "label"

	include {
		phase: TEST
	}
	transform_param {
    	mirror: false
		crop_size: 224
	}
	image_data_param {
		source: "%(test_file)s"
		root_folder: "%(image_root)s"
		batch_size: 1
		new_height: 256
		new_width: 256
	}
}

layer {
  bottom: "data"
  top: "conv1_1"
  name: "conv1_1"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 64
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv1_1"
  top: "conv1_1"
  name: "relu1_1"
  type: "ReLU"
}
layer {
  bottom: "conv1_1"
  top: "conv1_2"
  name: "conv1_2"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 64
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv1_2"
  top: "conv1_2"
  name: "relu1_2"
  type: "ReLU"
}
layer {
  bottom: "conv1_2"
  top: "pool1"
  name: "pool1"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool1"
  top: "conv2_1"
  name: "conv2_1"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 128
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv2_1"
  top: "conv2_1"
  name: "relu2_1"
  type: "ReLU"
}
layer {
  bottom: "conv2_1"
  top: "conv2_2"
  name: "conv2_2"

 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 128
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv2_2"
  top: "conv2_2"
  name: "relu2_2"
  type: "ReLU"
}
layer {
  bottom: "conv2_2"
  top: "pool2"
  name: "pool2"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool2"
  top: "conv3_1"
  name: "conv3_1"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 256
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv3_1"
  top: "conv3_1"
  name: "relu3_1"
  type: "ReLU"
}
layer {
  bottom: "conv3_1"
  top: "conv3_2"
  name: "conv3_2"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 256
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv3_2"
  top: "conv3_2"
  name: "relu3_2"
  type: "ReLU"
}
layer {
  bottom: "conv3_2"
  top: "conv3_3"
  name: "conv3_3"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 256
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv3_3"
  top: "conv3_3"
  name: "relu3_3"
  type: "ReLU"
}
layer {
  bottom: "conv3_3"
  top: "pool3"
  name: "pool3"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool3"
  top: "conv4_1"
  name: "conv4_1"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }

  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv4_1"
  top: "conv4_1"
  name: "relu4_1"
  type: "ReLU"
}
layer {
  bottom: "conv4_1"
  top: "conv4_2"
  name: "conv4_2"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv4_2"
  top: "conv4_2"
  name: "relu4_2"
  type: "ReLU"
}
layer {
  bottom: "conv4_2"
  top: "conv4_3"
  name: "conv4_3"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }

  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv4_3"
  top: "conv4_3"
  name: "relu4_3"
  type: "ReLU"
}
layer {
  bottom: "conv4_3"
  top: "pool4"
  name: "pool4"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool4"
  top: "conv5_1"
  name: "conv5_1"
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }

  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv5_1"
  top: "conv5_1"
  name: "relu5_1"
  type: "ReLU"
}
layer {
  bottom: "conv5_1"
  top: "conv5_2"
  name: "conv5_2"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  type: "Convolution"
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv5_2"
  top: "conv5_2"
  name: "relu5_2"
  type: "ReLU"
}
layer {
  bottom: "conv5_2"
  top: "conv5_3"
  name: "conv5_3"
  type: "Convolution"
 param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
  }
  convolution_param {
    num_output: 512
    pad: 1
    kernel_size: 3
  }
}
layer {
  bottom: "conv5_3"
  top: "conv5_3"
  name: "relu5_3"
  type: "ReLU"
}
layer {
  bottom: "conv5_3"
  top: "pool5"
  name: "pool5"
  type: "Pooling"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  bottom: "pool5"
  top: "fc6"
  name: "fc6"
 param {
    lr_mult: 10
    decay_mult: 1
  }
  param {
    lr_mult: 20
    decay_mult: 0
  }
  type: "InnerProduct"
  inner_product_param {
    num_output: 4096
  }
}
layer {
  bottom: "fc6"
  top: "fc6"
  name: "relu6"
  type: "ReLU"
}
layer {
  bottom: "fc6"
  top: "fc6"
  name: "drop6"
  type: "Dropout"
  dropout_param {
    dropout_ratio: 0.5
  }
}
layer {
  bottom: "fc6"
  top: "fc7"
  name: "fc7"
 param {
    lr_mult: 10
    decay_mult: 1
  }
  param {
    lr_mult: 20
    decay_mult: 0
  }
  type: "InnerProduct"
  inner_product_param {
    num_output: 4096
  }
}
layer {
  bottom: "fc7"
  top: "fc7"
  name: "relu7"
  type: "ReLU"
}
layer {
  bottom: "fc7"
  top: "fc7"
  name: "drop7"
  type: "Dropout"
  dropout_param {
    dropout_ratio: 0.5
  }
}
layer {
  bottom: "fc7"
  top: "fc8-101"
  name: "fc8-101"
 param {
    lr_mult: 10
    decay_mult: 1
  }
  param {
    lr_mult: 20
    decay_mult: 0
  }
  type: "InnerProduct"
  inner_product_param {
    num_output: 101
  weight_filler {
      type: "gaussian"
      std: 0.01
    }
    bias_filler {
      type: "constant"
      value: 0
    }
  }
}
layer {
  bottom: "fc8-101"
  bottom: "label"
  name: "loss"
  type: "SoftmaxWithLoss"
  include: { phase: TRAIN }
}

layer {
  name: "prob"
  type: "Softmax"
  bottom: "fc8-101"
  top: "prob"
    include {
    phase: TEST
  }
}
layer {
  name: "accuracy_train_top01"
  type: "Accuracy"
  bottom: "fc8-101"
  bottom: "label"
  top: "accuracy_train_top01"
  include {
    phase: TEST
    stage: "test-on-train"
  }
}

layer {
  name: "accuracy_train_top05"
  type: "Accuracy"
  bottom: "fc8-101"
  bottom: "label"
  top: "accuracy_train_top05"
  accuracy_param {
    top_k: 5
  }
  include {
    phase: TEST
    stage: "test-on-train"
  }
}

layer {
  name: "accuracy_train_top10"
  type: "Accuracy"
  bottom: "fc8-101"
  bottom: "label"
  top: "accuracy_train_top10"
  accuracy_param {
    top_k: 10
  }
  include {
    phase: TEST
    stage: "test-on-train"
  }
}
'''