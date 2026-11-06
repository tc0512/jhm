from pathlib import Path
tmp_dir = str(Path(__file__).resolve().parent)+"/../tmp/"
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
def number_line(x):
    x_max = int(abs(x)) + 1
    x_min = -x_max
    y_max, y_min = 1, -1

    ax = plt.gca()

    # x 轴箭头：从 x_min 指向 x_max，y=0 贴轴
    ax.annotate("", xy=(x_max, 0), xytext=(x_min, 0),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.5,
                                mutation_scale=20),
                annotation_clip=False)

    ax.scatter(x, 0, s=50, c="black")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    plt.savefig(tmp_dir+"numberline.png")
    plt.close()
