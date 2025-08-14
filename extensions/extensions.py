def main():
    word = input('File name: ').strip().lower()
    print(file_name(word))


def file_name(name):

    if name.endswith('.gif'):
        return 'image/gif'

    elif name.endswith('.jpg') or name.endswith('.jpeg'):
        return 'image/jpeg'

    elif name.endswith('.png'):
        return 'image/png'

    elif name.endswith('.pdf'):
        return 'application/pdf'

    elif name.endswith('.txt'):
        return 'text/plain'

    elif name.endswith('.zip'):
        return 'application/zip'

    else:
        return 'application/octet-stream'
    

main()

