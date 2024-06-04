 FIFA 21 Data Analysis Summary

# Overview
This analysis focuses on the FIFA 21 dataset, which includes detailed statistics and attributes of players. The goal is to clean, preprocess, and extract meaningful insights from the data. We cover various categories including clubs, contracts, physical attributes, and more. Below is a detailed summary of the data cleaning and analysis process for each category.

# Data Loading and Initial Inspection
- Loaded the dataset from the CSV file.
- Displayed the first few rows and checked the shape and information of the data.

# Data Cleaning and Preprocessing

 1. Clubs
- Inspected the `Club` column and identified any leading or trailing spaces.
- Removed extra spaces to standardize the club names.

 2. Contracts
- Analyzed the `Contract` column to identify patterns such as loan and free agents.
- Extracted contract start and end dates and calculated the contract length in years.
- Created new columns: `Contract Start`, `Contract End`, and `Contract Length (years)`.
- Categorized contract statuses into 'Free', 'On Loan', and 'Contract'.

 3. Physical Attributes
- Height: Standardized the height values by converting them to centimeters. Handled heights given in both cm and feet/inches formats.
- Weight: Standardized the weight values by converting them to kilograms. Handled weights given in both kg and lbs formats.

 4. Loan Information
- Filtered players on loan and examined their loan end dates to understand the duration and status of loan spells.

 5. Star Ratings
- Cleaned the `W/F` (Weak Foot) column by removing the star symbols and converting them to numeric values.

 6. Hits
- Inspected the `Hits` column to understand the unique values and data type.

# Detailed Analysis
 Clubs
- Standardized club names help in grouping and comparing player data across different clubs without inconsistencies.

 Contracts
- Understanding contract lengths and statuses helps in assessing player stability and movement within the clubs.
- Loan and free agent statuses are crucial for transfer market analysis.

 Physical Attributes
- Standardized heights and weights are important for scouting reports and physical assessments.
- Converted measurements allow for uniform comparisons and visualizations.

 Loan Information
- Detailed loan information provides insights into temporary player movements and their impact on both parent and loan clubs.

 Star Ratings
- Cleaned star ratings are essential for player skill assessments, affecting gameplay strategies and player valuation.

