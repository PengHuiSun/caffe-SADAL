import os
from proto import TMPL_TRAIN_PROTO, TMPL_TEST_PROTO

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(ROOT_DIR, 'dataset')
DATA_DIR = os.path.join(ROOT_DIR, 'data')


def dataset(name_of_dataset, *subdirs):
    if not os.path.exists(DATASET_DIR):
        os.mkdir(DATASET_DIR)
        raise ValueError("Please put some dataset in %s" % DATASET_DIR)

    dataset_root = os.path.join(DATASET_DIR, name_of_dataset)
    if not os.path.exists(dataset_root):
        raise ValueError("There is not such dataset named: %s" %
                         name_of_dataset)
    if len(subdirs) == 0:
        return dataset_root
    return os.path.join(dataset_root, *subdirs)


def data(name_of_dataset, *subdirs):
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
    data_root = os.path.join(DATA_DIR, name_of_dataset)
    if not os.path.exists(data_root):
        os.mkdir(data_root)
    if len(subdirs) == 0:
        return data_root
    return os.path.join(data_root, *subdirs)


class BaseDataset:
    name = None
    image_subdir = ''

    fmt_list_file = 'list.txt'
    fmt_train_file = 'train_list.txt'
    fmt_test_file = 'test_list.txt'
    fmt_proto_train_file = 'train_proto.txt'
    fmt_proto_test_file = 'test_proto.txt'

    @staticmethod
    def get_arg_parser():
        import argparse
        parser = argparse.ArgumentParser()

        parser.add_argument(
            'dataset',
            type=str,
            default='FGNET',
            help='dataset name',
        )

        parser.add_argument(
            'ratio',
            type=float,
            default=0.7,
            help='train/test ratio',
        )
        return parser
    
    @staticmethod
    def run():
        parser = BaseDataset.get_arg_parser()
        options = parser.parse_args()
        dataset = options['dataset']

        class_ = None
        for c in BaseDataset.__subclasses__():
            if c.name == dataset:
                class_ = c
                break
        if class_ is None:
            print("There is no such dataset %s" % dataset)
            return

        class_(dataset)

    
    def _fmt(self, fmt):
        vals = {}
        for k in self.__dir__():
            if not callable(getattr(self, k)):
                vals[k] = getattr(self, k)
        return fmt % vals

    def __init__(self, options):
        self.root = dataset(self.name)
        self.image_root = dataset(self.name, self.image_subdir)
        self.list_file = data(self.name, self._fmt(self.fmt_list_file))
        self.train_file = data(self.name, self._fmt(self.fmt_train_file))
        self.test_file = data(self.name, self._fmt(self.fmt_test_file))
        self.train_proto_file = data(self.name,
                                     self._fmt(self.fmt_proto_train_file))
        self.test_proto_file = data(self.name,
                                    self._fmt(self.fmt_proto_test_file))

        if not os.path.exists(self.list_file):
            self._fetch_list_file()

        self._fetch_stage_list_file(options)
        self._fetch_proto_file()

    def _fetch_list_file(self):
        raise NotImplementedError()

    def _fetch_stage_list_file(self, options):
        pass

    def _fetch_proto_file(self):
        print('generate %s' % self.train_proto_file)
        with open(self.train_proto_file, 'w', encoding='utf-8') as fp:
            fp.write(self._fmt(TMPL_TRAIN_PROTO))
        print('generate %s' % self.test_proto_file)
        with open(self.test_proto_file, 'w', encoding='utf-8') as fp:
            fp.write(self._fmt(TMPL_TEST_PROTO))


class FGNET(BaseDataset):
    name = 'FGNET'
    image_subdir = 'FGNET'

    def _fetch_list_file(self):
        fp = open(self.list_file, 'w', encoding='utf-8')
        for f in os.listdir(self.image_root):
            name = f
            age = int(name[4:6])
            fp.write('%(name)s\t%(age)d\n' % locals())
        fp.close()

class MORPH(BaseDataset):
    name = 'MORPH'
    image_subdir = 'margin_crop_MORPH'

    def _fetch_list_file(self):
        fp = open(self.list_file, 'w', encoding='utf-8')
        with open(dataset(self.name, 'list.txt'), 'r', encoding='utf-8') as i:
            fp.write(i.read())
        fp.close()


if __name__ == '__main__':
    BaseDataset.run()
