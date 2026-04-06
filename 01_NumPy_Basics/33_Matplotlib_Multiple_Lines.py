import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
python_scores = [85, 90, 88, 95]
ds_scores = [70, 75, 82, 89]

plt.plot(x, python_scores, label='Python')
plt.plot(x, ds_scores, label='Data Science')

plt.legend() # Shows which color belongs to which subject
plt.show()
