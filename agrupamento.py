import numpy as np
import cv2
import matplotlib.pyplot as plt

# Gerar um conjunto de ados sintetico com 500 pontos em 4 clusters
np.random.seed(42)

# Gerar 125 pontos em cada um dos 4 clusters
cluster1 = np.random.randn(125, 2) + np.array([2, 2])
cluster2 = np.random.randn(125, 2) + np.array([-2, 2])
cluster3 = np.random.randn(125, 2) + np.array([-2, -2])
cluster4 = np.random.randn(125, 2) + np.array([2, -2])

# Concatenar os clusters em um unico conjunto de dados

X = np.concatenate((cluster1, cluster2, cluster3, cluster4), axis = 0)

# Converter os pontos para o tipo float32
X = np.float32(X)

# Executar o algoritmo k-means para agrupamento
k = 4
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
_, labels, centers = cv2.kmeans(X, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Plotar os pontos e os clusters resultantes
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for i in range(k):
  cluster_points = X[labels.flatten() == i]
  plt.scatter(cluster_points[:, 0], centers[:, 1], c = colors[i], label = f'Cluster {i+1}')
  
plt.scatter(centers[:, 0], centers[:, 1], c = 'k', marker = '*', label = 'Centroids')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Analise de Agrupamento')
plt.legend()
plt.show()