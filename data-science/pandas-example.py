import pandas as pd
import matplotlib.pyplot as plt

# Dataframes

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)

print(df["Age"])


print("MAX---->", df["Age"].median())
print("DESCRIBE---->", df["Age"].describe())

# General

type(df[["Age", "Sex"]])


# Series
ages = pd.Series([22, 35, 58], name="Age")



print(ages)


# ploting

grades = pd.read_csv("grades.csv", index_col=0, parse_dates=True)
grades.head()
grades.plot()
plt.show()