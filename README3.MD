# ENSF 692 Spring 2024 - Assignment 4

## 📚 Learning Outcomes
* Manipulate and analyze data using Pandas DataFrame objects
* Read Excel data into a DataFrame
* Use hierarchical indexing to sort and slice data
* Process data according to specifications
* Find values in a dataset
* Operate on data in Pandas

## 💻 Program Specifications
The City of Calgary tracks information on the most popular licensed dog breeds in the city.
You are being asked to design a terminal-based application for computing and printing statistics based on a provided breed input.
The provided dataset has been modified from the City of Calgary data:
https://data.calgary.ca/Demographics/Top-100-Licensed-Dog-Breeds/wi52-6nx6

Your application must meet the following design specifications:
* Your final output should match the given examples (screenshots included in the rubric)
* Stage 1: DataFrame Creation
  1. Import the provided data into a Pandas DataFrame. 
  2. You may not change or sort the Excel file.
  3. You may not hard-code/copy-paste any information into your program except for the expected years and column header names.
  4. You may index the information in any way.
* Stage 2: User Entry
  1. Prompt the user to enter a dog breed.
  2. If the name does not exist within the given data, raise a KeyError to print “Dog breed not found in the data. Please try again.” 
  3. Users should be prompted continually until a correct input is provided.
  4. As long as the entry is spelled correctly, your program should accept entries in uppercase, lowercase, camel case, and mixed case.
  5. You may assume that the user knows how the breed names are identified in the database.
  6. After successful data entry and analysis, your program should end.
* Stage 3: Data Analysis
  1. Find and print all years where the selected breed was listed in the top breeds.
  2. Calculate and print the total number of registrations of the selected breed found in the dataset.
  3. Calculate and print the percentage of selected breed registrations out of the total percentage for each year (2021, 2022, 2023).
  4. Calculate and print the percentage of selected breed registrations out of the total three-year percentage.
  5. Find and print the months that were most popular for the selected breed registrations. Print all months that tie.
* Your terminal output must match the provided example interface, including the wording (not just printing the values).
* Your code should include and use at least one multi-index Pandas DataFrame, at least one IndexSlice object, at least one masking operation, at least one grouping operation, and at least one built-in Pandas or NumPy computational method.
* Your code must follow the conventions discussed so far in the course (ClassNames, four spaces for indentations, spaces between variables/operators, comments throughout, etc.)
* Any user-defined classes, methods, and functions must contain docstring documentation.
    1. For each class, include a functionality summary and describe any class and/or instance variables (do not include a separate docstring for \_\_init\_\_)
    2. For each method/function, include a functionality summary and describe parameters and return values (or specify if there are none)
    3. Main functions do not need a docstring but should be well-commented 
* Your code will be run by the TAs as your end user.
* To facilitate grading, please leave the Excel spreadsheet unmodified within your directory. Do not place it within a separate subfolder.
* Please do not provide a path to the Excel file when importing the data. You should simply use `'CalgaryDogBreeds.xlsx'` as it is contained within the same directory..
* The grading rubric will be posted to D2L.

## 📝 Assignment Tasks
* Make sure to review the corresponding labs and Jupyter Notebooks.
* Open VSCode and start a new terminal. 
* `calgary_dogs.py` is provided as a starting point. Fill in the header with your own information.
* Remember to test your program execution via the terminal: `python calgary_dogs.py`
* Take a screenshot of your successful program run and upload it to your assignment repository.
* Commit your screenshot and code.
* Push your local git history to GitHub.
* Submit your repository HTTPS link to the Assignment 4 D2L dropbox.
* Tip: If you want to learn more about a specific aspect of a Python object or the functionality of Pandas, remember to take a look at the official documentation!
