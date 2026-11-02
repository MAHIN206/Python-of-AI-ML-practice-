"""
PANDAS COMPLETE BEGINNER GUIDE
==============================

One-file reference for the most commonly used Pandas basics.
Run this file from VS Code or a Python environment where pandas is installed.

Install:
    python -m pip install pandas

Optional packages for Excel and plotting:
    python -m pip install openpyxl matplotlib

This file uses small sample datasets, so you can run it without downloading data.
"""

import pandas as pd
import numpy as np


# ============================================================
# 1. INTRODUCTION AND VERSION
# ============================================================

print("\n" + "=" * 65)
print("1. INTRODUCTION")
print("=" * 65)

print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)


# ============================================================
# 2. SERIES
# ============================================================

print("\n" + "=" * 65)
print("2. SERIES")
print("=" * 65)

# A Series is a one-dimensional labeled collection of values.
numbers = pd.Series([10, 20, 30, 40, 50])
print("\nSimple Series:\n", numbers)

# Create a Series with custom index labels.
marks = pd.Series(
    [85, 90, 78],
    index=["Math", "English", "Python"]
)
print("\nSeries with custom index:\n", marks)

# Access Series values.
print("\nFirst value:", marks.iloc[0])
print("Value at label Math:", marks.loc["Math"])
print("All values:\n", marks.values)
print("Index labels:", marks.index)
print("Data type:", marks.dtype)
print("Number of values:", marks.size)

# Series operations.
print("\nAdd 5 to every value:\n", marks + 5)
print("Values greater than 80:\n", marks[marks > 80])

# Useful Series methods.
print("Mean:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())
print("Unique values:", marks.unique())
print("Value counts:\n", marks.value_counts())


# ============================================================
# 3. CREATE A DATAFRAME
# ============================================================

print("\n" + "=" * 65)
print("3. CREATE A DATAFRAME")
print("=" * 65)

# A DataFrame is a two-dimensional table with rows and columns.
data = {
    "name": ["Amin", "Sara", "Rahim", "Nila", "Karim", "Tania"],
    "age": [22, 24, 21, 23, 25, 22],
    "department": ["CSE", "EEE", "CSE", "BBA", "CSE", "EEE"],
    "salary": [45000, 52000, 40000, 48000, 60000, 50000],
    "city": ["Dhaka", "Chattogram", "Dhaka", "Sylhet", "Dhaka", "Khulna"],
    "score": [88, 92, 75, 85, 95, 89]
}

df = pd.DataFrame(data)
print("\nComplete DataFrame:\n", df)

# Create a DataFrame from lists.
small_df = pd.DataFrame(
    [["A", 10], ["B", 20], ["C", 30]],
    columns=["item", "quantity"]
)
print("\nDataFrame from lists:\n", small_df)

# Create a DataFrame from a list of dictionaries.
students = pd.DataFrame([
    {"name": "Rafi", "age": 21},
    {"name": "Mitu", "age": 22},
    {"name": "Sami", "age": 23}
])
print("\nDataFrame from dictionaries:\n", students)


# ============================================================
# 4. INSPECT A DATAFRAME
# ============================================================

print("\n" + "=" * 65)
print("4. INSPECT A DATAFRAME")
print("=" * 65)

print("\nFirst 5 rows:\n", df.head())
print("\nFirst 3 rows:\n", df.head(3))
print("\nLast 5 rows:\n", df.tail())
print("\nLast 2 rows:\n", df.tail(2))
print("\nRandom 2 rows:\n", df.sample(2, random_state=1))

print("\nShape (rows, columns):", df.shape)
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))
print("Column names:", df.columns)
print("Index:", df.index)
print("Data types:\n", df.dtypes)

print("\nDataFrame information:")
df.info()

print("\nStatistical summary:\n", df.describe())
print("\nSummary including text columns:\n", df.describe(include="all"))

print("\nMemory usage:\n", df.memory_usage())
print("Total memory usage:", df.memory_usage(deep=True).sum())


