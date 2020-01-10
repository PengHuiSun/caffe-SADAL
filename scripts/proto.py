TMPL_TRAIN_PROTO = '''layer {
	name: "data"
	type: "ImageData"
	top: "data"
	top: "label"

	include {
		phase: TRAIN
	}

	image_data_param {
		source: "%(train_file)s"
		root_folder: "%(image_root)s"
		batch_size: 16
		new_height: 224
		new_width: 224
	}
}
layer {
  bottom: "data"
  top: "conv1_1"
  name: "conv1_1"
  type: "Convolution"
  convolution_param {
    num_output: 64
    pad: 1
    kernel_size: 3
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
      value: 0.2
    }
  }
  param {
    lr_mult: 1
    decay_mult: 1
  }
  param {
    lr_mult: 2
    decay_mult: 0
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
  top: "fc8"
  name: "fc8"
  type: "InnerProduct"
  inner_product_param {
    num_output: 2622
  }
}

layer {
  bottom: "fc8"
  top: "prob"
  name: "prob"
  type: "Sigmoid"
 }

layer {
  bottom: "prob"
  top: "dim_down"
  name: "dim_down"
  type: "InnerProduct"
  inner_product_param {
    num_output: 360
    weight_filler { type: "gaussian" std: 0.01}
    bias_filler { type: "constant" value: 0 }
  }
}

layer {
  bottom: "dim_down"
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
    num_output: 360
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
    num_output: 720
    weight_filler { type: "gaussian" std: 0.01}
    bias_filler { type: "constant" value: 0 }
  }
}

layer {
  bottom: "my_FC_2"
  top: "my_FC_3"
  name: "my_FC_3"
  type: "InnerProduct"
  inner_product_param {
    num_output: 360
    weight_filler { type: "gaussian" std: 0.01}
    bias_filler { type: "constant" value: 0 }
  }
}

layer {
  bottom: "my_FC_3"
  top: "gen_output"
  name: "gen_output"
  type: "Sigmoid"
}

layer {
  bottom: "dim_down"
  bottom: "gen_output"
  bottom: "label"
  top: "gen_loss"
  name: "gen_loss"
  type: "GeneratorLoss"
}

layer {
  bottom: "dim_down"
  bottom: "gen_output"
  top: "quad_merge"
  name: "quad_merge"
  type: "QuadMerge"
}

layer {
  bottom: "quad_merge"
  top: "merge"
  name: "merge"
  type: "InnerProduct"
  inner_product_param {
    num_output: 360
    weight_filler { type: "gaussian" std: 0.01}
    bias_filler { type: "constant" value: 0 }
  }
}

layer {
  bottom: "merge"
  top: "merge_2"
  name: "merge_2"
  type: "Sigmoid"
}

layer {
  bottom: "merge_2"
  bottom: "label"
  top: "sun_loss"
  name: "sun_loss"
  type: "SunPengHuiLoss"

  loss_param {
    normalization: NONE
  }
}
'''

TMPL_TEST_PROTO = '''
'''