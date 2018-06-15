from matplotlib import pyplot as plt

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [3, 4, 1, 5, 6, 2, 7]
    z = ["a", "b", "c", "d", 'e', 'f', 'g']
    plt.scatter(x, y)
    for x, y, z in zip(x, y, z):
        plt.annotate(z, xy=(x, y), xytext=(5, -15), textcoords="offset points")
    plt.show()
