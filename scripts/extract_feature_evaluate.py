import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# load caffe
import sys
sys.path.insert(0, os.path.join(ROOT_DIR, 'caffe/build/python'))

import caffe
import math
import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

os.environ["CUDA_VISIBLE_DEVICES"] = "1"


def listfile_read(path):
    ret = []
    with open(path, 'r') as fp:
        for line in fp.readlines():
            x = line.strip().split(' ')
            ret.append(tuple(x))
    return ret


def run(options):
    caffe.set_mode_gpu()

    time_start = time.time()
    net = caffe.Net(options.caffe_net, options.caffe_model, caffe.TEST)

    pairs = listfile_read(options.test_list)
    print('pairs: %s' % pairs)
    features_fc7 = []
    features = []
    labels = []

    round = int(math.ceil(len(pairs) * 1.0 / options.batch_size))

    print(len(sys.argv), options.caffe_model, options.mae_result_mat)
    print('Total images count is %d, ' % len(pairs))
    print('  so there are %d round.' % round)
    mae = 0
    N = 0
    err = []
    predict_lable = []
    for i in range(0, round):
        # load the image in the data layer
        # im = caffe.io.load_image(os.path.join(IMAGE_ROOT, filename))
        # net.blobs['data'].data[...] = transformer.preprocess('data', im)

        # print(filename, label)
        # output = net.forward()

        # fc7_data = net.blobs['fc8-101'].data
        # prob_data = output['fc8_101']
        # label_data = output['label']
        output = net.forward()
        label_data = output['label']
        for j in range(0, 1):
            fc7_data = net.blobs['prob'].data[j]
            truth_label = label_data[j]
            prob_max = fc7_data.flat[0]
            # l=0
            # for k in range(0, 101):
            #     if fc7_data.flat[k] > prob_max:
            #         prob_max = fc7_data.flat[k]
            #         l = k
            sum = 0
            for k in range(0, 101):
                sum += k * fc7_data.flat[k]

            err_abs = abs(truth_label - sum)
            print(truth_label)
            print(sum)
            print(err_abs)
            err.append(err_abs)
            predict_lable.append(sum)
            mae = mae + err_abs
            N = N + 1
        mae = mae / N
        time_end = time.time()
        print('time cost', time_end - time_start, 's')
        sio.savemat(options.mae_result_mat, {
            'mae': mae,
            'err': err,
            'predict_label': predict_lable
        })


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--caffe-net',
        type=str,
    )
    parser.add_argument(
        '--caffe-model',
        type=str,
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=1,
    )
    parser.add_argument(
        '--test-list',
        type=str,
    )
    parser.add_argument(
        '--test-img-root',
        type=str,
    )
    parser.add_argument(
        '--mae-result-mat',
        type=str,
    )
    options = parser.parse_args()

    if not os.path.exists(options.test_list):
        print('List %s not found...' % options.test_list)
        exit(1)

    if not os.path.exists(options.caffe_net):
        print('Model %s not found...' % options.caffe_net)
        exit(1)
    if not os.path.exists(options.caffe_model):
        print('Weights %s not found...' % options.caffe_model)
        exit(1)

    run(options)
