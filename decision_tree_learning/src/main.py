import src.decisionTree as dt
import matplotlib.pyplot as plt


def run():
    learning_dim = [i for i in range(1, 101)]
    success_rate = []
    data = dt.LoadData()
    for dim in learning_dim:
        my_learning_set, my_test_set = dt.SplitData(data, dim)
        tree = dt.BuildTree(my_learning_set)
        success_rate.append(dt.TestData(my_test_set, tree))
    plt.plot(learning_dim, success_rate)
    plt.axis([0, 100, 0, 100])
    plt.xlabel('Dimension of learning set')
    plt.ylabel('Success rate')
    plt.savefig('success_rate.png')
    plt.show()
    best_percentage = learning_dim[success_rate.index(max(success_rate))]
    print(f"Best fitting: {str(best_percentage)}, success: {str(max(success_rate))}")
    my_learning_set, my_test_set = dt.SplitData(data, best_percentage)
    tree = dt.BuildTree(my_learning_set)
    dt.DrawTree(tree)
    print(dt.ReprTree(tree))


if __name__ == '__main__':
    run()
