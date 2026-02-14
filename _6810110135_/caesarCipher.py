


def caesarCipher(s, k):
    dict_ = tuple("abcdefghijklmnopqrstuvwxyz")
    encypt = ""
    for i in range(len(s)):
        if s[i] in dict_:
            encypt += dict_[(dict_.index(s[i]) + k) % 26]
        else:
            encypt += s[i]
    return encypt


if __name__ == '__main__':
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)