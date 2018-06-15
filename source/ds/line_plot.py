from matplotlib import pyplot as plt


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 23, 45, 123, 234, 478, 1002, 1566, 2345, 3450]
    plt.plot(x, y, color="green", marker="o", linestyle="solid")
    plt.title("икес")
    plt.ylabel("игрэк")
    plt.show()
