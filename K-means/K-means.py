import numpy as np
import random
import matplotlib.pyplot as plt


# arr中距离k_arr最远的元素，用于初始化聚类中心
def farthest(Cen, dataset):
    f = Cen
    max_d = 0
    for data in dataset:
        d = 0
        for i in range(len(Cen)):
            d = d + np.sqrt(np.sum(np.square(data - Cen)))
        if d > max_d:
            max_d = d
            f = data
    return f


if __name__ == '__main__':
    # 生成随机坐标作为数据库
    dataset = np.random.randint(100, size=(100, 2))

    # 初始化聚类中心数
    m = 5
    index = random.sample(range(len(dataset)), m)
    Cen = dataset[index]

    # 初始化聚类容器，用于存放每一类中的数据点
    cla_arr = []
    for i in range(m):
        cla_arr.append([])

    # 迭代聚类,n为迭代次数
    n = 20
    for i in range(n):  # 迭代n次
        for data in dataset:  # 把集合里每一个元素聚到最近的类
            Ci = 0  # 假定距离第一个中心最近
            min_d = np.sqrt(np.sum(np.square(data - Cen[Ci])))
            for j in range(1, len(Cen)):
                dis = np.sqrt(np.sum(np.square(data - Cen[j])))
                if dis <= min_d:  # 找到更近的聚类中心
                    min_d = dis
                    Ci = j
            cla_arr[Ci].append(data)

        # 迭代更新聚类中心
        for k in range(len(Cen)):
            if n - 1 == i:
                break
            Cen[k] = np.mean(cla_arr[k], axis=0)
            cla_arr[k] = []

    # 可视化展示
    col = ['HotPink', 'Aqua', 'red', 'yellow', 'LightSalmon']
    for i in range(m):
        plt.scatter(Cen[i][0], Cen[i][1], linewidth=10, color=col[i])
        plt.scatter([e[0] for e in cla_arr[i]], [e[1] for e in cla_arr[i]], color=col[i])
    plt.show()

    print()
