# Developed by Ibrohimova Adolatxon
import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': ['x', 'y', 'z', 'x', 'y']}
df = pd.DataFrame(data)

# A ustunida qiymati 3 dan katta bo'lgan qatorlarni tanlang
filtered_df = df[df['A'] > 3]
print(filtered_df)

# B ustunida qiymati 8 dan kichik yoki C ustunida qiymati 'x' bo'lgan qatorlarni tanlang
filtered_df = df[(df['B'] < 8) | (df['C'] == 'x')]
print(filtered_df)

# A ustunida qiymati 2 va 4 orasida bo'lgan qatorlarni tanlang
filtered_df = df[(df['A'] >=2) & (df['A'] <=4)]
print(filtered_df)