# ============================================================
# 5. SELECT COLUMNS AND ROWS
# ============================================================

print("\n" + "=" * 65)
print("5. SELECT COLUMNS AND ROWS")
print("=" * 65)

# Select one column: returns a Series.
print("\nName column:\n", df["name"])
print("\nName column using dot notation:\n", df.name)

# Select multiple columns: returns a DataFrame.
print("\nName and salary:\n", df[["name", "salary"]])

# Select rows by position with iloc.
print("\nFirst row:\n", df.iloc[0])
print("\nFirst three rows:\n", df.iloc[0:3])
print("\nFirst row, first two columns:\n", df.iloc[0, 0:2])
print("\nRows 1 to 3, columns 0 to 2:\n", df.iloc[1:4, 0:3])

# Select rows by labels with loc.
print("\nRow with index label 0:\n", df.loc[0])
print("\nRows 1 to 3:\n", df.loc[1:3])
print("\nSelected rows and columns:\n", df.loc[0:2, ["name", "salary"]])

# Select a single value.
print("\nValue at row 0, column name:", df.loc[0, "name"])
print("Value by position:", df.iloc[0, 0])

# Select using at and iat (fast scalar access).
print("Using at:", df.at[0, "name"])
print("Using iat:", df.iat[0, 0])


# ============================================================
# 6. FILTER ROWS
# ============================================================

print("\n" + "=" * 65)
print("6. FILTER ROWS")
print("=" * 65)

print("\nAge greater than 22:\n", df[df["age"] > 22])
print("\nSalary equal to 50000:\n", df[df["salary"] == 50000])
print("\nSalary not equal to 50000:\n", df[df["salary"] != 50000])

# Multiple conditions: use & for AND, | for OR.
print("\nAge > 21 AND salary > 45000:\n",
      df[(df["age"] > 21) & (df["salary"] > 45000)])

print("\nDepartment is CSE OR EEE:\n",
      df[(df["department"] == "CSE") | (df["department"] == "EEE")])

# Use isin() for multiple allowed values.
print("\nDepartment in CSE or BBA:\n",
      df[df["department"].isin(["CSE", "BBA"])])

# Use between() for a range.
print("\nSalary between 45000 and 55000:\n",
      df[df["salary"].between(45000, 55000)])

# Use query() for readable filtering.
print("\nUsing query:\n", df.query("age >= 22 and salary > 45000"))

# Check whether text contains a word.
print("\nNames containing 'a':\n",
      df[df["name"].str.contains("a", case=False, na=False)])


# ============================================================
# 7. ADD, UPDATE, RENAME AND DELETE COLUMNS
# ============================================================

print("\n" + "=" * 65)
print("7. ADD, UPDATE, RENAME AND DELETE COLUMNS")
print("=" * 65)

work = df.copy()

# Add a new column.
work["bonus"] = 5000
work["total_income"] = work["salary"] + work["bonus"]
work["is_senior"] = work["age"] >= 23
print("\nAfter adding columns:\n", work)

# Add a column at a specific position.
work.insert(1, "student_id", [101, 102, 103, 104, 105, 106])
print("\nAfter insert:\n", work)

# Update an existing column.
work.loc[0, "salary"] = 47000
work.loc[work["department"] == "CSE", "bonus"] = 7000
print("\nAfter updating values:\n", work)

# Rename columns.
renamed = work.rename(columns={"name": "full_name", "salary": "monthly_salary"})
print("\nRenamed columns:\n", renamed)

# Rename the index.
renamed.index.name = "row_number"
print("\nIndex name:", renamed.index.name)

# Delete columns (drop returns a new DataFrame by default).
without_bonus = work.drop(columns=["bonus", "total_income"])
print("\nAfter dropping columns:\n", without_bonus)

# Delete rows by index label.
without_first_row = df.drop(index=0)
print("\nAfter dropping first row:\n", without_first_row)

