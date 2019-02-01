import random

def randomize_participants():
    # Get input from user for all rostered troopers and roster cap
    try:
        signups = input("Enter the names of all rostered members, separated by commas: ")
        roster_cap = int(input("Enter the roster cap: "))
    except ValueError as e:
        print("Error with input: You didn't provide a valid roster cap number!\n"
              "{e}".format(e=e))
        raise e

    # some quick input validation
    if not signups:
        print("Error: you didn't provide any names!")
        exit()

    # Convert that input into a list
    signup_list = [member for member in signups.split(",")]

    # Clean up the list by removing leading and trailing whitespace from each entry
    for index, string in enumerate(signup_list):
        signup_list[index] = string.rstrip().lstrip()

    # Randomize the order of all entries in the list
    random.shuffle(signup_list)

    print("There is {rostered} rostered member(s)".format(rostered=len(signup_list)))
    print("The roster cap is {cap} member(s)".format(cap=roster_cap))

    # return the randomized list, but split it up so we can see rostered / waitlisted
    roster = [member for member in signup_list[0:roster_cap]]
    waitlist = [member for member in signup_list[roster_cap:]]

    print("Here is the roster for the event:\n"
          "ROSTERED MEMBERS: ")
    for member in roster:
        print(member)

    if not waitlist:
        pass
    else:
        print("WAITLISTED MEMBERS: ")
        for member in waitlist:
            print(member)


if __name__ == "__main__":
    randomize_participants()
