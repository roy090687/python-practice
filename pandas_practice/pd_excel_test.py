import pandas as pd

pd.set_option('display.max_columns', None)   # show all columns
pd.set_option('display.max_rows', None)      # show all rows (careful with big data)

df = pd.read_excel("resource/test-data.xlsx", sheet_name="course-part-1")
print(df)

# Group by Category and calculate average Rating
print("----------------------- Group by Category and calculate average Rating -----------------------")
avg_rating = df.groupby("Category")["Rating"].mean()
print(avg_rating)

# Filter rows where Instructor = "Rahul Shetty"
print("----------------------- Filter rows where Instructor = 'Rahul Shetty' -----------------------")
rahul_courses = df[df["Instructor"] == "Rahul Shetty"][["Course Name", "Instructor"]]
print(rahul_courses)

# Create a new row as a dictionary
new_row = {
    "Course ID": "C111",
    "Course Name": "API Automation",
    "Category": "Automation",
    "Duration (hrs)": 20,
    "Level": "Intermediate",
    "Instructor": "Snehasish Roy",
    "Price (USD)": 150,
    "Rating": 4.7,
    "Enrolled Students": 280
}

# Append the row to DataFrame
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Save back to Excel (overwrite existing file)
df.to_excel("resource/test-data.xlsx", sheet_name="course-part-1", index=False)

print("Row added and Excel updated")