# Keep only selected columns.
selected = df.filter(items=["name", "salary"])
print("\nUsing filter:\n", selected)


# ============================================================
# 8. SORTING
# ============================================================

print("\n" + "=" * 65)
print("8. SORTING")
print("=" * 65)

print("\nSort by salary ascending:\n", df.sort_values("salary"))
print("\nSort by salary descending:\n", df.sort_values("salary", ascending=False))
print("\nSort by department then salary:\n",
      df.sort_values(["department", "salary"], ascending=[True, False]))

print("\nSort index ascending:\n", df.sort_index())
print("\nSort index descending:\n", df.sort_index(ascending=False))


# ============================================================
# 9. MISSING VALUES
# ============================================================

print("\n" + "=" * 65)
print("9. MISSING VALUES")
print("=" * 65)

missing_df = pd.DataFrame({
    "name": ["Amin", "Sara", None, "Nila", "Karim"],
    "age": [22, np.nan, 21, 23, np.nan],
    "salary": [45000, 52000, np.nan, 48000, 60000],
    "city": ["Dhaka", None, "Dhaka", "Sylhet", None]
})
print("\nData with missing values:\n", missing_df)

print("\nMissing-value mask:\n", missing_df.isna())
print("\nMissing values per column:\n", missing_df.isna().sum())
print("\nTotal missing values:", missing_df.isna().sum().sum())
print("\nNon-missing values:\n", missing_df.notna())

# Remove rows or columns containing missing values.
print("\nDrop rows with any missing value:\n", missing_df.dropna())
print("\nDrop columns with any missing value:\n", missing_df.dropna(axis=1))
print("\nDrop rows where all values are missing:\n", missing_df.dropna(how="all"))

# Fill missing values with a fixed value.
print("\nFill all missing values with 0:\n", missing_df.fillna(0))

# Fill selected columns with suitable values.
filled = missing_df.copy()
filled["age"] = filled["age"].fillna(filled["age"].mean())
filled["salary"] = filled["salary"].fillna(filled["salary"].median())
filled["name"] = filled["name"].fillna("Unknown")
filled["city"] = filled["city"].fillna("Not given")
print("\nFill columns with mean/median/text:\n", filled)

# Forward fill and backward fill.
print("\nForward fill:\n", missing_df.ffill())
print("\nBackward fill:\n", missing_df.bfill())

# Replace selected values.
print("\nReplace Unknown with N/A:\n",
      filled.replace("Unknown", "N/A"))


# ============================================================
# 10. DUPLICATE VALUES
# ============================================================

print("\n" + "=" * 65)
print("10. DUPLICATE VALUES")
print("=" * 65)

duplicate_df = pd.DataFrame({
    "name": ["Amin", "Sara", "Amin", "Nila"],
    "age": [22, 24, 22, 23]
})

print("\nOriginal data:\n", duplicate_df)
print("\nDuplicate row mask:\n", duplicate_df.duplicated())
print("\nDuplicate names:\n", duplicate_df.duplicated(subset=["name"]))

print("\nRemove duplicate rows:\n", duplicate_df.drop_duplicates())
print("\nKeep last duplicate:\n", duplicate_df.drop_duplicates(keep="last"))
print("\nRemove duplicates based on name:\n",
      duplicate_df.drop_duplicates(subset=["name"]))


# ============================================================
# 11. DATA TYPES AND CONVERSION
# ============================================================

print("\n" + "=" * 65)
print("11. DATA TYPES AND CONVERSION")
print("=" * 65)

type_df = pd.DataFrame({
    "age": ["20", "21", "22"],
    "salary": ["30000", "40000", "50000"],
    "passed": ["True", "False", "True"]
})
print("\nOriginal data types:\n", type_df.dtypes)

type_df["age"] = type_df["age"].astype(int)
type_df["salary"] = pd.to_numeric(type_df["salary"])
type_df["passed"] = type_df["passed"].map({"True": True, "False": False})
print("\nConverted data types:\n", type_df.dtypes)
print(type_df)

