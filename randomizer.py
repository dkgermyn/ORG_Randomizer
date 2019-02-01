import random

def randomize_participants():
    # Get input from user for all rostered troopers and roster cap
    signups = input("Enter the names of all rostered members, separated by commas: ")
    roster_cap = int(input("Enter the roster cap: "))

    # Convert that input into a list
    signup_list = [member for member in signups.split(",")]

    # Clean up the list by removing leading and trailing whitespace from each entry
    for index, string in enumerate(signup_list):
        signup_list[index] = string.rstrip().lstrip()

    # Randomize the order of all entries in the list
    random.shuffle(signup_list)

    # Create a new empty "participants" list and a count of participating troopers, starting from zero
    number_of_participants = 0
    participant_list = []

    print("There's {rostered} rostered member(s)".format(rostered=len(signup_list)))
    print("The roster cap is {cap} member(s)".format(cap=roster_cap))

    # Keep adding a random rostered trooper from the signup list to the new "participants" list
    # until we hit the roster cap, or until the signup list is empty, whichever comes first
    while (number_of_participants < roster_cap) and (len(signup_list) > 0):
        # take a member from the signup list
        participant = signup_list.pop()
        # add them to the participant list
        participant_list.append(participant)
        # increment "number of participants"
        number_of_participants += 1

    # finally, print our new list of randomized troopers
    print("Your participants are {participants}".format(participants=participant_list))

if __name__ == "__main__":
    randomize_participants()
