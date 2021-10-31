import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Which city do you want to choice? Chicago, New york city, Washington\n')
        if city not in ('Chicago', 'New york city', 'Washington'):
            print("This choice is not exist in our dataset, Try again please: ")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

     months = { '1' : 'january' , 
                '2' : 'february',
                '3' : 'march' ,
                '4' :  'april', 
                '5' :  'may' ,
                '6' : 'june',
                '7' : 'all' }
    x = 1
    while (x >= 1): 
        num = input("Enter the number of month you interested in or all: \n1-january 2-february 3-march 4-april 5-may 6-june 7-all\n")
        if num in months.keys():
            month = months[num]
            if(m != 'all'):
                num = int(num)
                break
        else: 
            print('Please, Enter a valid month number or all: \n')
            x += 1
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Which day do you want to choice? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type all if want to choose all days\n')
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
            print("This day is not exist in our dataset, Try again please: ")
            continue
        else:
            break

    print('-'*40)
    return city,month,num,day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most Common Month is: ", df['month'].mode()[0])
    # TO DO: display the most common day of week
    print("Most Common Day is: ", df['day_of_week'].mode()[0])
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most Common Hour is: ", df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print("Most Commonly used start station is: ", df['Start Station'].value_counts().idxmax())
    # TO DO: display most commonly used end station
    print("Most Commonly used end station is: ", df['End Station'].value_counts().idxmax())
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " : " + df['End Station']
    print("Most Commonly used combination of start station and end station trip is: ", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\nTotal travel time is: ", sum(df['Trip Duration']))
    # TO DO: display mean travel time
    print("\nMean travel time is: ", df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print('User Types is:\n{} '.format(df['User Type'].ValueCounts()))
    # TO DO: Display counts of gender
    if( city == 'chicago' or city == 'new york city' ):
        print('The COUNTS OF GENDER : \n{} '.format(df['Gender'].ValueCounts()))
        # TO DO: Display earliest, most recent, and most common year of birth
        print('The MOST EARLIEST YEAR : {} '.format(int(df['Birth Year'].min())) )
        print('The MOST RECENT  YEAR : {} '.format(int(df['Birth Year'].max())))
        print('The COMMON YEAR : {} '.format(int(df['Birth Year'].mode()[0])))
    else :
        print ('Washington has no gender or birth year data!')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        #getting input data from user city month and day
        city,month,num,day = get_filters()
        print ('You are interested about:\n City: {} Month: {} Month No: {} Day is {}\n'.format(city , month,num,day))
        
        #loading data from csv files 
        #check  for month
        if (month == 'all'):
            df = load_data(city,month, day)
        else:
             df = load_data(city,num, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        #I provided city for user_stats because washington has no data for gender and birth year
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break
if __name__ == "__main__":
	main()
