import matplotlib.pyplot as plt

def visualize(grid, path, start, goal):
    plt.imshow(grid, cmap='gray')

    x, y = zip(*path)
    plt.plot(y, x, color='blue')

    plt.scatter(start[1], start[0], color='green', label="Start")
    plt.scatter(goal[1], goal[0], color='red', label="Goal")

    plt.legend()
    plt.title("Autonomous Navigation Path")
    plt.show()