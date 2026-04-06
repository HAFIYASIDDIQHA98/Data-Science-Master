import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
study_hours = [2, 3, 5, 4, 6]

plt.plot(days, study_hours)
plt.title("Study Progress")
plt.xlabel("Days")
plt.ylabel("Hours Studied")
plt.show()
