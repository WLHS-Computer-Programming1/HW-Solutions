def main():
    # Read the weather condition and number of participants from the user
    weather = input("Enter the weather condition (sunny or rainy): ").lower()
    participants = int(input("Enter the number of participants: "))

    # Determine the suggested activity based on combined conditions
    if weather == 'sunny' and participants < 5:
        activity = "A small group hike would be enjoyable"
    elif weather == 'sunny' and participants >= 5:
        activity = "A team sport like soccer or volleyball at the park."
    elif weather == 'rainy' and participants < 5:
        activity = "Board games or a movie indoors would be cozy."
    elif weather == 'rainy' and participants >= 5:
        activity = "Organize a group indoor trivia or a large board game session."

    # Print the suggested activity
    print(activity)

if __name__ == '__main__':
    main()