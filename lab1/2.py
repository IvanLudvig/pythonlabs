import matplotlib.pyplot as plt

framesX = []
framesY = []
with open('frames.dat') as f:
    for i in range(6):
        X = [float(x) for x in next(f).split()]
        Y = [float(x) for x in next(f).split()]
        framesX.append(X)
        framesY.append(Y)
f.close()

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(6, 9))

for i in range(6):
    ax = axes[int(i / 2), int(i % 2)]
    ax.set_xlim([0, 16])
    ax.set_ylim([-9, 12])
    ax.plot(framesX[i], framesY[i])
    ax.title.set_text('Frame {}'.format(i))
    ax.grid()

fig.savefig('frames.png')
plt.show()
