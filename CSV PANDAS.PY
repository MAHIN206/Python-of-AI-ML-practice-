# Read CSV
df = pd.read_csv("data.csv")

# Read selected columns
df = pd.read_csv("data.csv", usecols=["Name", "Salary"])

# Read only first 100 rows
df = pd.read_csv("data.csv", nrows=100)

# Read large CSV in chunks
for chunk in pd.read_csv("data.csv", chunksize=1000):
    print(chunk.head())

# Export CSV
df.to_csv("output.csv", index=False)

# Read Excel
df = pd.read_excel("data.xlsx")

# Export Excel
df.to_excel("output.xlsx", index=False)

# Export JSON
df.to_json("output.json", orient="records")

# Export HTML
df.to_html("output.html", index=False)