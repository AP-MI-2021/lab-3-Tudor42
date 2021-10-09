from copy import deepcopy

# problema 1, 20


def is_perfect_square(i: int):
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
    assert is_perfect_square(121) is True
    assert is_perfect_square(144) is True
    print('Everything passed')


def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
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
    input:
        n - numarul verificat
    output:
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
    input:
        lst - lista de numere
    output:
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
    while True:
        print("1. Citire date.")
        print("2. Determinare cea mai lungă subsecvență cu proprietatea 1.")
        print("3. Determinare cea mai lungă subsecvență cu proprietatea 2.")
        print("4. Ieșire.")
        option = input("Optiunea: ")
        if option == "1":
            data = readData()
        elif option == "2":
            print(get_longest_all_perfect_squares(data))
        elif option == "3":
            print(get_longest_concat_is_prime(data))
        elif option == "4":
            break


if __name__ == "__main__":
    main()
