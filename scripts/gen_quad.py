import random
import itertools


def gen_quad(age2row, age_margin):
    result = []
    print('len(ages):', len(age2row.keys()))
    for age, fn_list in age2row.items():
        pos_items = tuple(itertools.combinations(fn_list, 2))
        pos_items = random.sample(pos_items, min(len(pos_items), 100))
        if len(pos_items) == 0:
            continue
        negs_1 = []
        negs_2 = []
        for neg_age, neg_fn_list in age2row.items():
            distance = int(neg_age) - int(age)
            if distance == 0:
                continue
            elif distance < 0 and distance >= -age_margin:
                negs_1.append(random.choice(neg_fn_list))
            elif distance > 0 and distance <= age_margin:
                negs_2.append(random.choice(neg_fn_list))
        if len(negs_1) == 0 or len(negs_2) == 0:
            continue
        neg_items = ((random.choice(negs_1), random.choice(negs_2)), )
        result.append(itertools.product(pos_items, neg_items))
    return result


def parse_age2row(fn):
    age2row = {}
    with open(fn, 'r', encoding='utf-8') as fp:
        for row in fp.readlines():
            cols = row.strip().split(' ')
            if cols[1] not in age2row:
                age2row[cols[1]] = []
            age2row[cols[1]].append(row.strip())
    return age2row


def save_quad(fn, quads):
    with open(fn, 'w', encoding='utf-8') as fp:
        for quad in quads:
            for pair in quad:
                for x, y in pair:
                    fp.write(x + '\n')
                    fp.write(y + '\n')


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        type=str,
        help='input list file name with format: %(image_file_name)s\t%(age)d',
    )
    parser.add_argument(
        '--output',
        type=str,
        help='output list file name',
    )
    parser.add_argument(
        '--age-margin',
        metavar='age_margin',
        type=int,
        default=5,
        help='age margin to generate quad',
    )

    options = parser.parse_args()
    age2row = parse_age2row(options.input)
    quads = gen_quad(age2row, options.age_margin)
    save_quad(options.output, quads)


if __name__ == '__main__':
    main()
