from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    print(os.getenv("TEST"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/