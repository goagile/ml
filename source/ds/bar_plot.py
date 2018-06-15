from matplotlib import pyplot as plt


if __name__ == "__main__":
    ticks = [2008, 2009, 2010, 2011]
    bars = [10, 23, 12, 21]
    plt.bar(ticks, bars)
    plt.title("Годы")
    plt.ylabel("топливо")
    plt.show()
