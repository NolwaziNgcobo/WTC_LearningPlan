#create two functions namely convert and main. These convert :) and :( to emoji characters and call main function.

def main():
    message = input('How are you feeling? ')
    print(convert(message))


def convert(words):

    #replace :) and :( by splitting and joining the string
    words = words.split(":)")
    words = "🙂".join(words)

    words = words.split(":(")
    words = "🙁".join(words)
    return words


main()
