import os
import shutil


def main():
    os.chdir('FilesToSort')
    print(os.getcwd())
    extensions = []
    categorys = []
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            extension = filename.split(".")[1]
            prompt = "What category would you like to sort " + str(extension) + " files into?"
            if extension not in extensions:
                extensions.append(extension)
                category = input(prompt)
            if category not in categorys:
                os.mkdir(category)
            categorys.append(category)
            shutil.move(filename, category)


main()