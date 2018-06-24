#
from collections import Counter
from matplotlib import pyplot as plt


num_friends = [
    45, 10, 102, 56, 38, 13, 67, 55, 56, 38, 67, 55, 102, 13, 67, 55, 10, 10,
    13, 67, 55, 102, 56, 38, 67, 55, 102, 13, 67, 55, 102, 56, 38, 67, 55, 67,
    45, 10, 102, 56, 38, 13, 67, 55, 45, 10, 102, 56, 38, 13, 67, 55, 13, 10,
    55, 102, 56, 38, 67, 38, 67, 55, 10, 102, 56, 45, 10, 102, 56, 38, 13, 55
]


def mean(x):
    return sum(x) / len(x)


if __name__ == "__main__":

    c = Counter(num_friends)
    xs = [x for x in num_friends]
    ys = [c[x] for x in num_friends]

    print("mean: {0}".format(mean(num_friends)))

    plt.bar(xs, ys)
    plt.axis([0, 103, 0, 15])
    plt.show()
