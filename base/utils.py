def greeting(currentime):
    if currentime.hour < 12:
        return('Good morning.')
    elif 12 <= currentime.hour < 18:
        return('Good afternoon.')
    else:
        return('Good evening.')