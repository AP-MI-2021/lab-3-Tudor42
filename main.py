from copy import deepcopy

# problema 1, 20
# adaugator problema 3


def get_longest_alternating_signs(lst: list[int]) -> list[int]:
    """
    Returneaza cea mai lunga secventa din lst in care numerele
    au semne alternate
    param:
        lst - lista
    return:
        res_lst - secventa cea mai lunga
    """
    if not len(lst):
        return []
    sign = lst[0] >= 0
    # True if previous element was pozitive
    res_lst = [lst[0]]
    act_lst = [lst[0]]
    for i in range(1, len(lst)):
        act_sign = lst[i] >= 0
        # True if i-th element is pozitive
        if sign ^ act_sign:
            act_lst.append(lst[i])
        else:
            if len(act_lst) > len(res_lst):
                res_lst = act_lst[:]
            act_lst = [lst[i]]
        sign = act_sign
    if len(act_lst) > len(res_lst):
        res_lst = act_lst[:]
    return res_lst


def test_get_longest_alternating_signs():
    print("Test get_longest_alternatig_signs")
    assert get_longest_alternating_signs([1, 2, 3, -1, 2, 0]) == [3, -1, 2]
    assert get_longest_alternating_signs([]) == []
    assert get_longest_alternating_signs([0, 0, 0, 0]) == [0]
    assert get_longest_alternating_signs([-1, 0, -2, 10, -4])\
        == [-1, 0, -2, 10, -4]
    print("Everything passed")


def is_perfect_square(i: int):
    """
    Verifica daca un numar este patrat perfect
    param:
        i - numarul verificat
    return:
        True - daca numarul este patrat perfect
        False - daca numarul nu este patrat perfect
    """
    if i < 0:
        return False
    lh = 1
    rh = i
    while(lh <= rh):
        middle = (lh+rh)//2
        if middle*middle == i:
            return True
        if middle*middle < i:
            lh = middle + 1
        else:
            rh = middle - 1
    return False


def test_is_perfect_square():
    print('Test is_perfect_square')
    assert is_perfect_square(1) is True
    assert is_perfect_square(4) is True
    assert is_perfect_square(11) is False
    assert is_perfect_square(-1) is False
    assert is_perfect_square(121) is True
    assert is_perfect_square(144) is True
    print('Everything passed')


def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
    """
    Returneaza lista care contine cea mai lunga secventa de
    patrate perfecte din lst
    param:
        lst - lista initiala
    return:
        Lista care contine cea mai lunga secventa
        in care toate numerele sunt patrate perfecte
    """
    longest_list, actual_list = [], []
    for i in lst:
        if is_perfect_square(i):
            actual_list.append(i)
        else:
            if len(longest_list) < len(actual_list):
                longest_list = actual_list
            actual_list = []
    return longest_list


def test_get_longest_all_perfect_squares():
    print('Test get_longest_all_perfect_squares')
    assert get_longest_all_perfect_squares([4, 10, 3, 5]) == [4]
    assert get_longest_all_perfect_squares([5, 4, 16, 36, 10, 25]) == \
        [4, 16, 36]
    assert get_longest_all_perfect_squares([1, 10, 4, 7, 8]) == [1]
    assert get_longest_all_perfect_squares([6, 7, 8, 10, 11, 12]) == []
    print('Everything passed')


def is_prime(n):
    """
    Verifica daca un numar n este prim
    param:
        n - numarul verificat
    return:
        True  - n este prim
        False - n nu este prim
    """
    if n == 2:
        return True

    if n < 2 or not n % 2:
        return False

    for i in range(3, n//2 + 1, 2):
        if n % i == 0:
            return False
    return True


def get_longest_concat_is_prime(lst: list[int]) -> list[int]:
    """
    Returneaza cea mai lunga secventa din lst, in care
    concatenarea elementelor formeaza un numar prim
    param:
        lst - lista de numere
    return:
        res_lst - cel mai lunga subsecventa in
            care concatenarea elementelor formeaza un numar prim
    """
    inter_lst = []
    # fiecare element din inter_lst e format dintr-o lista
    # si numarul creat la concatenarea numerelor din lista
    res_lst = []
    # pastreaza rezultatul final
    for item in lst:
        for i in range(len(inter_lst)):
            inter_lst[i][0].append(item)
            inter_lst[i][1] += str(item)
            if is_prime(int(inter_lst[i][1]))\
               and len(inter_lst[i][0]) > len(res_lst):
                res_lst = deepcopy(inter_lst[i][0])
        inter_lst.append([[item, ], str(item)])
        # print(inter_lst)
    if is_prime(int(inter_lst[-1][1]))\
       and len(inter_lst[-1][0]) > len(res_lst):
        res_lst = inter_lst[-1][0]
    # print(res_lst)
    return res_lst


def test_get_longest_concat_is_prime():
    print("Test get_longest_concat_is_prime")
    assert get_longest_concat_is_prime([3, 7, 4, 5]) == [3, 7]
    assert get_longest_concat_is_prime([20, 19, 3, 4]) == [19, 3]
    assert get_longest_concat_is_prime([2222, 222, 22, 2]) == [2]
    assert get_longest_concat_is_prime([9, 1, 3, 7, 100]) == [9, 1, 3, 7]
    print("Everything passed")


def readData():
    """
    Citeste o lista de la tastatura
    param:
    return:
        o lista cu elementele citite
    """
    try:
        num = [int(i) for i in
               input('Lista de numere(numerele scrise prin spatiu): ').split()]
    except ValueError:
        print('Toate numerele trebuie sa fie integeruri')
        return []
    return num


def main():
    data = []
    test_is_perfect_square()
    test_get_longest_all_perfect_squares()
    test_get_longest_concat_is_prime()
    test_get_longest_alternating_signs()
    while True:
        print("1. Citire date.")
        print("2. Determinare cea mai lungă subsecvență cu proprietatea 1.")
        print("3. Determinare cea mai lungă subsecvență cu proprietatea 2.")
        print("4. Determinare cea mai lunga subsecventa cu proprietatea 3.")
        print("5. Ieșire.")
        option = input("Optiunea: ")
        if option == "1":
            data = readData()
        elif option == "2":
            print(get_longest_all_perfect_squares(data))
        elif option == "3":
            print(get_longest_concat_is_prime(data))
        elif option == "4":
            print(get_longest_alternating_signs(data))
        elif option == "5":
            break


if __name__ == "__main__":
    main()
