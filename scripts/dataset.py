import os
import random
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
    fmt_train_set_file = 'train_set.txt'
    fmt_train_file = 'train_list.txt'
    fmt_test_set_file = 'test_set.txt'
    fmt_test_file = 'test_list.txt'
    fmt_proto_train_file = 'train_proto.txt'
    fmt_proto_test_file = 'test_proto.txt'

    @staticmethod
    def get_arg_parser():
        import argparse
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--dataset',
            type=str,
            default='FGNET',
            help='dataset name',
        )
        parser.add_argument(
            '--ratio',
            type=float,
            default=0.9,
            help='train/test ratio',
        )
        parser.add_argument(
            '--fgnet-test-id',
            type=str,
            default=None,
            help='to specify a test id for fgnet',
        )
        parser.add_argument(
            '--morph-round',
            type=int,
            default=-1,
            help=
            'morph round to generate quad, if it is -1, force to re-split list',
        )
        parser.add_argument(
            '--age-margin',
            metavar='age_margin',
            type=int,
            default=5,
            help='age margin to generate quad',
        )
        return parser

    @staticmethod
    def run():
        parser = BaseDataset.get_arg_parser()
        options = parser.parse_args()
        dataset = options.dataset
        options.ratio = float(options.ratio)

        class_ = None
        for c in BaseDataset.__subclasses__():
            if c.name == dataset:
                class_ = c
                break
        if class_ is None:
            print("There is no such dataset %s" % dataset)
            return

        class_(options)

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
        self._fmt_values()

        if not os.path.exists(self.list_file):
            self._fetch_list_file()

        self._fetch_stage_set_file(options)
        self._fetch_stage_list_file(options)
        self._fetch_proto_file()

    def _fmt_values(self):
        self.train_file = data(self.name, self._fmt(self.fmt_train_file))
        self.train_set_file = data(self.name,
                                   self._fmt(self.fmt_train_set_file))
        self.test_file = data(self.name, self._fmt(self.fmt_test_file))
        self.test_set_file = data(self.name, self._fmt(self.fmt_test_set_file))
        self.train_proto_file = data(self.name,
                                     self._fmt(self.fmt_proto_train_file))
        self.test_proto_file = data(self.name,
                                    self._fmt(self.fmt_proto_test_file))

    def _fetch_list_file(self):
        raise NotImplementedError()

    def _fetch_stage_set_file(self, options):
        rows = []
        with open(self.list_file, 'r', encoding='utf-8') as fp:
            for row in fp.readlines():
                rows.append(row.strip())
        print('generate %s' % self.train_set_file)
        print('generate %s' % self.test_set_file)
        train_set = random.sample(rows, int(len(rows) * options.ratio))
        train_set_fp = open(self.train_set_file, 'w', encoding='utf-8')
        test_set_fp = open(self.test_set_file, 'w', encoding='utf-8')
        for row in rows:
            if row in train_set:
                train_set_fp.write(row + '\n')
            else:
                test_set_fp.write(row + '\n')

    def _fetch_stage_list_file(self, options):
        from gen_quad import gen_quad, save_quad, parse_age2row
        age2row = parse_age2row(self.train_set_file)
        quads = gen_quad(age2row, options.age_margin)
        save_quad(self.train_file, quads)
        with open(self.test_set_file, 'r', encoding='utf-8') as fp:
            with open(self.test_file, 'w', encoding='utf-8') as test_fp:
                for row in fp.readlines():
                    test_fp.write(row.strip() + '\n')

    def _fetch_proto_file(self):
        print('generate %s' % self.train_proto_file)
        with open(self.train_proto_file, 'w', encoding='utf-8') as fp:
            fp.write(self._fmt(TMPL_TRAIN_PROTO))
        print('generate %s' % self.test_proto_file)
        with open(self.test_proto_file, 'w', encoding='utf-8') as fp:
            fp.write(self._fmt(TMPL_TEST_PROTO))


