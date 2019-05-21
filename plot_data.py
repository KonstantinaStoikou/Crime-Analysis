import seaborn as sns
import matplotlib.pyplot as plt


def make_plot(ser, xlabel, ylabel, title, path, image_name):
    """ Make a bar plot on the given series. """
    sns.set(style="darkgrid")

    norm = plt.Normalize(0, ser.values.max())
    colors = plt.cm.Blues(norm(ser.values))
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(ser.index, ser.values, palette=colors)
    ax.set(ylabel=ylabel, xlabel=xlabel)
    plt.title(title)
    # save plot to an image
    plt.savefig(path + image_name, bbox_inches="tight")
    plt.close()
