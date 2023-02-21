import math
import pandas as pd
data = pd.read_csv('age-buy.csv')
# Compute counts for each age and buy combination
counts = data.groupby(['Age', 'Buy']).size().unstack(fill_value=0)
counts1=data.groupby(['Income','Buy']).size().unstack(fill_value=0)
counts2=data.groupby(['Status','Buy']).size().unstack(fill_value=0)
# Compute total counts for each buy category
buy_counts = counts.sum(axis=0)


# Compute probabilities of "yes" and "no" for each age and buy category
p_yes = counts['yes'] / buy_counts['yes']
p_no = counts['no'] / buy_counts['no']

p_yes1 = counts1['yes'] / buy_counts['yes']
p_no1 = counts1['no'] / buy_counts['no']

p_yes2 = counts2['yes'] / buy_counts['yes']
p_no2 = counts2['no'] / buy_counts['no']


p_yes_total=buy_counts['yes']/(buy_counts['yes']+buy_counts['no'])
p_no_total=buy_counts['no']/(buy_counts['yes']+buy_counts['no'])

# Create a new DataFrame with the results
results = pd.DataFrame({
                        'Age':counts.index,
                        'Yes': counts['yes'],
                        'No': counts['no'],
                        'Total Yes': buy_counts['yes'],
                        'Total No': buy_counts['no'],
                        'P(Yes|Age)': p_yes,
                        'P(No|Age)': p_no})
                    
results = results.reset_index(drop=True)


results1 = pd.DataFrame({
                        'Income':counts1.index,
                        'Yes': counts1['yes'],
                        'No': counts1['no'],
                        'Total Yes': buy_counts['yes'],
                        'Total No': buy_counts['no'],
                        'P(Yes|Income)': p_yes1,
                        'P(No|Income)': p_no1})

results1 = results1.reset_index(drop=True)

results2 = pd.DataFrame({
                        'Status':counts2.index,
                        'Yes': counts2['yes'],
                        'No': counts2['no'],
                        'Total Yes': buy_counts['yes'],
                        'Total No': buy_counts['no'],
                        'P(Yes|Status)': p_yes2,
                        'P(No|Status)': p_no2})

results2 = results2.reset_index(drop=True)

print('\n')
print(results)
print('\n')
print(results1)
print('\n')
print(results2)
print('\n')


input_age = input('Enter Age Category: ')
input_income = input('Enter Income Category: ')
input_status = input('Enter Status Category: ')

results_filtered = results[(results['Age'] == input_age)]
results_filtered1=results1[results1['Income']==input_income]
results_filtered2=results2[results2['Status']==input_status]
# Extract P(Yes|Age), P(Yes|Income), and P(Yes|Status) from the corresponding DataFrames
p_yes_age = results_filtered['P(Yes|Age)'].values[0]
p_yes_income = results_filtered1['P(Yes|Income)'].values[0]
p_yes_status = results_filtered2['P(Yes|Status)'].values[0]

p_no_age = results_filtered['P(No|Age)'].values[0]
p_no_income = results_filtered1['P(No|Income)'].values[0]
p_no_status = results_filtered2['P(No|Status)'].values[0]


p_yes_find=p_yes_age*p_yes_income*p_yes_status*p_yes_total
p_no_find=p_no_age*p_no_income*p_no_status*p_no_total


print("\n")
print("P(Yes|Find): ",round(p_yes_find,4))
print("P(No|Find): ",round(p_no_find,4))

total=p_yes_find+p_no_find

print("Total: ",total)

while(math.isclose(total,1.0,abs_tol=0.001)==False):
    print("\n")
    print("Normalization: ")
    p_yes_find=p_yes_find/total
    print("P(Yes|Find): ",p_yes_find)
    p_no_find= p_no_find/ total
    print("P(No|Find): ",p_no_find)
    total=p_yes_find+p_no_find
    print("Total: ",total)
    print('\n')


if(p_yes_find>=p_no_find):
    print("He can Buy")
else:
    print("He can't Buy")
print('\n')