# Safe numeric conversion: invalid values become NaN.
safe_numbers = pd.Series(["10", "20", "wrong", "40"])
print("\nSafe numeric conversion:\n", pd.to_numeric(safe_numbers, errors="coerce"))

# Convert to category.
category_df = df.copy()
category_df["department"] = category_df["department"].astype("category")
print("\nCategory data type:", category_df["department"].dtype)


# ============================================================
# 12. MATHEMATICAL AND STATISTICAL OPERATIONS
# ============================================================

print("\n" + "=" * 65)
print("12. MATHEMATICAL AND STATISTICAL OPERATIONS")
print("=" * 65)

print("\nSum:\n", df[["age", "salary", "score"]].sum())
print("\nMean:\n", df[["age", "salary", "score"]].mean())
print("\nMedian:\n", df[["age", "salary", "score"]].median())
print("\nMode:\n", df[["age", "department"]].mode())
print("\nMinimum:\n", df[["age", "salary", "score"]].min())
print("\nMaximum:\n", df[["age", "salary", "score"]].max())
print("\nStandard deviation:\n", df[["age", "salary", "score"]].std())
print("\nVariance:\n", df[["age", "salary", "score"]].var())
print("\nCount of non-missing values:\n", df.count())
print("\nQuantiles:\n", df["salary"].quantile([0.25, 0.50, 0.75]))
print("\nCorrelation:\n", df[["age", "salary", "score"]].corr())
print("\nCumulative sum:\n", df["salary"].cumsum())
print("\nCumulative maximum:\n", df["salary"].cummax())
print("\nPercentage change:\n", df["salary"].pct_change())

# Apply mathematical operations to a column.
print("\nSalary divided by 12:\n", df["salary"] / 12)
print("\nScore rounded:\n", df["score"].round(0))


# ============================================================
# 13. VALUE COUNTS AND UNIQUE VALUES
# ============================================================

print("\n" + "=" * 65)
print("13. VALUE COUNTS AND UNIQUE VALUES")
print("=" * 65)

print("\nUnique departments:", df["department"].unique())
print("Number of unique departments:", df["department"].nunique())
print("\nDepartment frequency:\n", df["department"].value_counts())
print("\nDepartment percentage:\n", df["department"].value_counts(normalize=True) * 100)
print("\nInclude missing values:\n", missing_df["city"].value_counts(dropna=False))


# ============================================================
# 14. GROUPBY
# ============================================================

print("\n" + "=" * 65)
print("14. GROUPBY")
print("=" * 65)

# Group data by one column and calculate statistics.
print("\nAverage salary by department:\n",
      df.groupby("department")["salary"].mean())

print("\nTotal salary by department:\n",
      df.groupby("department")["salary"].sum())

print("\nMultiple statistics:\n",
      df.groupby("department")["salary"].agg(["count", "mean", "min", "max", "sum"]))

# Group by multiple columns.
print("\nGroup by department and city:\n",
      df.groupby(["department", "city"])["salary"].mean())

# Named aggregation.
summary = df.groupby("department").agg(
    employee_count=("name", "count"),
    average_salary=("salary", "mean"),
    highest_score=("score", "max")
)
print("\nNamed aggregation:\n", summary)

# Transform returns a result aligned with the original rows.
group_means = df.groupby("department")["salary"].transform("mean")
grouped_df = df.copy()
grouped_df["department_average_salary"] = group_means
print("\nGroup transform:\n", grouped_df)


# ============================================================
# 15. APPLY, MAP AND REPLACE
# ============================================================

print("\n" + "=" * 65)
print("15. APPLY, MAP AND REPLACE")
print("=" * 65)

# map() changes values in a Series using a dictionary or function.
department_codes = df["department"].map({
    "CSE": "Computer Science",
    "EEE": "Electrical",
    "BBA": "Business"
})
print("\nMap department names:\n", department_codes)

