# Beautiful soup 4 is used for finding the title, genres of the anime searched
import bs4

# Used to connect to the proposed url
import urllib.request

# Used for finding random numbers when asked
from random import randint

#For reading a file
import time

# Asks the user to input a number so we know what anime to start on
# If the user is lazy then they can have the computer choose
def OneToTenThousand():
    num = input("\nPlease choose a number between 1 - 11000 or choose 0 for a random num ")
    check = True
    while check:
        # Keeps checking if the str is a number
        while not num.isnumeric():
            num = input("\nPlease choose a number between 1 - 11000 or choose 0 for a random num ")
            check = False
        # Checks if the number is 0 which means that the computer chooses the number
        if int(num) is 0:
            num = randint(1, 11000)
            return num
        # Checks if the number is out-of-bounds
        if int(num) > 11000 or int(num) < 1:
            num = input("\nPlease choose a number between 1 - 11000 or choose 0 for a random num ")
            check = True
        # Checks if the number is a number and in-bounds
        if num.isnumeric() and int(num) <= 11000 and int(num) >= 1:
            return num

def UserInputsIfTheyWantMoreThanOneGenre():
    # Makes the console look better and more decorated
    print("  _    __  __   __    __  __     _\n /_\   ||\ ||   ||   | |\/| |   |_ \n/   \  || \||   ||   | |  | |   |_")
    # Warns the user of the data usage
    print("Welcome to the anime searcher. \nConnect to a Wi-Fi source as this program searches online and takes up alot of data")
    print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////\n    Notice:\n    This program is essentially a crawler. It will take a while to collect all the anime. \n    This is why you need to connect to a Wi-Fi source \n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/////////////////////////")
    search1ormore = ""
    # Checks the 4 or 1 genre(s) that the user wants to search
    while search1ormore not in ("1", "0"):
        search1ormore = input("\nDo you want to search for more than one anime genre? \nThe base genre is action \nTrue: 1 (Action, Drama, Adventure, Sci-Fi) \nFalse: 0 (Action) \nEnter your response here: \n")
    return search1ormore

def GetWebPageNum():
    # Sees how many webpages the user would like to search
    # This is for reducing the data usage if you have a limited data plan
    num = input("\nHow many webpages do you want to search (1 - 11000) or choose 0 for a random num ")
    check = True
    while check:
        # Keeps checking if the str is a number
        while not num.isnumeric():
            num = input("\nPlease choose a number between (1 - 11000) or choose 0 for a random num ")
            check = False
        # Checks if the number is 0 which means that the computer chooses the number
        if int(num) is 0:
            num = randint(1, 11000)
            return num
        # Checks if the number is out-of-bounds
        if int(num) > 11000 or int(num) < 1:
            num = input("\nPlease choose a number between (1 - 11000) or choose 0 for a random num ")
            check = True
            # Checks if the number is a number and in-bounds)
            # Keeps checking if the str is a number
        if num.isnumeric() and int(num) <= 11000 and int(num) >= 1:
            return num
def ReadOrWrite():
    answer = ""
    while not answer == "1" or answer == "2":
        answer = input("Do you want to read or write? 1. Read 2. Write: ")
        while not answer.isnumeric():
            print("\n Oopsie you didn't type a correct number please try again")
            answer = input("Do you want to read or write? 1. Read 2. Write: \n")
        if answer == "1" or answer == "2":
            return answer


def getreq(num):
    responsedef = urllib.request.urlopen("https://myanimelist.net/anime/" + str(num))
    return responsedef

RorW = ReadOrWrite()
if RorW == "2":
    file = open("Anime", "w")
    filecount = 1
    AnimeGenre = UserInputsIfTheyWantMoreThanOneGenre()
    # Helps with finding out the url of the anime. Turns previous count obj(str) into new count obj(int) for future mathematical use.
    count = OneToTenThousand()
    count = int(count)
    # Breakout is a variable that breaks out of the loop. This prevents the unnecessary use of data usage and computing power.
    breakout = 0
    # Determines how many websites the program searches. Further prevents unnecessary data and computational power use.
    animenum = GetWebPageNum()

    for i in range(int(animenum)):
        # Try-exception loop used due to the fact that some urls cannot be found
        try:
            # Connects to the url provided
            response = getreq(count)
            # Downloads and parses the html using beautiful soup and store in variable `soup`
            soup = bs4.BeautifulSoup(response, 'html.parser')

            # Sees if the anime consists of the chosen genres and prints it's findings
            if AnimeGenre is 1:
                if soup.find_all("a", title="Drama") or soup.find_all("a", title="Action") or soup.find_all("a", title="Adventure") or soup.find_all("a", title="Sci-Fi"):
                    # Gets the title of the anime
                    title = soup.title
                    newstr = title.text
                    # Cuts - My Anime List out of the string
                    newstr = newstr[:-18]
                    # Prints the anime and it's url
                    print("\nYour anime is: " + newstr + " \nTo find it on the internet please use this url: " + "https://myanimelist.net/anime/" + str(count) + "\n")
                    breakout = 0
                    filecount += 1
                    filestring = "\nYour anime is: " + newstr + " \nTo find it on the internet please use this url: " + "https://myanimelist.net/anime/" + str(count) + "\n"
                    file.write(filestring)
            # Sees if the anime consists of the chosen genres and prints it's findings
            else:
                if soup.find_all("a", title="Action"):
                    # Gets the title of the anime
                    title = soup.title
                    newstr = title.text
                    # Cuts - My Anime List out of the string
                    newstr = newstr[:-18]
                    # Prints the anime and it's url
                    print("\nThe anime is: " + newstr + " \nTo find it on the internet please use this url: " + "https://myanimelist.net/anime/" + str(count) + "\n")
                    breakout = 0
                    filecount += 1
                    filestring = "\nYour anime is: " + newstr + " \nTo find it on the internet please use this url: " + "https://myanimelist.net/anime/" + str(count) + "\n"
                    file.write(filestring)
            count += 1
        except:
            count += 1
            breakout += 1
            if breakout >= 100:
                break
    file.close()
else:
    with open("Anime", "r") as file:
        for line in file:
            print(line)
        time.sleep(0.5)
        file.close()

