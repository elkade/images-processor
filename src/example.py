from skimage import data

from hist_plot import get_hist_plot

if __name__ == 'main':
    plt = get_hist_plot(data.moon())
    plt.show()
