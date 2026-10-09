import pandas as pd

''' task 1 '''

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet'],
    'Price': [1200, 800, 400],
    'Stock': [50, 150, 200]
}
df = pd.DataFrame(data)

data1 = {'Product': 'USB Hub', 'Price': 40, 'Stock': 150, 'Warranty': '2 years'}

df1 = pd.DataFrame([data1])

df = pd.concat([df, df1], ignore_index=True)
print(df)

''' task 2 '''

data2 = {'Product': 'USB Hub', 'Price': 'Forty', 'Stock': 150}
df2 = pd.DataFrame([data2])

df = pd.concat([df, df2], ignore_index=True)
print(df)


''' task 3 '''


feedback = pd.read_csv('customer_feedback.csv')

print(feedback)

grouped_feedback = feedback.groupby(['Region','Month'])['Rating'].mean()

grouped_feedback_un = grouped_feedback.unstack()

print(grouped_feedback_un)

average_rating = feedback['Rating'].mean()
grouped_feedback = grouped_feedback_un.fillna(average_rating)

print(grouped_feedback)