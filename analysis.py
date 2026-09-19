import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())


print("\nMissing Values:")
print(df.isnull().sum())

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Sales",
    bins=10,
    kde=False
)

plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig("sales_histogram.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Sales",
    bins=10,
    kde=True
)

plt.title("Sales Distribution with KDE")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig("sales_histogram_kde.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))

sns.kdeplot(
    data=df,
    x="Sales",
    fill=True
)

plt.title("KDE Plot of Sales")
plt.xlabel("Sales")
plt.ylabel("Density")
plt.tight_layout()

plt.savefig("sales_kde.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    y="Sales"
)

plt.title("Boxplot of Sales")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("sales_boxplot.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Region",
    y="Sales"
)

plt.title("Sales Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("region_sales_boxplot.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))

sns.kdeplot(
    data=df,
    x="Sales",
    hue="Region",
    fill=True,
    common_norm=False
)

plt.title("Sales Distribution: Region Comparison")
plt.xlabel("Sales")
plt.ylabel("Density")
plt.tight_layout()

plt.savefig("region_sales_kde.png", dpi=300)
plt.show()

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("\nLower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("\nOutliers:")
print(outliers)

skewness = df["Sales"].skew()

print("\nSales Skewness:", skewness)

if skewness > 0.5:
    print("Interpretation: Sales distribution is positively/right skewed.")
elif skewness < -0.5:
    print("Interpretation: Sales distribution is negatively/left skewed.")
else:
    print("Interpretation: Sales distribution is approximately symmetric.")

sales_range = df["Sales"].max() - df["Sales"].min()
sales_std = df["Sales"].std()

print("\nSales Range:", sales_range)
print("Sales Standard Deviation:", sales_std)

group_stats = df.groupby("Region")["Sales"].agg(
    ["count", "mean", "median", "std", "min", "max"]
)

print("\nRegional Statistics:")
print(group_stats)
group_stats.to_csv("regional_statistics.csv")

print("\nAnalysis completed successfully.")
