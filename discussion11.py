import pandas as pd
import matplotlib.pyplot as plt


def disc11():
    df = pd.read_csv('StudentPerformanceFactors.csv')
    print(df['Distance_from_Home'])

    distance = df['Distance_from_Home'].head(12)
    performance = df['Exam_Score'].head(12)

    fig = plt.figure(figsize=(10, 7))
    plt.yticks(range(0, 100, 5))

    plt.bar(distance, performance)


def disc12():
    measurements = [5.1, 4.9, 5.0, 5.2, 5.3, 4.8, 5.4, 5.0, 4.9, 5.1, 5.2, 5.3, 5.4, 5.5, 5.2, 5.1, 4.8, 5.0, 5.1, 5.3]

    num_bins = len(set(measurements))

    counts, bin_edges, _ = plt.hist(measurements, bins=num_bins, edgecolor='black', alpha=0.7)

    plt.xticks(bin_edges, rotation=45)
    plt.yticks(range(0, 5, 1))

    plt.title("Measurements of leaves")
    plt.xlabel("Length, cm", labelpad=12)
    plt.ylabel("Frequency", labelpad=12)

    plt.tight_layout()
    plt.show()


disc12()
