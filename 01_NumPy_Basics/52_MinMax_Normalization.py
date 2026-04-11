from sklearn.preprocessing import MinMaxScaler

# Same data use karte hain
scaler_minmax = MinMaxScaler()
df_normalized = scaler_minmax.fit_transform(df)

print("Normalized Data (Range 0 to 1):\n", df_normalized)
