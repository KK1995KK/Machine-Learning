import numpy as np
import pandas as pd

# Read dataset
# Header refers to which line is head
data = pd.read_csv(r"dataset/iris.arff.csv", header=0)


def printSamples():
    # Return the first 5 rows.
    print(data.head(), "\n")
    # Return the first `n` rows.
    # data.head(n)
    print(data.head(10), "\n")

    # Return the last 5 rows.
    print(data.tail(), "\n")
    # Return the last `n` rows.
    # data.tail(n)
    print(data.tail(10), "\n")

    # Return a random sample of items from an axis of object.
    print(data.sample())
    # Return n random samples of items from an axis of object.
    # data.sample(n)
    print(data.sample(10))


def mapLeraning():
    data["class"] = data["class"].map({"Iris-virginica": 0})
    data["class"] = data["class"].map({"Iris-setosa": 0})


if __name__ == "__main__":
    printSamples()
    print("t")
