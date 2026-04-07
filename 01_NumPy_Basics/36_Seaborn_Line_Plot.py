import seaborn as sns
import matplotlib.pyplot as plt

# 1. Seaborn ka inbuilt dataset load karein (Flight data)
# Isme mahino ke hisab se passengers ki counting hoti hai
flights = sns.load_dataset("flights")

# 2. Plot ki styling set karein
sns.set_theme(style="whitegrid")

# 3. Line Plot banayein
# x-axis par 'year' aur y-axis par 'passengers' dikhayenge
plt.figure(figsize=(10, 6))
sns.lineplot(data=flights, x="year", y="passengers", color="teal", linewidth=2.5)

# 4. Title aur Labels add karein
plt.title("Trend of Air Passengers (1949 - 1960)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Passengers", fontsize=12)

# 5. Graph ko display karein
plt.show()
