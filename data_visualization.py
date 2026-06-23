import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("books_data.csv")

# Clean Price Column
df["Price"] = df["Price"].str.extract(r'(\d+\.\d+)')
df["Price"] = df["Price"].astype(float)

# Style
sns.set_style("whitegrid")

# -------------------------
# 1. Histogram
# -------------------------

plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=10)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.savefig("histogram.png")
plt.show()

# -------------------------
# 2. Box Plot
# -------------------------

plt.figure(figsize=(8,5))
sns.boxplot(y=df["Price"])
plt.title("Book Price Box Plot")
plt.savefig("boxplot.png")
plt.show()

# -------------------------
# 3. Top 10 Expensive Books
# -------------------------

top10 = df.sort_values(by="Price", ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(
    x="Price",
    y="Title",
    data=top10
)

plt.title("Top 10 Most Expensive Books")
plt.tight_layout()
plt.savefig("top10_books.png")
plt.show()

# -------------------------
# 4. Pie Chart
# -------------------------

price_groups = pd.cut(
    df["Price"],
    bins=[0, 20, 40, 60],
    labels=["Low", "Medium", "High"]
)

price_groups.value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Book Price Categories")
plt.ylabel("")
plt.savefig("pie_chart.png")
plt.show()

print("All visualizations created successfully!")