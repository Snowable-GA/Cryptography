def GenerateStream(K):
    for i in range(0, len(K)):
        K.append(K[i]);
    return K;

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1];
    return list;


def InitialPermutation(S, T):
    j = 0;
    for i in range(0, len(S)):
        j = (j + S[i] + T[i])%8;
        swap(S, i, j);
    return S;

def XOR(S, P):
    i = 0;
    j = 0;
    index = 0;
    C = [];
    while(index < len(P)):
        i = (i + 1)%8;
        j = (j + S[i])%8;
        swap(S, i, j);
        t = (S[i] + S[j])%8;
        k = S[t];
        C.append(k ^ P[index]);
        index = index + 1;
    return C;


#RC4 encrypt:
S = [0, 1, 2, 3, 4, 5, 6, 7]
K = [1, 2, 3, 6]
P = [1, 2, 2, 2]

T = GenerateStream(K);

print(InitialPermutation(S, T));

print(XOR(S, P));










