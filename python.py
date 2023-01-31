color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')




while color != "quit":
    if color == 'green':
        print("Go")
    elif color == "yellow":
        print('wait')
    else:
        print("bogus")
    break