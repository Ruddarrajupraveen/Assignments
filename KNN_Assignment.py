{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The class of test point (2, 4) lies in Class 0\n"
     ]
    }
   ],
   "source": [
    "def ED(dataset, test_point, k):\n",
    "    dist = []\n",
    "    for group in dataset:\n",
    "        for feature in dataset[group]:\n",
    "         # calculating the euclidean distance\n",
    "         euclidean_distance = ((feature[0] - test_point[0]) ** 2 + (feature[1] - test_point[1]) ** 2) ** 0.5\n",
    "      \n",
    "         dist.append((euclidean_distance, group))\n",
    "      \n",
    "   #sorting\n",
    "   \n",
    "    distance = sorted(dist)[:k]\n",
    "   \n",
    "    f1 = 0\n",
    "    f2 = 0\n",
    "   \n",
    "    for i in distance:\n",
    "        if i[1] == 0:\n",
    "            f1 += 1\n",
    "        elif i[1] == 1:\n",
    "            f2 += 1\n",
    "         \n",
    "    if f1 > f2:\n",
    "        return 0\n",
    "    else:\n",
    "        return 1\n",
    "      \n",
    "      \n",
    " # KNN function\n",
    "def knn():\n",
    "    dataset = {0: [(1, 1), (1, 2), (2, 1), (1.8, 1.9), (1, 2), (1.5, 3.5), (1, 5), (2.5, 1), (2, 2.5), (2, 1.5)],\n",
    "              1: [(5, 2.5), (4.5, 5), (5, 6), (5.5, 4), (6, 3), (6, 5), (7, 4), (6.5, 4)]}\n",
    "   \n",
    "   # test point (x,y)\n",
    "    test_point = (2, 4)\n",
    "   \n",
    "   # K value(no of neighbours)\n",
    "    k = 3\n",
    "   \n",
    "    print(\"The class of test point\",test_point, \"lies in Class\",(ED(dataset, test_point, k)))\n",
    "knn()"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
