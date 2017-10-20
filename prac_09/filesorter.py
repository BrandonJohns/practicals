import os
import shutil


def main():
    os.chdir('FilesToSort')
    print(os.getcwd())
    extensions = []
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            extension = filename.split(".")
            extension = extension[1]
            if extension not in extensions:
                extensions.append(extension)
                try:
                    os.mkdir(extension)
                except:
                    print("directorys already created")
            shutil.move(filename, extension)


main()