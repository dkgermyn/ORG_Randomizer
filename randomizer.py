import random
from collections import deque

def randomize_participants():

    signups = ""
    roster_cap = 0
    locked_members = []

    # Get input from user for all rostered troopers and roster cap
    try:
        signups = input("Enter the names of all rostered members, separated by commas: ")
        roster_cap = int(input("Enter the roster cap: "))
    except ValueError as e:
        print("Error with input: You didn't provide a valid roster cap number!")
        exit()
    finally:
        # some quick input validation
        if not signups:
            print("Error: you didn't provide any names!")
            exit()

    # Ask if any slots are locked
    locked_slots = False
    number_of_locked_slots = 0
    try:
        number_of_locked_slots = int(input("How many slots are locked?  (Press 'Enter' for none)") or False)
    except ValueError as e:
        print("Something went wrong: {e}".format(e=e))
    finally:
        if number_of_locked_slots > 0:
            locked_slots = True

    # Convert that input into a list
    signup_list = deque([member for member in signups.split(",")])

    # Clean up the list by removing leading and trailing whitespace from each entry
    for index, string in enumerate(signup_list):
        signup_list[index] = string.rstrip().lstrip()

    # if there are locked slots, lock them before randomizing the list
    if locked_slots:
        print("There are {number} locked slots, holding on to them...".format(number=number_of_locked_slots))
        for x in range (0, number_of_locked_slots):
            member = signup_list.popleft()
            locked_members.append(member)

    # Randomize the order of all entries in the list
    random.shuffle(signup_list)

    print("{rostered} rostered member(s)".format(rostered=len(signup_list)))
    print("Roster cap is {roster_cap} member(s)".format(roster_cap=roster_cap))

    # return the randomized list, but split it up so we can see rostered / waitlisted
    signup_list = list(signup_list)
    roster = signup_list[0:roster_cap]
    waitlist = signup_list[roster_cap:]

    print("Here is the roster for the event:\n"
          "ROSTERED MEMBERS: ")
    # if there are locked slots, announce them...
    if locked_slots:
        print("LOCKED SLOTS: ")
        for member in locked_members:
            print(member)
        print("RANDOMIZED SLOTS: ")

    for member in roster:
        print(member)

    if waitlist:
        print("WAITLISTED MEMBERS: ")
        for member in waitlist:
            print(member)
    else:
        pass

if __name__ == "__main__":
    randomize_participants()
