def plecak(n, C, wartosci, wagi, memo={}):
    if n == 0 or C == 0:
        return 0

    if (n, C) in memo:
        return memo[(n, C)]

    if wagi[n - 1] > C:
        result = plecak(n - 1, C, wartosci, wagi, memo)
    else:
        result = max(
            wartosci[n - 1] + plecak(n - 1, C - wagi[n - 1], wartosci, wagi, memo),
            plecak(n - 1, C, wartosci, wagi, memo)
        )

    memo[(n, C)] = result
    return result


n = 4
C = 7
wartosci = [1, 4, 5, 7]
wagi = [1, 3, 4, 5]

wynik = plecak(n, C, wartosci, wagi)
print(f"Maksymalna wartosc w plecaku: {wynik}")
