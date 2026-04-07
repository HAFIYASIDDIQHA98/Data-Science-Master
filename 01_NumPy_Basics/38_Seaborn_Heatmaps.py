import seaborn as sns
import matplotlib.pyplot as plt

# Flights ka dataset load karke pivot table banayein
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

plt.figure(figsize=(12, 8))

# Heatmap creation
# 'annot=True' se cells ke andar numbers bhi dikhte hain
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")

plt.title("Passenger Traffic Heatmap (Year vs Month)")
plt.show()
