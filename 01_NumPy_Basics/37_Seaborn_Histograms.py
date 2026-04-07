import seaborn as sns
import matplotlib.pyplot as plt

# Penguins ka dataset load karein
penguins = sns.load_dataset("penguins")

plt.figure(figsize=(10, 6))

# Histogram with KDE (Kernel Density Estimate) curve
sns.histplot(data=penguins, x="flipper_length_mm", kde=True, color="purple", bins=30)

plt.title("Distribution of Flipper Length")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")
plt.show()
