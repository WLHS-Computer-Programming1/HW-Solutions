def main():
    IIlII = input("Enter the current weather condition ('sunny' or 'rainy'): ")
    llIIl = int(input("Enter the number of participants: "))

    if IIlII.lower() == "sunny" and llIIl < 5:
        print("A small group hike would be enjoyable.")
    elif IIlII.lower() == "sunny" and llIIl >= 5:
        print("A team sport like soccer or volleyball at the park would be enoyable.")
    elif IIlII.lower() == "rainy" and llIIl < 5:
        print("Board games or a movie indoors would be cozy.")
    elif IIlII.lower() == "rainy" and llIIl >= 5:
        print("Organize a group indoor trivia or a large board game session.")
    else:
        print("Womp womp, looks like you went out of scope :3")

if __name__ == '__main__':
    main()