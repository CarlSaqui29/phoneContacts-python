import array as rawr

contacts = rawr.array('d', [])
contacts_2 = rawr.array('d', [])
contacts_3 = rawr.array('d', [])
list_1 = []
list_2 = []
list_3 = []
country_num = '+63'
country = 'Philippines'
phil = 1
thai = 0
US = 0

a = 0
i = 0
l = 0
s = 0
v = 0

a_2 = 0
i_2 = 0
l_2 = 0
s_2 = 0
v_2 = 0

a_3 = 0
i_3 = 0
l_3 = 0
s_3 = 0
v_3 = 0

while True:
    print('My Contacts (' + country + ')\n')
    print('(a) Add Contacts\n(b) Remove Contacts\n(c) Search Contact\n(d) View Contacts\n(e) Update Contacts\n(f) Settings\n(0) Exit')
    choice = input('--> ')

    if choice == 'a' or choice == 'A':
        if phil == 1:
            print('My Contacts (' + country + ')\n')
            new = None
            name = None
            while True:
                name = input('Name: ')
                if name and name.strip() and name.isalpha():
                    break
                else:
                    print('Invalid Input!')
            while name in list_1:
                print(name + ' is already in the contacts!')
                while True:
                    name = input('Name: ')
                    if name and name.strip():
                        break
                    else:
                        print('You entered nothing!')
            while True:
                new = input('Number: '+ country_num)
                if new and new.strip():
                    try:
                        val = int(new)
                        count = 0
                        new = int(new)
                        old = None
                        old = new
                        while (old > 0):
                            old = old // 10
                            count = count + 1
                        if count == 10 and new > 9010000000:
                            break
                        else:
                            print("Error! Enter the 10 digit number. ex: 9752751625")
                    except ValueError:
                        print("Invalid Input!")
                else:
                    print('Invalid Input!')


            new = float(new)
            list_1.append(name)
            contacts.insert(i, new)
            print(name + ' is Added in the Contacts.\n')
            i += 1
            l += 1
            s += 1
            v += 1
            a += 1

        if thai == 1:
            print('My Contacts (' + country + ')\n')
            new = None
            name = None
            while True:
                name = input('Name: ')
                if name and name.strip() and name.isalpha():
                    break
                else:
                    print('Invalid Input!')
            while name in list_2:
                print(name + ' is already in the contacts!')
                while True:
                    name = input('Name: ')
                    if name and name.strip():
                        break
                    else:
                        print('You entered nothing!')
            while True:
                new = input('Number: ' + country_num)
                if new and new.strip():
                    try:
                        val = int(new)
                        count = 0
                        new = int(new)
                        old = None
                        old = new
                        while (old > 0):
                            old = old // 10
                            count = count + 1
                        if count == 10 and new > 0:
                            break
                        else:
                            print("IError! Enter the 10 digit number. First digit must not be 0")
                    except ValueError:
                        print("Invalid Input!")
                else:
                    print('Invalid Input!')

            new = float(new)
            list_2.append(name)
            contacts_2.insert(i, new)
            print(name + ' is Added in the Contacts.\n')
            i_2 += 1
            l_2 += 1
            s_2 += 1
            v_2 += 1
            a_2 += 1

        if US == 1:
            print('My Contacts (' + country + ')\n')
            new = None
            name = None
            while True:
                name = input('Name: ')
                if name and name.strip() and name.isalpha():
                    break
                else:
                    print('Invalid Input!')
            while name in list_3:
                print(name + ' is already in the contacts!')
                while True:
                    name = input('Name: ')
                    if name and name.strip():
                        break
                    else:
                        print('You entered nothing!')
            while True:
                new = input('Number: ' + country_num)
                if new and new.strip():
                    try:
                        val = int(new)
                        count = 0
                        new = int(new)
                        old = None
                        old = new
                        while (old > 0):
                            old = old // 10
                            count = count + 1
                        if count == 10 and new > 0:
                            break
                        else:
                            print("Error! Enter the 10 digit number. First digit must not be 0")
                    except ValueError:
                        print("Invalid Input!")
                else:
                    print('Invalid Input!')

            new = float(new)
            list_3.append(name)
            contacts_3.insert(i, new)
            print(name + ' is Added in the Contacts.\n')
            i_3 += 1
            l_3 += 1
            s_3 += 1
            v_3 += 1
            a_3 += 1

    if choice == 'b' or choice == 'B':
        if phil == 1:
            print('My Contacts (' + country + ')\n')
            if l >= 1:
                while True:
                    print('(e) back')
                    name_delete = input("Remove: ")
                    if name_delete and name_delete.strip():
                        if name_delete == 'e' or name_delete == 'E':
                            break
                        if name_delete in list_1:
                            search = list_1.index(name_delete)
                            del contacts[search]
                            list_1.remove(name_delete)
                            print(name_delete + ' has been Deleted.')
                            i -= 1
                            l -= 1
                            s -= 1
                            v -= 1
                            break
                        else:
                            print(name_delete + ' is not in the Contacts.\n')
            else:
                print('No contacts to be deleted.\n')

        if thai == 1:
            print('My Contacts (' + country + ')\n')
            if l_2 >= 1:
                while True:
                    print('(e) back')
                    name_delete = input("Remove: ")
                    if name_delete and name_delete.strip():
                        if name_delete == 'e' or name_delete == 'E':
                            break
                        if name_delete in list_2:
                            search = list_2.index(name_delete)
                            del contacts_2[search]
                            list_2.remove(name_delete)
                            print(name_delete + ' has been Deleted.')
                            i_2 -= 1
                            l_2 -= 1
                            s_2 -= 1
                            v_2 -= 1
                            break
                        else:
                            print(name_delete + ' is not in the Contacts.\n')
            else:
                print('No contacts to be deleted.\n')

        if US == 1:
            print('My Contacts (' + country + ')\n')
            if l_3 >= 1:
                while True:
                    print('(e) back')
                    name_delete = input("Remove: ")
                    if name_delete and name_delete.strip():
                        if name_delete == 'e' or name_delete == 'E':
                            break
                        if name_delete in list_3:
                            search = list_3.index(name_delete)
                            del contacts_3[search]
                            list_3.remove(name_delete)
                            print(name_delete + ' has been Deleted.')
                            i_3 -= 1
                            l_3 -= 1
                            s_3 -= 1
                            v_3 -= 1
                            break
                        else:
                            print(name_delete + ' is not in the Contacts.\n')
            else:
                print('No contacts to be deleted.\n')

    if choice == 'c' or choice == 'C':
        if phil == 1:
            print('My Contacts (' + country + ')\n')
            if s >= 1:
                while True:
                    print('(e) back')
                    search_name = input('Search: ')
                    if search_name and search_name.strip():
                        if search_name == 'e' or search_name == 'E':
                            break
                        if search_name in list_1:
                            search = list_1.index(search_name)
                            print(search_name,country_num + str(round(contacts[search])), '\n')
                            break
                        else:
                            print(search_name + ' is not in the Contacts.')
            else:
                print('No contacts to be searched.\n')
        if thai == 1:
            print('My Contacts (' + country + ')\n')
            if s_2 >= 1:
                while True:
                    print('(e) back')
                    search_name = input('Search: ')
                    if search_name and search_name.strip():
                        if search_name == 'e' or search_name == 'E':
                            break
                        if search_name in list_2:
                            search = list_2.index(search_name)
                            print(search_name,country_num + str(round(contacts_2[search])), '\n')
                            break
                        else:
                            print(search_name + ' is not in the Contacts.')
            else:
                print('No contacts to be searched.\n')
        if US == 1:
            print('My Contacts (' + country + ')\n')
            if s_3 >= 1:
                while True:
                    print('(e) back')
                    search_name = input('Search: ')
                    if search_name and search_name.strip():
                        if search_name == 'e' or search_name == 'E':
                            break
                        if search_name in list_3:
                            search = list_3.index(search_name)
                            print(search_name,country_num + str(round(contacts_3[search])), '\n')
                            break
                        else:
                            print(search_name + ' is not in the Contacts.')
            else:
                print('No contacts to be searched.\n')

    if choice == 'd' or choice == 'D':
        if phil == 1:
            print('My Contacts (' + country + ')\n')
            if v >= 1:
                a=0
                for x in contacts:
                    print(str(list_1[a]) + " " + country_num + str(round(x)))
                    a+=1
                while True:
                    print('\n(e) back    (0) exit')
                    back = input('--> ')
                    if back == 'e' or back == 'E':
                        break
                    elif back == '0':
                        print('goodbye!')
                        quit()
                    else:
                        print('Please enter e or 0 only.')
            else:
                print('No contacts to be Viewed.\n')
        if thai == 1:
            print('My Contacts (' + country + ')\n')
            if v_2 >= 1:
                a_2=0
                for x in contacts_2:
                    print(str(list_2[a_2]) + " " + country_num + str(round(x)))
                    a_2+=1
                while True:
                    print('\n(e) back    (0) exit')
                    back = input('--> ')
                    if back == 'e' or back == 'E':
                        break
                    elif back == '0':
                        print('goodbye!')
                        quit()
                    else:
                        print('Please enter e or 0 only.')
            else:
                print('No contacts to be Viewed.\n')
        if US == 1:
            print('My Contacts (' + country + ')\n')
            if v_3 >= 1:
                a_3=0
                for x in contacts_3:
                    print(str(list_3[a_3]) + " " + country_num + str(round(x)))
                    a_3+=1
                while True:
                    print('\n(e) back    (0) exit')
                    back = input('--> ')
                    if back == 'e' or back == 'E':
                        break
                    elif back == '0':
                        print('goodbye!')
                        quit()
                    else:
                        print('Please enter e or 0 only.')
            else:
                print('No contacts to be Viewed.\n')


    if choice == 'e' or choice == 'E':
        if phil == 1:
            print('My Contacts (' + country + ')\n')
            if s >= 1:
                while True:
                    print('(e) back')
                    update_name = input('Update: ')
                    if update_name and update_name.strip():
                        if update_name == 'e' or update_name == 'E':
                            break
                        if update_name in list_1:
                            search = list_1.index(update_name)
                            print(update_name + " " + country_num + str(round(contacts[search])))
                            while True:
                                new_num = input('New number: ' + country_num)
                                if new_num and new_num.strip():
                                    try:
                                        val = int(new_num)
                                        count = 0
                                        new = int(new_num)
                                        old = None
                                        old = new
                                        while (old > 0):
                                            old = old // 10
                                            count = count + 1
                                        if count == 10:
                                            contacts[search] = new
                                            print('New number of', update_name, 'has been saved.\n')
                                            break
                                        else:
                                            print("Error! Enter the 10 digit number.")
                                    except ValueError:
                                        print("Invalid Input!")
                            break
                        else:
                            print(update_name + ' is not in the Contacts.')
            else:
                print('No contacts to be update.\n')

        if thai == 1:
            print('My Contacts (' + country + ')\n')
            if s_2 >= 1:
                while True:
                    print('(e) back')
                    update_name = input('Update: ')
                    if update_name and update_name.strip():
                        if update_name == 'e' or update_name == 'E':
                            break
                        if update_name in list_2:
                            search = list_2.index(update_name)
                            print(update_name + " " + country_num + str(round(contacts_2[search])))
                            while True:
                                new_num = input('New number: ' + country_num)
                                if new_num and new_num.strip():
                                    try:
                                        val = int(new_num)
                                        count = 0
                                        new = int(new_num)
                                        old = None
                                        old = new
                                        while (old > 0):
                                            old = old // 10
                                            count = count + 1
                                        if count == 10:
                                            contacts_2[search] = new
                                            print('New number of', update_name, 'has been saved.\n')
                                            break
                                        else:
                                            print("Error! Enter the 10 digit number.")
                                    except ValueError:
                                        print("Invalid Input!")
                            break
                        else:
                            print(update_name + ' is not in the Contacts.')
            else:
                print('No contacts to be update.\n')


        if US == 1:
            print('My Contacts (' + country + ')\n')
            if s_3 >= 1:
                while True:
                    print('(e) back')
                    update_name = input('Update: ')
                    if update_name and update_name.strip():
                        if update_name == 'e' or update_name == 'E':
                            break
                        if update_name in list_3:
                            search = list_3.index(update_name)
                            print(update_name + " " + country_num + str(round(contacts_3[search])))
                            while True:
                                new_num = input('New number: ' + country_num)
                                if new_num and new_num.strip():
                                    try:
                                        val = int(new_num)
                                        count = 0
                                        new = int(new_num)
                                        old = None
                                        old = new
                                        while (old > 0):
                                            old = old // 10
                                            count = count + 1
                                        if count == 10:
                                            contacts_3[search] = new
                                            print('New number of', update_name, 'has been saved.\n')
                                            break
                                        else:
                                            print("Error! Enter the 10 digit number.")
                                    except ValueError:
                                        print("Invalid Input!")
                            break
                        else:
                            print(update_name + ' is not in the Contacts.')
            else:
                print('No contacts to be update.\n')

    if choice == 'f' or choice == 'F':
        while True:
            print('Set Country(' + country + ')\n\n(a) Philippines\n(b) Thailand\n(c) United States\n(e) back')
            set_country = input('--> ')
            if set_country == 'a' or set_country == 'A':
                country_num = '+63'
                country = 'Philippines'
                print('Country is set to', country + '\n')
                phil = 1
                thai = 0
                US = 0
                break
            if set_country == 'b' or set_country == 'B':
                country_num = '+66'
                country = 'Thailand'
                print('Country is set to',country + '\n')
                phil = 0
                thai = 1
                US = 0
                break
            if set_country == 'c' or set_country == 'C':
                country_num = '+1'
                country = 'United States'
                print('Country is set to', country + '\n')
                phil = 0
                thai = 0
                US = 1
                break
            if set_country == 'e' or set_country == 'E':
                break

    if choice == '0':
        print('Goodbye!')
        quit()





























































































