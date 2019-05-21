from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def kmeans(df, images_path, image_name, title, n_clusters):
    """ Cluster locations using KMeans and make a plot. """

    # make a copy so that initial dataset remains the same
    df_cp = df.copy()

    km = KMeans(n_clusters=n_clusters)
    km.fit(df_cp)
    km.predict(df_cp)
    labels = km.labels_

    LABEL_COLOR_MAP = {0: 'darkturquoise',
                       1: 'plum',
                       2: 'saddlebrown',
                       3: 'greenyellow',
                       4: 'green',
                       5: 'royalblue',
                       6: 'gold',
                       7: 'firebrick',
                       8: 'coral',
                       9: 'darkmagenta'
                       }

    label_color = [LABEL_COLOR_MAP[l] for l in labels]
    # make plot
    plt.scatter(x='Long', y='Lat', c=label_color, data=df_cp)
    plt.title(title)
    plt.savefig(images_path + image_name, bbox_inches="tight")
    plt.close()
