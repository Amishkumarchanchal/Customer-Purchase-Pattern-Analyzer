
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: CSV file load karo
try:
    df = pd.read_csv("orders.csv")
    print("CSV file successfully loaded!")

except FileNotFoundError:
    print("Error: orders.csv file nahi mili.")
    print("orders.csv aur main.py same folder mein rakho.")
    raise SystemExit

# Step 2: Required columns check karo
required_columns = ["OrderID", "Month", "Category", "Amount"]

if not all(col in df.columns for col in required_columns):
    print("Error: CSV columns sahi nahi hain.")
    raise SystemExit

# Step 3: Amount ko numeric banao
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df = df.dropna(subset=["Amount"])
df = df[df["Amount"] >= 0]

if df.empty:
    print("Error: CSV mein valid orders nahi hain.")
    raise SystemExit

# Step 4: Analysis calculate karo
monthly = df.groupby("Month")["Amount"].sum()
total = df["Amount"].sum()

category = df.groupby("Category")["Amount"].sum()
percentage = (category / total) * 100

best_month = monthly.idxmax()
best_amount = monthly.max()

mean_purchase = df["Amount"].mean()
median_purchase = df["Amount"].median()

# Step 5: Menu
while True:
    print("\n===== CUSTOMER PURCHASE PATTERN ANALYZER =====")
    print("1. Monthly Spending")
    print("2. Total Spending and Best Month")
    print("3. Category-wise Analysis")
    print("4. Mean, Median and Total Orders")
    print("5. Show Spending Chart")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()
    print("DEBUG:", repr(choice))
    input("Test dekhne ke liye Enter dabao...")

    if choice == "1":
        print("\n----- MONTHLY SPENDING -----")
        print(monthly.to_string())

    elif choice == "2":
        print("\n----- TOTAL SPENDING -----")
        print("Total Spending: Rs.", total)
        print("Best Month:", best_month)
        print("Best Month Spending: Rs.", best_amount)

    elif choice == "3":
        print("\n----- CATEGORY ANALYSIS -----")
        print("\nCategory-wise Spending:")
        print(category.to_string())

        print("\nCategory-wise Percentage:")
        print(percentage.round(2).to_string())

    elif choice == "4":
        print("\n----- PURCHASE STATISTICS -----")
        print("Mean Purchase: Rs.", round(mean_purchase, 2))
        print("Median Purchase: Rs.", median_purchase)
        print("Total Orders:", len(df))

    elif choice == "5":
        print("\nShowing spending chart...")
        monthly.plot(kind="bar")
        plt.title("Monthly Customer Spending")
        plt.xlabel("Month")
        plt.ylabel("Spending (Rs.)")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

    elif choice == "6":
        print("Thank you for using the analyzer!")
        break

    else:
        print("Invalid choice! Please enter 1 to 6.")
