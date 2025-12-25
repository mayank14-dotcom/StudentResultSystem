import pandas as pd
data={
    "student_id":[101,102,103,104],
    "name":["max","mayank","ram","raj"],
    "maths":[34,96,78,95],
    "science":[34,86,22,45],
    "english":[89,97,89,96],
    "history":[23,89,23,56]
}
df=pd.DataFrame(data)
print(df)
print("\n")
df["total_marks"]=df[["maths","science","english","history"]].sum(axis=1)
print(df)
print("\n")
max_total=df["total_marks"].max()
print("maximum total marks scored is :",max_total)
print("\n")
failed_condition = (df[["maths","science","english","history"]] < 40).any(axis=1)
failed_students = df[failed_condition]
print("Failed students (marks < 40 in any subject):")
print(failed_students)
print("\n")
topper=df[df["total_marks"]==max_total]
print("topper student details:")
print(topper)