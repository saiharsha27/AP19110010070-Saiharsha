def camel_case():
    import camelcase
    import emoji
    import pyttsx3
    data = input("Enter the data: ")
    x = camelcase.CamelCase()
    count = 0
    for i in data.split(' '):
        if i != i.capitalize():
            count = 1
    if count == 0:
        print(emoji.emojize(':thumbs_up:'))
    else:
        string = x.hump(data)
        print(string)
        spk = pyttsx3.init()
        spk.say("Successfully converted your data into camelcase")
        spk.runAndWait()