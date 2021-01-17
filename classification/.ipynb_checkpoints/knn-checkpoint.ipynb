{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter\n",
    "import numpy as np\n",
    "\n",
    "class KNN:\n",
    "    \n",
    "    def __init__(self, k=3):\n",
    "        \n",
    "        self.k = k\n",
    "        \n",
    "    def fit(self, X, y):\n",
    "        \n",
    "        self.X_train = X\n",
    "        self.y_train = y\n",
    "        \n",
    "    def predict(self, X):\n",
    "        \n",
    "        predicted_labels = [self._predict(x) for x in X]\n",
    "        return np.array(predicted_labels)\n",
    "        \n",
    "    def _predict(self, x):\n",
    "        \n",
    "        # compute distances\n",
    "        distance = [eucladian_(x, x_train) for x_train in self.X_train]\n",
    "        \n",
    "        #get the k nearest samples, labels\n",
    "        k_indices = np.argsort(distance)[:self.k]\n",
    "        k_nearest_labels = [self.y_train[i] for i in k_indices]\n",
    "        \n",
    "        #majority vote most common labels\n",
    "        most_common = Counter(k_nearest_labels).most_common(1)\n",
    "        return most_common[0][0]\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
