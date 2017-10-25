import os
import shutil
from operator import itemgetter


def main():
    os.chdir('FilesToSort')
    print(os.getcwd())
    extensions = {}
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            extension = filename.split(".")
            extension = extension[1]
            if extension not in extensions:
                extensions[extension] = "placeholder"
    categorys = []
    for extension in extensions:
        prompt = "What category would you like to sort "+str(extension)+" files into?"
        category = input(prompt)
        extensions[extension] = category
        categorys.append(category)
    print(set(categorys))
    print(extensions)

    for category in set(categorys):
        try:
            os.mkdir(category)
        except:
            print("directorys already created")

    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            if filename.split(".")[1] in extensions:

            print(extension)

main()