import matplotlib.pyplot as plt
from scipy.stats import binom

n = 4  # количество испытаний
p = 0.1  # вероятность успеха в одном испытании

x = list(range(n+1))  # значения k: 0, 1, ..., n
y = [binom.pmf(k, n, p) for k in x]  # вероятности для каждого k

plt.bar(x, y)
plt.title('Биномиальное распределение')
plt.xlabel('Количество нестандартных деталей (k)')
plt.ylabel('Вероятность P(X=k)')
plt.show()
