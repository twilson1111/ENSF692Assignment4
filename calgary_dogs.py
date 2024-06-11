# calgary_dogs.py
# AUTHOR NAME: Tom Wilson
#
# This terminal program will input a datasource describing the most popular dog breeds
# The program prompts the user to select a breed, after which it reports various statistics for that breed
# 

import os
import numpy as np
import pandas as pd
import string

def import_file(file_name: string):
    """
    Read excel (xlsx) file into Pandas dataframe.
    @param filename to import eg: "file.xlsx"
    @return Pandas Dataframe containing data
    """
    # Import data here
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    # MULTIINDEX DATAFRAME
    df = pd.read_excel(file_path, index_col=[2, 0]) # Breed, Year, Month
    return df

def prompt_user_for_breed(breed_set):
    """
    Prompt user to input breed until they enter a breed that matches the supplied set
    @param breed_set: Set of strings representing available breeds
    @return: matched breed
    """
    found_breed = ""
    while not found_breed:
        try:
            breed_input = input("Please enter a dog breed: ")
            found_breed = parse_breed(breed_set, breed_input)
            if not found_breed:
                raise KeyError()
        except KeyError:
            print("Dog breed was not found in the data.  Please try again\n")
    return found_breed


def make_string_friendly(str: string):
    """
    Modify string to make it easier to compare.
    @param string to modify
    @return string with whitespace stripped and converted to uppercase
    """
    return str.strip().upper()

def parse_breed(breed_set, str: string):
    """
    Compare user input to available choices and look for a match
    @param breed_set: Set of strings representing available choices
    @param str: string to compare to available choices, looking for a match
    @return matched breed or empty string if no match
    """
    friendly_str = make_string_friendly(str)
    if friendly_str in breed_set:
        return friendly_str
    else:
        return ""

def report_total_registrations(df: pd.DataFrame, found_breed: str):
    """
    Print out the total number of registrations for the selected breed in the data
    @param: df - the dataframe
    @param: found_breed - the breed to use for search
    """
    total_reg = df.loc[(found_breed, slice(None)), :].Total.sum()
    print("There have been " + str(total_reg) + " " + found_breed + " dogs registered total.")
    
def list_years_with_breed(year_range, df: pd.DataFrame, found_breed: str):
    """
    Print out all the years that have the breed, along with their percentages of the total
    @param: year_range - the years to check
    @param: df - the dataframe
    @param: found_breed - the breed to use for search
    """
    df_unstacked = df.reset_index()
    years_with_breed = set()

    ### generate list of years where breed exists
    for year in year_range:
        breed_mask = df_unstacked["Breed"] == found_breed
        year_mask = df_unstacked["Year"] == int(year)
        breed_year_mask = breed_mask & year_mask
        breed_year_data = df_unstacked[breed_year_mask]
        breed_year_total = breed_year_data.Total.sum()
        if breed_year_total > 0:
            years_with_breed.add(str(year))
    years_with_breed_list = list(years_with_breed)
    years_with_breed_list.sort()
    years_with_breed_str: string = " ".join(years_with_breed_list)
    print("The " + found_breed + " was found in the years: " + years_with_breed_str)

    # For each found year, report percentage of this breed over total
    for year in years_with_breed_list:
        total_for_year = df.loc[(slice(None), int(year)), :]
        breed_year_data = df.loc[(found_breed, int(year)), :]
        breed_year_total = breed_year_data.Total.sum()
        total_for_year_total = total_for_year.Total.sum()
        percent = 100.0 * breed_year_total / total_for_year_total
        print("The {0} was {1:9.6f}% of top breeds in {2}".format(found_breed, percent, year))

    ### IndexSlice
    # report percentage over all years
    breed_all_time_slice = pd.IndexSlice
    breed_all_time = df.loc[(breed_all_time_slice[found_breed, :])].Total.sum()
    total_all_time = df.Total.sum()
    percent = 100.0 * breed_all_time / total_all_time
    print("The {0} was {1:9.6f}% of top breeds across all years".format(found_breed, percent))

def list_most_popular_months(df: pd.DataFrame, found_breed: str):
    """
    Report the months that appear the most within the data for a given breed
    @param df: the dataframe
    @param found_breed: the breed to analyze
    """
    df_unstacked = df.reset_index()
    number_of_monthly_appearances = df_unstacked[df_unstacked["Breed"] == found_breed].groupby('Month')['Month'].count()
    max_number_of_monthly_appearances = number_of_monthly_appearances.max()
    most_popular_months = number_of_monthly_appearances[number_of_monthly_appearances == max_number_of_monthly_appearances]
    print("The most popular month(s) for " + str(found_breed) + " dogs: ")
    print(*most_popular_months.index)

def main():

    print("ENSF 692 Dogs of Calgary")

    # Import file into MultiIndex Dataframe
    df = import_file("CalgaryDogBreeds.xlsx")

    # local variables
    breed_set = {item[0] for item in df.index}
    year_range = range(2021, 2023 + 1, 1)

    # User input stage
    found_breed = prompt_user_for_breed(breed_set)

    # Report total of registrations
    report_total_registrations(df, found_breed)

    # Report breed statistics by year
    list_years_with_breed(year_range, df, found_breed)

    # Report most popular months for breed
    list_most_popular_months(df, found_breed)


if __name__ == '__main__':
    main()
