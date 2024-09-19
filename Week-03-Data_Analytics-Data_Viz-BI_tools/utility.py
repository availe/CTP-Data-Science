import matplotlib.pyplot as plt

def custom_bar_plot(data, title):
    data.head(10).plot.barh(x="neighbourhood", y="price")
    plt.title(title)
    plt.xlabel('Mean house price (in thousands of dollars)')
    plt.ylabel('Neighbourhood')
    plt.gca().invert_yaxis()
