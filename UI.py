import time

def main():

    while True:
        print('**********************************************************************************************')
        input_value = input("Please enter 'start' to start the program -> ")
        print('\n')
        print("At any point in the program type 'help' for more information")
        print("At any point in the program type 'stop' to stop the program")
        print("At any point in the program type 'restart' to restart the program")
        print('\n')
        if input_value == 'start':
            print('**********************************************************************************************')
            print("Welcome to Money converter!!!")
            print("-Purpose of money converter is to see the perceived value of the american dollar to other forms of currency, so that the user is informed of equivalent value")
            print("-Process will require a few inputs of data and will complete the currency conversion in a few seconds so please be patient")
            print("-Thank you")
            print('\n')
            print("[+]Please enter the amount of money you have in American dollars!!!")
            print("-Please disregard the $ sign when inputting the dollar amount")
            print("\n")
            input_value_a = input(">>Enter response here: ")


            if input_value_a == 'help':
                print('**********************************************************************************************')
                print("This is the help page!")
                print("\n")
                print("If you are in need of assistance please contact us at our number 000-000-0000")
                

            if input_value_a == 'stop':
                break

            if input_value_a == 'restart':
                continue

            print('\n')
            print("[+]Please enter the currency you would like to convert to!!!")
            print("-For example, conversion to yen can be entered as word form 'yen' or symbol form '¥'")
            print('-Available conversions at the moment:')
            print('     -> American Dollars to Japanese Yen ($ -> ¥)')
            print('\n')
            input_value_2 = input(">>Enter response here: ")

            if input_value_2 == 'help':
                print('**********************************************************************************************')
                print("This is the help page!")
                print("\n")
                print("If you are in need of assistance please contact us at out number 000-000-0000")
                print("You will now be redirected to the beginning of the program")
                print('**********************************************************************************************')
                

            if input_value_2 == 'stop':
                break

            if input_value_2 == 'restart':
                continue

            var = open("converter.txt", 'w')
            var.write(input_value_a)
            var.close()
            time.sleep(4)

            var_2 = open("currency.txt", "w")
            var_2.write(input_value_2)
            var_2.close()
            time.sleep(4)

            var_3 = open("converter.txt", "r")
            var_line_3 = var_3.readline()
            var_3.close()
            time.sleep(4)

            if input_value_a == 'help' or input_value_2 == 'help':
                print("One of your inputs had an incorrect input. Please try again!")
                continue
            elif input_value_a == 'stop' or input_value_2 == 'stop':
                print("One of your inputs had an incorrect input. Please try again!")
                continue
            elif input_value_a == 'restart' or input_value_2 == 'restart':
                print("One of your inputs had an incorrect input. Please try again!")
                continue
            else:
                print('**********************************************************************************************')
                print(f'From American Dollars to {input_value_2} the conversion came out to be {var_line_3}')

        else:
            return
        

if __name__ == '__main__':
    main()