class FGNET(BaseDataset):
    name = 'FGNET'
    image_subdir = 'margin_crop_FGNET'

    def _fetch_list_file(self):
        fp = open(self.list_file, 'w', encoding='utf-8')
        for f in os.listdir(self.image_root):
            name = f
            age = int(name[4:6])
            fp.write('%(name)s\t%(age)d\n' % locals())
        fp.close()

    def _fetch_stage_set_file(self, options):
        id2file = {}
        with open(self.list_file, 'r', encoding='utf-8') as fp:
            for row in fp.readlines():
                fid = row[:3]  # len('001')
                if fid not in id2file:
                    id2file[fid] = []
                id2file[fid].append(row)
        print('generate %s' % self.train_set_file)
        print('generate %s' % self.test_set_file)
        train_set_fp = open(self.train_set_file, 'w', encoding='utf-8')
        test_set_fp = open(self.test_set_file, 'w', encoding='utf-8')
        if options.fgnet_test_id != None:
            selected_fid = options.fgnet_test_id
        else:
            selected_fid = random.choice(list(id2file.keys()))
        print('select "%s" as test set' % selected_fid)
        selected_used = False
        for fid, rows in id2file.items():
            for row in rows:
                if fid != selected_fid:
                    train_set_fp.write(row)
                else:
                    test_set_fp.write(row)
                    selected_used = True
        if not selected_used:
            print('WARNING: there is no such id %s for test' % selected_fid)
        train_set_fp.close()
        test_set_fp.close()


class MORPH(BaseDataset):
    name = 'MORPH'
    image_subdir = 'margin_crop_MORPH'
    fmt_split_file = 'split/%(round)d.txt'
    fmt_train_set_file = 'train_set_%(round)d.txt'
    fmt_train_file = 'train_list_%(round)d.txt'
    fmt_test_set_file = 'test_set_%(round)d.txt'
    fmt_test_file = 'test_list_%(round)d.txt'
    fmt_proto_train_file = 'train_proto_%(round)d.txt'
    fmt_proto_test_file = 'test_proto_%(round)d.txt'

    def __init__(self, options):
        self.round = options.morph_round
        super().__init__(options)

    def _split_list_file(self):
        tester = os.path.dirname(
            data(self.name, self._fmt(self.fmt_split_file)))
        if not os.path.exists(tester):
            os.makedirs(tester)

        rows = []
        with open(self.list_file, 'r', encoding='utf-8') as fp:
            for row in fp.readlines():
                rows.append(row.strip())
        random.shuffle(rows)

        step = int(len(rows) / 10)
        for i in range(0, 10):
            self.round = i
            fn = data(self.name, self._fmt(self.fmt_split_file))
            with open(fn, 'w', encoding='utf-8') as fp:
                subset = rows[i:i + step]
                for row in subset:
                    fp.write(row + '\n')

    def _fetch_list_file(self):
        fp = open(self.list_file, 'w', encoding='utf-8')
        with open(dataset(self.name, 'list.txt'), 'r', encoding='utf-8') as i:
            for row in i.readlines():
                cols = row.strip().split(' ')
                fp.write("%s\t%s\n" % tuple(cols))
        fp.close()

    def _fetch_stage_set_file(self, options):
        if self.round is None or self.round == -1:
            print('split list file')
            self._split_list_file()
            self.round = 0
            self._fmt_values()  # update files name

        print('Start generating round(%d) set files' % self.round)
        print('generate %s' % self.train_set_file)
        print('generate %s' % self.test_set_file)

        train_set_fp = open(self.train_set_file, 'w', encoding='utf-8')
        test_set_fp = open(self.test_set_file, 'w', encoding='utf-8')

        for i in range(10):
            splited_fn = data(self.name, self._fmt(self.fmt_split_file))
            if i == self.round:
                with open(splited_fn, 'r', encoding='utf-8') as fp:
                    test_set_fp.write(fp.read())
            else:
                with open(splited_fn, 'r', encoding='utf-8') as fp:
                    train_set_fp.write(fp.read())


if __name__ == '__main__':
    BaseDataset.run()
