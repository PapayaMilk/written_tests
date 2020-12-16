def pseudo_encrypt(value):
    l1 = (value >> 16) & 65535
    r1 = value & 65535
    i = 0
    while i < 3:
        l2 = r1
        r2 = l1 ^ int((((1366 * r1 + 150889) % 714025) / 714025) * 32767)
        l1 = l2
        r1 = r2
        i += 1
    return (r1 << 16) + l1


if __name__ == "__main__":
    # value = 1
    # print(pseudo_encrypt(value))
    for i in range(10):
        print(pseudo_encrypt(i))
