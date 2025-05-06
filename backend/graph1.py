import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import classification_report



import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns


def plot_classification_report(report_dict, class_names, title='Classification Metrics per Class'):
    """
    Plots precision, recall, and f1-score for each class using a bar chart.

    Parameters:
    - report_dict: dict from sklearn's classification_report(output_dict=True)
    - class_names: list of class labels (e.g., ['Hate Speech', 'Offensive Language', 'Neither'])
    - title: optional title for the plot
    """
    df = pd.DataFrame(report_dict).transpose()
    metrics = ['precision', 'recall', 'f1-score']

    # Plot only selected class names
    df.loc[class_names, metrics].plot(kind='bar')
    plt.title(title)
    plt.ylabel('Score')
    plt.ylim(0, 1.05)
    plt.xticks(rotation=45)
    plt.legend(loc='lower right')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
