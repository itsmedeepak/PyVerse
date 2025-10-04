while True:
    print('\n--- Temperature Converter ---')
    print('Choose a scale to convert from:')
    print('1. Celsius')
    print('2. Fahrenheit')
    print('3. Kelvin')
    print('4. Exit')

    choose = input('Enter 1, 2, 3 or 4: ')

    if choose == '4':
        print("Goodbye 👋")
        break

    temp = float(input('Enter temperature: '))

    if choose == '1':  # Celsius
        print('1. Convert to Fahrenheit')
        print('2. Convert to Kelvin')
        a = input('Enter 1 or 2: ')
        if a == '1':
            result = (temp * 9/5) + 32
            print(f"{temp}°C = {round(result, 2)}°F")
        else:
            result = temp + 273.15
            print(f"{temp}°C = {round(result, 2)}K")

    elif choose == '2':  # Fahrenheit
        print('1. Convert to Celsius')
        print('2. Convert to Kelvin')
        a = input('Enter 1 or 2: ')
        if a == '1':
            result = (temp - 32) * 5/9
            print(f"{temp}°F = {round(result, 2)}°C")
        else:
            result = (temp + 459.67) * 5/9
            print(f"{temp}°F = {round(result, 2)}K")

    elif choose == '3':  # Kelvin
        print('1. Convert to Celsius')
        print('2. Convert to Fahrenheit')
        a = input('Enter 1 or 2: ')
        if a == '1':
            result = temp - 273.15
            print(f"{temp}K = {round(result, 2)}°C")
        else:
            result = (temp - 273.15) * 9/5 + 32
            print(f"{temp}K = {round(result, 2)}°F")

    else:
        print("❌ Invalid choice. Try again.")

    input('Press Enter to continue...')