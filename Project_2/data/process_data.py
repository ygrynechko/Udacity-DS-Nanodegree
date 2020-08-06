import re
import sys

import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    This function is going to load data from two csv files
    INPUT:
    messages_filepath - location and name of the first csv file
    categories_filepath - location and name of the second csv file
    OUTPUT:
    df - merged dataframe containing data form both CSVs
    """

    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')
    return df


def clean_data(df):
    """
    This function is going to clean the data.
    INPUT:
    df- dataframe with merged data from messages and categories csvs
    OUTPUT:
    df - cleaned dataframe
    """
    # Split categories into separate rows
    categories = df['categories'].str.split(";", expand=True)

    # Create column names for categories
    columns = re.sub('[012;-]', ' ', df['categories'].iloc[0]).split()

    # Assign new column names
    categories.columns = columns

    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1:]

        # convert column from string to numeric
        categories[column] = categories[column].astype(int)

    # check how many unique values every column has
    # if unique number is 1 we can drow that column

    for col in categories:
        if categories[col].nunique() > 2:
            categories.drop(categories.index[categories[col] == 2], inplace=True)

    # drop the original categories column from `df`
    df = df.drop(['categories'], axis=1)

    df = pd.merge(df, categories, left_index=True, right_index=True)

    # drop duplicates
    df = df.drop_duplicates()

    return df


def save_data(df, database_filename):
    """
    This function will save cleaned data to sql database. If the table already
    exists it will be removed before saving.
    INPUT:
    df - dataframe with clean data
    database_filename - name of the database
    """
    # Before saving remove old table if exists
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('df', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories ' \
              'datasets as the first and second argument respectively, as ' \
              'well as the filepath of the database to save the cleaned data ' \
              'to as the third argument. \n\nExample: python process_data.py ' \
              'disaster_messages.csv disaster_categories.csv ' \
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
