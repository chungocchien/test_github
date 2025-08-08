import pandas as pd

df = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'sales': [200, 220, 250, 275, 300],
    'profit': [50, 60, 70, 80, 90]
})
print(df.describe())