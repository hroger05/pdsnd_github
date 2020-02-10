import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. Avoids error if input not available.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("What city would you like to explore? Choose: Chicago, New York City, or Washington: ").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("I\'m sorry, that choice is unavailable. Please choose from the cities Chicago, New York City, or Washington: ")
        else:
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("What month would you like to explore? Choose: All, or any month from January to June: ").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("I\'m sorry, that choice is unavailable. Please choose any month from January to June, or just type \'all\': ")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("What day of the week would you like to explore? Choose: All, or any day of the week: ").lower()
        if day not in ('all','saturday','sunday','monday','tuesday','wednesday','thursday','friday'):
            print("I\'m sorry, that choice is unavailable. Please choose any day of the week, or just type \'all\': ")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('-'*40)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("Most Common Month of Travel: {}\n".format(common_month))

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most Common Day of Travel: {}\n".format(common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most Common Hour of Travel: {}\n".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations:"""

    print('-'*40)
    print('\nCalculating The Most Popular Stations:...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("Most Common Station for Beginning of Travel: {}\n".format(common_start))

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("Most Common Station for End of Travel: {}\n".format(common_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('-'*40)
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['travel_time'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    total_time = df['travel_time'].sum()
    print("Total Travel Time: {}\n".format(total_time))

    # display mean travel time

    mean_time = df['travel_time'].mean()
    print("Average Travel Time: {}\n".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('-'*40)
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\n\nNumber of Users, by Type: \n")
    print(df['User Type'].value_counts())

    # Display counts of gender
    print("\n\nNumber of Users, by Gender: \n")
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print('I\'m sorry, there is no gender data available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)

        while True:
            block1 = input('\nWould you like to see stats on usage by station? Enter yes or no.\n')
            if block1 not in ('yes','no'):
                block1 = input('\nI\'m sorry, I didn\'t understand. Would you like to see stats on usage by station? Enter yes or no.\n')
            else:
                break

        if block1.lower() == 'yes':
            station_stats(df)


        while True:
            block2 = input('\nWould you like to see stats on trip duration? Enter yes or no.\n')
            if block2 not in ('yes','no'):
                block2 = input('\nI\'m sorry, I didn\'t understand. Would you like to see stats on trip duration? Enter yes or no.\n')
            else:
                break

        if block2.lower() == 'yes':
            trip_duration_stats(df)


        while True:
            block3 = input('\nWould you like to see stats on users? Enter yes or no.\n')
            if block3 not in ('yes','no'):
                block3 = input('\nI\'m sorry, I didn\'t understand. Would you like to see stats on users? Enter yes or no.\n')
            else:
                break

        if block3.lower() == 'yes':
            user_stats(df)


        restart2 = input('\nWould you like to restart? Enter yes or no.\n')
        if restart2.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