# apply() applies a function to each value in a Series.
print("\nNames in uppercase:\n", df["name"].apply(lambda x: x.upper()))

# apply() can work across DataFrame rows or columns.
print("\nSalary category:\n",
      df["salary"].apply(lambda x: "High" if x >= 50000 else "Normal"))

print("\nMaximum of each numeric column:\n",
      df[["age", "salary", "score"]].apply(max))

# replace() replaces values.
print("\nReplace CSE with CS:\n", df["department"].replace("CSE", "CS"))


# ============================================================
# 16. STRING OPERATIONS (.STR)
# ============================================================

print("\n" + "=" * 65)
print("16. STRING OPERATIONS")
print("=" * 65)

text_df = pd.DataFrame({
    "name": ["  amin rahman ", "SARA KHAN", "rahim uddin", "Nila Akter"],
    "email": ["amin@gmail.com", "sara@yahoo.com", "rahim@gmail.com", "nila@gmail.com"]
})

print("\nOriginal text:\n", text_df)
print("\nLowercase:\n", text_df["name"].str.lower())
print("\nUppercase:\n", text_df["name"].str.upper())
print("\nTitle case:\n", text_df["name"].str.title())
print("\nRemove extra spaces at ends:\n", text_df["name"].str.strip())
print("\nReplace text:\n", text_df["name"].str.replace("a", "@", regex=False))
print("\nContains 'rah':\n", text_df["name"].str.contains("rah", case=False, na=False))
print("\nStarts with S:\n", text_df["name"].str.startswith("S", na=False))
print("\nEnds with n:\n", text_df["name"].str.endswith("n", na=False))
print("\nString length:\n", text_df["name"].str.len())
print("\nSplit names:\n", text_df["name"].str.strip().str.split(" "))
print("\nExtract email domain:\n", text_df["email"].str.split("@").str[-1])


# ============================================================
# 17. CONCATENATION
# ============================================================

print("\n" + "=" * 65)
print("17. CONCATENATION")
print("=" * 65)

first = pd.DataFrame({"name": ["Amin", "Sara"], "score": [80, 90]})
second = pd.DataFrame({"name": ["Rahim", "Nila"], "score": [75, 88]})

# Stack rows.
print("\nConcatenate rows:\n", pd.concat([first, second], ignore_index=True))

# Join columns side by side.
left = pd.DataFrame({"name": ["Amin", "Sara"]})
right = pd.DataFrame({"city": ["Dhaka", "Sylhet"]})
print("\nConcatenate columns:\n", pd.concat([left, right], axis=1))

# Keep original indexes if ignore_index is not used.
print("\nConcatenate with original index:\n", pd.concat([first, second]))


# ============================================================
# 18. MERGE AND JOIN
# ============================================================

print("\n" + "=" * 65)
print("18. MERGE AND JOIN")
print("=" * 65)

employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Amin", "Sara", "Rahim", "Nila"],
    "dept_id": [10, 20, 10, 30]
})

departments = pd.DataFrame({
    "dept_id": [10, 20, 30],
    "department": ["CSE", "EEE", "BBA"]
})

# Inner merge: matching keys only.
print("\nInner merge:\n",
      pd.merge(employees, departments, on="dept_id", how="inner"))

# Left merge: keep all rows from the left DataFrame.
print("\nLeft merge:\n",
      pd.merge(employees, departments, on="dept_id", how="left"))

# Right merge: keep all rows from the right DataFrame.
print("\nRight merge:\n",
      pd.merge(employees, departments, on="dept_id", how="right"))

# Outer merge: keep all keys from both DataFrames.
print("\nOuter merge:\n",
      pd.merge(employees, departments, on="dept_id", how="outer"))

# Merge when key column names are different.
left_data = pd.DataFrame({"employee_dept": [10, 20], "employee": ["Amin", "Sara"]})
right_data = pd.DataFrame({"dept_code": [10, 20], "dept_name": ["CSE", "EEE"]})
print("\nMerge with different key names:\n",
      pd.merge(left_data, right_data,
               left_on="employee_dept", right_on="dept_code"))

