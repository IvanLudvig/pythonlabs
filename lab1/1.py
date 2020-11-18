import matplotlib.pyplot as plt

for i in range(1, 6):
    X=[]
    Y=[]
    with open('dead_moroz/00{}.dat'.format(i)) as f:
        N = int(next(f))
        for k in range(N):
            x, y = [float(x) for x in next(f).split()]
            X.append(x)
            Y.append(y)
    f.close()

    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.scatter(X, Y)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Number of points: {}'.format(N))
    plt.show()

    fig.savefig('plot1/00{}.png'.format(i))
    plt.close()
