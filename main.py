import os
import sys
import datetime

def getDate():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M:%S.000Z")

def findForbiddenChars(string):
    forbidden = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|", "'"]
    for char in forbidden:
        if char in string:
            return char
    return None

def makeTemplate(name, creator, price, description, preview):
    json = """{
    "name": "TEMPLATE_NAME",
    "creator": "DISCORD_ID",
    "css": "CSS HERE",
    "price": 30,
    "description": "TEMPLATE",
    "created_at": {
      "$date": "2023-04-25T21:52:57.458Z"
    },
    "preview": "IMAGE_URL"
}
    """

    # Sort all the parameters out
    if findForbiddenChars(name) != None:
        sys.exit("Forbidden character ' {} ' found in name".format(findForbiddenChars(name)))
    if findForbiddenChars(creator) != None:
        sys.exit("Forbidden character ' {} ' found in creator".format(findForbiddenChars(creator)))
    if findForbiddenChars(description) != None:
        sys.exit("Forbidden character ' {} ' found in description".format(findForbiddenChars(description)))

    json = json.replace("TEMPLATE_NAME", name)
    json = json.replace("DISCORD_ID", creator)
    json = json.replace("CSS HERE", "")
    json = json.replace("30", price)
    json = json.replace("TEMPLATE", description)
    json = json.replace("2023-04-25T21:52:57.458Z", getDate())
    json = json.replace("IMAGE_URL", preview)

    firstLetter = name[0].upper()
    with open("themes/{}/{}.json".format(firstLetter, name), "w") as f:
        f.write(json)

    
    
    


args = sys.argv[1:]

system = sys.platform



if system == "win32":
    os.system("cls")
if system == "linux":
    os.system("clear")
elif system == "darwin":
    os.system("clear")

if len(args) == 0:
    sys.exit("No arguments provided")

if args[0] == "create":
    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    for letter in letters:
        os.mkdir("themes/" + letter)
        with open("themes/" + letter + "/hello.txt", "w") as f:
            f.write("This is just for git... AKA this file is useless (Just like your life)")

    print("Folders created successfully!")
if args[0] == "delete":
    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    for letter in letters:
        os.remove("themes/" + letter + "/hello.txt")
        os.rmdir("themes/" + letter)

    print("Folders deleted successfully!")
        

if args[0] == "template":
    name = input("Name of template: ")
    creator = input("Creator's Discord ID: ")
    price = input("Price of template: ")
    description = input("Description of template: ")
    preview = input("Preview image URL: ")

    print("\n\n")

    choice = input("Are you sure you want to create a template with the following information? (y/n)\nName: {}\nCreator: {}\nPrice: {}\nDescription: {}\nPreview: {}\n\n> ".format(name, creator, price, description, preview))
    if choice == "y":
        print("Creating template...")
        makeTemplate(name, creator, price, description, preview)
        print("Template created successfully!")
        print("You can find the template in themes/{}/{}.json".format(name[0].upper(), name))
        fullPath = os.path.abspath("themes/{}/{}.json".format(name[0].upper(), name))
        
        print("Full path: {}".format(fullPath))

        openFile = input("Would you like to open the file in your default text editor? (y/n)\n> ")
        if openFile == "y":
            os.startfile(fullPath)
        elif openFile == "n":
            print("Aborting...")
            sys.exit(0)
        else:
            print("Invalid choice")
            sys.exit(0)
    if choice == "n":
        print("Aborting...")
        sys.exit(0)