# Join uses indexes by default.
employee_indexed = employees.set_index("dept_id")
department_indexed = departments.set_index("dept_id")
print("\nJoin by index:\n", employee_indexed.join(department_indexed, rsuffix="_department"))


# ============================================================
# 19. PIVOT TABLES AND CROSSTABS
# ============================================================

print("\n" + "=" * 65)
print("19. PIVOT TABLES AND CROSSTABS")
print("=" * 65)

sales = pd.DataFrame({
    "city": ["Dhaka", "Dhaka", "Sylhet", "Sylhet", "Dhaka", "Sylhet"],
    "product": ["Rice", "Egg", "Rice", "Egg", "Rice", "Egg"],
    "sales": [100, 200, 150, 180, 120, 220]
})

print("\nPivot table:\n",
      sales.pivot_table(
          values="sales",
          index="city",
          columns="product",
          aggfunc="sum"
      ))

print("\nCrosstab:\n",
      pd.crosstab(df["department"], df["city"]))

print("\nCrosstab with percentages:\n",
      pd.crosstab(df["department"], df["city"], normalize="index") * 100)


# ============================================================
# 20. RESHAPING DATA
# ============================================================

print("\n" + "=" * 65)
print("20. RESHAPING DATA")
print("=" * 65)

wide = pd.DataFrame({
    "name": ["Amin", "Sara"],
    "Math": [80, 90],
    "English": [85, 95]
})

# Wide format to long format.
long = wide.melt(
    id_vars="name",
    var_name="subject",
    value_name="marks"
)
print("\nMelt (wide to long):\n", long)

# Long format to wide format.
print("\nPivot (long to wide):\n",
      long.pivot(index="name", columns="subject", values="marks"))


# ============================================================
# 21. INDEX OPERATIONS
# ============================================================

print("\n" + "=" * 65)
print("21. INDEX OPERATIONS")
print("=" * 65)

indexed = df.set_index("name")
print("\nSet name as index:\n", indexed)
print("\nReset index:\n", indexed.reset_index())

# Set a new index without removing the column.
print("\nSet index with drop=False:\n", df.set_index("name", drop=False))

# Reindex rows.
print("\nReindex:\n", df.reindex([0, 2, 4, 10]))

# Reset index and drop old index.
print("\nReset index and drop old index:\n", indexed.reset_index(drop=True))


# ============================================================
# 22. DATE AND TIME
# ============================================================

print("\n" + "=" * 65)
print("22. DATE AND TIME")
print("=" * 65)

date_df = pd.DataFrame({
    "date": ["2026-01-05", "2026-02-15", "2026-03-20"],
    "sales": [100, 150, 200]
})

# Convert text to datetime.
date_df["date"] = pd.to_datetime(date_df["date"])
print("\nDatetime data:\n", date_df)
print("Date data type:", date_df["date"].dtype)

# Extract date components.
print("\nYear:\n", date_df["date"].dt.year)
print("\nMonth:\n", date_df["date"].dt.month)
print("\nMonth name:\n", date_df["date"].dt.month_name())
print("\nDay:\n", date_df["date"].dt.day)
print("\nDay name:\n", date_df["date"].dt.day_name())
print("\nQuarter:\n", date_df["date"].dt.quarter)

# Filter dates.
print("\nDates after February 1:\n",
      date_df[date_df["date"] > "2026-02-01"])

# Create date ranges.
print("\nDate range:\n", pd.date_range(start="2026-01-01", periods=5, freq="D"))

# Date difference.
date_df["days_from_start"] = (date_df["date"] - date_df["date"].min()).dt.days
print("\nDate differences:\n", date_df)


# ============================================================
# 23. READING FILES
# ============================================================

print("\n" + "=" * 65)
print("23. READING FILES")
print("=" * 65)

# These are common file-reading commands.
# Uncomment and change the filename when you have the file.

