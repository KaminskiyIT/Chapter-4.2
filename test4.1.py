def listToString(myList):
    myStr = ''
    for i in range(len(myList)):
        myStr += myList[i]
        if i == len(myList)-2:
            myStr += ' and '
        elif i < len(myList)-2:
            myStr += ', '

    print(myStr)

spam = ['apples', 'bananas', 'tofu', 'cats']
listToString(spam)
