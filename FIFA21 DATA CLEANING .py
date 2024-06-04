#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np


# In[2]:


pd.set_option('display.max_columns', None)

# Alternatively, you can use the options attribute directly:
#pd.options.display.max_columns = None

# Loading your CSV file
data = pd.read_csv('C:/Users/ODUOBUK/Documents/My Data Sources/fifa21 raw data v2.csv')

# Print the first few rows of the DataFrame to check
data.sample(10)


# In[3]:


data.shape


# In[4]:


data.info()


# In[5]:


fifa = data.copy()
fifa.sample(3)


# In[6]:


fifa['Club'].dtype


# In[7]:


fifa['Club'].unique()


# In[8]:


fifa['Club'] = fifa['Club'].str.strip()
fifa['Club'].unique()


# In[9]:


fifa['Contract'].dtype


# In[10]:


fifa['Contract'].unique()


# In[11]:


for index, row in fifa.iterrows():
    if 'On Loan' in row['Contract'] or 'Free' in row ['Contract']:
        print(row['Contract'])


# In[12]:


def extract_contract_info(contract):
    if contract == 'Free' or 'On Loan' in contract:
        start_date = np.nan
        end_date =np.nan
        contract_length = 0
    else:
        start_date, end_date = contract.split(' ~ ')
        start_year = int(start_date[:4])
        end_year = int(end_date[:4])
        contract_length = end_year - start_year
    return start_date, end_date, contract_length

# Apply fn to contract column & create new columns

new_cols = ['Contract Start', 'Contract End', 'Contract Length(years)']
new_data = fifa['Contract'].apply(lambda x: pd.Series(extract_contract_info(x)))

for i in range(len(new_cols)):
    fifa.insert(loc=fifa.columns.get_loc('Contract')+1+i, column=new_cols[i], value=new_data[i])


# In[13]:


fifa.sample(3)


# In[14]:


fifa[['Contract', 'Contract Start', 'Contract End', 'Contract Length(years)']].sample(5)


# In[15]:


#Contact categories

def categorize_contract_status(contract):
    if contract == 'Free':
        return 'Free'
    elif 'On Loan' in contract:
        return 'On Loan'
    else:
        return 'contract'


fifa.insert(fifa.columns.get_loc('Contract Length(years)')+1, 'Contract Status', fifa['Contract'].apply(categorize_contract_status))
fifa.sample(3)


# In[16]:


fifa[['Contract', 'Contract Start', 'Contract End', 'Contract Length(years)', 'Contract Status']].sample(5)


# In[17]:


fifa['Height'].dtype


# In[18]:


fifa['Height'].unique()


# In[19]:


def convert_height(height):
    if "cm" in height:
        return int(height.strip("cm"))
    else:
        feet, inches = height.split("'")
        total_inches = int(feet)*12 + int(inches.strip('"'))
        return round(total_inches * 2.54)
    
# Apply fnto height column
fifa['Height'] = fifa['Height'].apply(convert_height)
fifa['Height'].unique()

        


# In[20]:


fifa = fifa.rename(columns={'Height':"Height(cm)"})
fifa.sample(1)


# In[21]:


fifa['Weight'].dtype


# In[22]:


fifa['Weight'].unique()


# In[28]:


def convert_weight(weight):
    weight = weight.strip()  
    if weight.lower().endswith('kg'): 
        return int(weight[:-2])
    elif weight.lower().endswith('lbs'): 
        pounds = int(weight[:-3])
        return round(pounds / 2.205)
    else:
        return None 
# Applying the corrected function
fifa['Weight'] = fifa['Weight'].apply(convert_weight)
fifa['Weight'].unique()


# In[29]:


fifa = fifa.rename(columns={"Weight":"Weight(kg)"})
fifa.sample(3)


# In[30]:


fifa['Loan Date End'].dtype


# In[31]:


fifa['Loan Date End'].unique()


# In[32]:


on_loan = fifa[fifa['Contract Status'] == 'On Loan']
on_loan[['Contract', 'Contract Status', 'Loan Date End']]


# In[33]:


fifa['W/F'].dtype


# In[34]:


fifa['W/F'].unique()


# In[35]:


fifa['W/F'] = fifa['W/F'].str.replace('★',"")
fifa['W/F'].unique()


# In[36]:


fifa['Hits'].dtype


# In[37]:


fifa['Hits'].unique()


# In[ ]:




