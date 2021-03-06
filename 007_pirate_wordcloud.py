import numpy as np
import matplotlib.pyplot as plt
from os import getcwd, path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS


def generate_wordcloud(wordcloud: WordCloud, mask: [int]):
    """
    Plots a wordcloud to a specific numpy array image
    :param wordcloud: the wordcloud object
    :param mask: the mask (stencil) that creates the specific image
    """
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def main():
    dir = getcwd()

    # Read the whole text
    text = open('lorem_ipsum/pirate_fish.txt').read()

    # read the mask image
    octopus_mask = np.array(Image.open(path.join(dir, "img/lady_octopus.jpg")))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    # generate word cloud
    wc = WordCloud(background_color="white", max_words=1500, mask=octopus_mask,
                   stopwords=stopwords, contour_width=1, contour_color='steelblue')
    wc.generate(text)

    # store to file
    wc.to_file(path.join(dir, "octopus_cloud.jpg"))

    # plot wordcloud
    generate_wordcloud(wc, octopus_mask)


if __name__ == '__main__':
    main()
