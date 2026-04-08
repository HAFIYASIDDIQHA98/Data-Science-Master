import seaborn as sns
import matplotlib.pyplot as plt

# Dataset load karein
tips = sns.load_dataset("tips")

# Box plot banayein
sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker", palette="Set3")

plt.title("Bill Distribution by Day & Smoking Status")
plt.show()