# csv_df = pd.read_csv("data.csv")
# excel_df = pd.read_excel("data.xlsx")
# json_df = pd.read_json("data.json")
# txt_df = pd.read_csv("data.txt", sep="\t")
# html_tables = pd.read_html("https://example.com/table-page")
# parquet_df = pd.read_parquet("data.parquet")

# Useful read_csv options:
# pd.read_csv("data.csv", nrows=100)                 # Read first 100 rows
# pd.read_csv("data.csv", skiprows=2)                # Skip first 2 rows
# pd.read_csv("data.csv", usecols=["name", "age"])   # Read selected columns
# pd.read_csv("data.csv", header=0)                  # Specify header row
# pd.read_csv("data.csv", names=["A", "B"])          # Set column names
# pd.read_csv("data.csv", na_values=["NA", "?"])     # Define missing values
# pd.read_csv("data.csv", encoding="utf-8")          # Specify encoding
# pd.read_csv("data.csv", sep=";")                   # Change separator

print("File-reading examples are listed as comments in this section.")


# ============================================================
# 24. WRITING / EXPORTING FILES
# ============================================================

print("\n" + "=" * 65)
print("24. WRITING AND EXPORTING FILES")
print("=" * 65)

export_df = df.copy()

# Save to CSV.
export_df.to_csv("pandas_output.csv", index=False)
print("Saved: pandas_output.csv")

# Other common export commands (uncomment when needed).
# export_df.to_excel("pandas_output.xlsx", index=False)  # Requires openpyxl
# export_df.to_json("pandas_output.json", orient="records", indent=4)
# export_df.to_csv("pandas_output.txt", sep="\t", index=False)
# export_df.to_pickle("pandas_output.pkl")
# export_df.to_parquet("pandas_output.parquet")          # Requires pyarrow/fastparquet

# Read back the CSV created above.
read_back = pd.read_csv("pandas_output.csv")
print("\nRead the saved CSV:\n", read_back)


# ============================================================
# 25. WORKING WITH CSV FILES: COMMON OPTIONS
# ============================================================

print("\n" + "=" * 65)
print("25. CSV OPTIONS")
print("=" * 65)

# Examples:
# df.to_csv("file.csv", index=False)              # Do not save row index
# df.to_csv("file.csv", index=True)               # Save row index
# df.to_csv("file.csv", columns=["name", "age"], index=False)
# df.to_csv("file.csv", encoding="utf-8", index=False)
# df.to_csv("file.csv", sep=";", index=False)
# pd.read_csv("file.csv", index_col=0)            # Use first column as index
# pd.read_csv("file.csv", parse_dates=["date"])   # Parse date column
# pd.read_csv("file.csv", dtype={"id": str})      # Set data type

print("CSV options are listed as comments in this section.")


# ============================================================
# 26. CONDITIONAL COLUMNS: WHERE, MASK AND CLIP
# ============================================================

print("\n" + "=" * 65)
print("26. CONDITIONAL OPERATIONS")
print("=" * 65)

condition_df = df.copy()

# where keeps values when condition is True.
condition_df["salary_where"] = condition_df["salary"].where(
    condition_df["salary"] >= 50000, 0
)
print("\nUsing where:\n", condition_df[["name", "salary", "salary_where"]])

# mask replaces values where condition is True.
condition_df["salary_mask"] = condition_df["salary"].mask(
    condition_df["salary"] < 50000, 0
)
print("\nUsing mask:\n", condition_df[["name", "salary", "salary_mask"]])

# clip limits values to a range.
print("\nClip scores between 80 and 90:\n", df["score"].clip(80, 90))


# ============================================================
# 27. RANKING AND CUTTING INTO GROUPS
# ============================================================

print("\n" + "=" * 65)
print("27. RANKING AND BINNING")
print("=" * 65)

rank_df = df[["name", "score"]].copy()
rank_df["rank"] = rank_df["score"].rank(ascending=False, method="dense")
print("\nRanking:\n", rank_df)

