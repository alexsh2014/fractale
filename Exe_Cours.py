# coding=Utf-8
# def ifactorielle(iF_n):
#     iF_resultat = 1
#     iF_indice = 0
#     while iF_indice != iF_n:
#         iF_indice += 1
#         iF_resultat *= iF_indice
#     return iF_resultat


def rfactorielle(rF_n, x):
    if rF_n == 0:
        x = 1
    if rF_n > 1:
        x = rfactorielle(rF_n-1, x)*x
    return x


print(rfactorielle(5, 2))
