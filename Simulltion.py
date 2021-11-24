import numpy as np
from xlwt import Workbook

bases = ["+", "x"]
alice_bases = []
eve_bases = []
bob_bases = []

N = 100
# Workbook is created
# wb = Workbook()

# add_sheet is used to create sheet.
# quantum_cryptography_1 = wb.add_sheet('quantum_cryptography_1')
#
# quantum_cryptography_1.write(1, 0, 'alice_bases')
# quantum_cryptography_1.write(2, 0, 'message_bits')
# quantum_cryptography_1.write(3, 0, 'eve_bases')
# quantum_cryptography_1.write(4, 0, 'eve_bits')
# quantum_cryptography_1.write(5, 0, 'bob_bases')
# quantum_cryptography_1.write(6, 0, 'bob_bits')

eve_caused_mistake_percentage = 0

for i in range(N):
    alice_basis = bases[np.random.randint(2)]
    eve_basis = bases[np.random.randint(2)]
    bob_basis = bases[np.random.randint(2)]
    alice_bases.append(alice_basis)
    eve_bases.append(eve_basis)
    bob_bases.append(bob_basis)
    # quantum_cryptography_1.write(1, i + 1, alice_basis)
    # quantum_cryptography_1.write(5, i + 1, bob_basis)

    # 4 options for alice's wave plate depending on basis and bit
    alice_bit = np.random.randint(2)
    # quantum_cryptography_1.write(2, i + 1, alice_bit)

    if alice_basis == eve_basis:
        eve_bit = alice_bit
    else:
        eve_bit = np.random.randint(2)
    if eve_basis == bob_basis:
        bob_bit = eve_bit
    else:
        bob_bit = np.random.randint(2)

    if bob_basis == alice_basis and bob_bit != alice_bit:
        eve_caused_mistake_percentage += 1

    # quantum_cryptography_1.write(6, i + 1, bob_bit)

# sanity check
same_base_num = sum(alice_bases[i] == bob_bases[i] for i in range(len(alice_bases)))
print("percentage of time alice and bob had the same basis is : ", 100 * same_base_num / len(alice_bases), "%")

eve_caused_mistake_percentage = eve_caused_mistake_percentage * 100 / same_base_num

print("the percentage of time bits were misplaced because of eve is : ", eve_caused_mistake_percentage, "%")

# wb.save('quantum_cryptography.xls')
