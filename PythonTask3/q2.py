import pandas as pd


df = pd.read_csv('/Users/aastik/vs/task3/names.csv', header=None, names=['number', 'name'])


df = df.sort_values(by='number')
print(df)
 
df =df.iloc[::2]
print(df)
name_string = ' '.join(df['name']).replace(' ', '').strip()

min_diff = float('inf')
name_set = set(name_string) 

for char1 in name_set:
    for char2 in name_set:
        if char1 != char2:  
            diff = abs(ord(char1) - ord(char2))
            min_diff = min(min_diff, diff)

print(f"The minimum absolute ASCII difference is: {min_diff}")



