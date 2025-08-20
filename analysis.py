import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "RetentionRate": [68.93, 73.34, 70.62, 78.60]
}
industry_target = 85

# Create DataFrame
df = pd.DataFrame(data)
df["Target"] = industry_target

# Calculate Average
average_rate = df["RetentionRate"].mean()
print(f"Average Retention Rate: {average_rate:.2f}")  # Should print 72.87

# Plot trend
plt.figure(figsize=(8,5))
plt.plot(df["Quarter"], df["RetentionRate"], marker="o", label="Company Retention Rate")
plt.axhline(industry_target, color="red", linestyle="--", label=f"Industry Target ({industry_target})")

#Visualisation
plt.title("Customer Retention Rate - 2024")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate (%)")
plt.legend()
plt.grid(True)
plt.savefig("retention_trend.png", dpi=300)
plt.show()
