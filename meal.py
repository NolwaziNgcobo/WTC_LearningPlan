def main():
    #ask user for the time
    time = input ('What time is it? ')

    #change given time into a number we can compare
    time_now = convert(time)

    if time_now >= 7.0 and time_now <= 8.0:
        print('breakfast time')
    
    elif time_now >= 12.0 and time_now <= 13.0:
        print('lunch time')
    
    elif time_now >= 18.0 and time_now <= 19.0:
        print ('dinner time')




def convert(time):
    #split the given time into hours and minutes
    time_parts = time.split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1])

    #change minutes into a fraction of an hour
    minutes_in_hour = minutes / 60

    #add the hours and minutes together and return
    return hours + minutes_in_hour

if __name__ == "__main__":
    main()