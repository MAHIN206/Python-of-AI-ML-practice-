
df = pd.read_csv("data.csv")


df = pd.read_csv("data.csv", usecols=["Name", "Salary"])


df = pd.read_csv("data.csv", nrows=100)


for chunk in pd.read_csv("data.csv", chunksize=1000):
    print(chunk.head())


df.to_csv("output.csv", index=False)



df.to_json("output.json", orient="records")
df.to_html("output.html", index=False)
df.to_excel("output.xlsx", index=False)