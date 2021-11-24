import numpy as np
from xlwt import Workbook

bases = ["+", "x"]
alice_bases = []
bob_bases = []
message_bits = []
alice_degree_settings = []
bob_degree_settings = []
N = 100
# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
quantum_cryptography_1 = wb.add_sheet('quantum_cryptography_1')

# offset of number of rows in excel
offset = 0

for i in range(N):
    alice_basis = bases[np.random.randint(2)]
    bob_basis = bases[np.random.randint(2)]
    eve_basis = bases[np.random.randint(2)]
    alice_bases.append(alice_basis)
    bob_bases.append(bob_basis)
    quantum_cryptography_1.write(1 + offset, i+1, alice_basis)
    quantum_cryptography_1.write(6 + offset, i+1, bob_basis)
    quantum_cryptography_1.write(4 + offset, i+1, eve_basis)


    # 4 options for alice's wave plate depending on basis and bit
    next_bit = np.random.randint(2)
    quantum_cryptography_1.write(3 + offset, i+1, next_bit)

    if alice_basis == "+":
        if next_bit == 1:
            alice_degree = 0
        else:
            alice_degree = 90


    # alice basis = "x"
    else:
        if next_bit == 0:
            alice_degree = -45
        else:
            alice_degree = 45

    if bob_basis == "+":
        bob_degree = 0
    else:
        bob_degree = 45

    if eve_basis == "+":
        eve_degree = 0
    else:
        eve_degree = 45

    quantum_cryptography_1.write(2 + offset, i+1, alice_degree)
    quantum_cryptography_1.write(5 + offset, i+1, eve_degree)
    quantum_cryptography_1.write(7 + offset, i+1, bob_degree)

quantum_cryptography_1.write(1 + offset, 0, 'alice_bases')
quantum_cryptography_1.write(2 + offset, 0, 'alice_degree_settings')
quantum_cryptography_1.write(3 + offset, 0, 'message_bits')
quantum_cryptography_1.write(4 + offset, 0, 'eve_basis')
quantum_cryptography_1.write(5 + offset, 0, 'eve_degree')
quantum_cryptography_1.write(6 + offset, 0, 'bob_bases')
quantum_cryptography_1.write(7 + offset, 0, 'bob_degree_settings')

print(sum(alice_bases[i]==bob_bases[i]for i in range(len(alice_bases)))/len(alice_bases))
wb.save('quantum_cryptography.xls')




