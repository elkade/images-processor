import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_float, exposure


def get_hist_plot(img, ax_hist):
    image = img_as_float(img)

    ax_cdf = ax_hist.twinx()

    # Display histogram
    ax_hist.hist(image.ravel(), bins=256, histtype='step', color='black')
    ax_hist.ticklabel_format(axis='y', scilimits=(0, 0))
    ax_hist.set_xlim(0, 1)
    ax_hist.set_yticks([])

    # Display cumulative distribution
    img_cdf, bins = exposure.cumulative_distribution(image, 256)
    ax_cdf.plot(bins, img_cdf, 'r')
    ax_cdf.set_yticks([])

    y_min, y_max = ax_hist.get_ylim()
    ax_hist.set_yticks(np.linspace(0, y_max, 5))
