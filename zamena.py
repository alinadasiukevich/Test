with open('my.py', 'r') as file:
    with open('changes.py', 'w') as res:
        while True:
            line = file.readline()
            if not line:
               break
            if 'cast(' in line:
                list_line = line.split(' ')
                new_list = []
                for i in list_line:
                    if 'cast(' not in i:
                        new_list.append(i)

                result = ' '.join(new_list)
                correct_result = ''
                for sym in result:
                    if sym == ')':
                        correct_result += ''
                    else:
                        correct_result += sym

                print(correct_result)
                res.write(correct_result)
            else:
                res.write(line)