# Divide numeric values into fixed-width categories.
rank_df["score_category"] = pd.cut(
    rank_df["score"],
    bins=[0, 80, 90, 100],
    labels=["Needs improvement", "Good", "Excellent"],
    include_lowest=True
)
print("\nUsing cut:\n", rank_df)

# Divide values into approximately equal-sized groups.
rank_df["score_quartile"] = pd.qcut(
    rank_df["score"],
    q=3,
    labels=["Low", "Medium", "High"]
)
print("\nUsing qcut:\n", rank_df)


# ============================================================
# 28. WINDOWS AND ROLLING CALCULATIONS
# ============================================================

print("\n" + "=" * 65)
print("28. ROLLING AND EXPANDING")
print("=" * 65)

time_series = pd.Series([10, 20, 30, 40, 50, 60])

print("\nRolling average of 3:\n", time_series.rolling(window=3).mean())
print("\nRolling sum of 3:\n", time_series.rolling(window=3).sum())
print("\nExpanding sum:\n", time_series.expanding().sum())
print("\nExponential weighted mean:\n", time_series.ewm(span=3).mean())


# ============================================================
# 29. DISPLAY SETTINGS
# ============================================================

print("\n" + "=" * 65)
print("29. DISPLAY SETTINGS")
print("=" * 65)

# These settings affect how Pandas prints tables.
pd.set_option("display.max_rows", 20)
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 120)
pd.set_option("display.max_colwidth", 30)
pd.set_option("display.precision", 2)

print("\nDisplay settings applied.")
print(df)

# Restore default display settings when needed.
# pd.reset_option("all")


# ============================================================
# 30. USEFUL DATAFRAME CHECKS
# ============================================================

print("\n" + "=" * 65)
print("30. USEFUL CHECKS")
print("=" * 65)

print("Is DataFrame empty?", df.empty)
print("Is each cell missing?\n", df.isna())
print("Does DataFrame have duplicate rows?", df.duplicated().any())
print("Are all values in score greater than 0?", (df["score"] > 0).all())
print("Is any salary greater than 55000?", (df["salary"] > 55000).any())
print("Columns containing numeric data:\n", df.select_dtypes(include="number"))
print("Columns containing text data:\n", df.select_dtypes(include="object"))


# ============================================================
# 31. COMMON METHOD CHEAT SHEET
# ============================================================

print("\n" + "=" * 65)
print("31. COMMON PANDAS CHEAT SHEET")
print("=" * 65)

cheat_sheet = {
    "Create": "pd.Series(), pd.DataFrame()",
    "Inspect": "head(), tail(), sample(), info(), describe()",
    "Select": "[], loc[], iloc[], at[], iat[]",
    "Filter": "df[condition], isin(), between(), query()",
    "Sort": "sort_values(), sort_index()",
    "Columns": "columns, rename(), insert(), drop()",
    "Missing": "isna(), notna(), dropna(), fillna()",
    "Duplicates": "duplicated(), drop_duplicates()",
    "Types": "dtypes, astype(), to_numeric(), to_datetime()",
    "Statistics": "mean(), median(), mode(), sum(), min(), max(), std(), corr()",
    "Groups": "groupby(), agg(), transform()",
    "Combine": "concat(), merge(), join()",
    "Reshape": "melt(), pivot(), pivot_table(), crosstab()",
    "Text": "str.lower(), str.upper(), str.strip(), str.contains()",
    "Dates": "to_datetime(), dt.year, dt.month, dt.day_name()",
    "Files": "read_csv(), read_excel(), to_csv(), to_excel()",
    "Other": "apply(), map(), replace(), where(), mask(), rank(), cut()"
}

for topic, methods in cheat_sheet.items():
    print(f"{topic:15} : {methods}")




print("\n" + "=" * 65)
print("PANDAS GUIDE COMPLETED SUCCESSFULLY!")
print("=" * 65)
print("You can use this file as a reference and practice each section.")
