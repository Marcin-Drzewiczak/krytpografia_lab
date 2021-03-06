# Zaimplementuj algorytm, który oblicza wielokrotność punktu na krzywej eliptycznej.
# Dane: P= (x, y)∈E(Fp),n∈N,E= [A, B, p]
# Wynik: Q=nP∈E(Fp)


def effective_power(b, k, n):
    y = 1
    binary = list(reversed(bin(k)[2:]))
    i = len(binary) - 1
    while i >= 0:
        y = (y ** 2) % n
        if binary[i] == "1":
            y = (y * b) % n
        i = i - 1
    return y


def reverse_element(n, b):
    A = n
    B = b
    U = 0
    V = 1
    while B != 0:
        q = A // B
        temp = A
        A = B
        B = temp + (-q * B)
        temp = U
        U = V
        V = temp + (-q * V)
    if U < 0:
        return n + U
    return U


def opposed_point(x, y, p):
    return x, p-y


def sum_points(x1: int, y1: int, x2: int, y2: int, A: int, B: int, p: int):
    if (x1, y1) == opposed_point(x2, y2, p):
        return None, None
    elif x1 is None and y1 is None:
        return x2, y2
    elif x2 is None and y2 is None:
        return x1, y1
    elif x1 == x2 and y1 == y2:
        fi = ((3 * effective_power(x1, 2, p) + A) * reverse_element(p, (2*y1) % p)) % p
        x3 = (effective_power(fi, 2, p) - 2*x1) % p
        return x3, (fi * (x1 - x3) - y1) % p
    else:
        fi = ((y2 - y1) * reverse_element(p, (x2 - x1) % p)) % p
        x3 = (effective_power(fi, 2, p) - x1 - x2) % p
        return x3, (fi * (x1 - x3) - y1) % p


def multiple_point(x, y, n, a, b, p):
    N = n
    x_q = x
    y_q = y
    x_r = None
    y_r = None
    while N > 0:
        if N % 2 == 1:
            x_r, y_r = sum_points(x_r, y_r, x_q, y_q, a, b, p)
            N = N - 1
        else:
            x_q, y_q = sum_points(x_q, y_q, x_q, y_q, a, b, p)
            N = N // 2
    return x_r, y_r


# print(multiple_point(285113634279465403319996581740169338329454608669814309137990174814243655992779447106132850,
#                      598700530906084162596261101440667782569915319623798143751082061599951188013331503150304328,
#                      3,
#                      239614427021073265587611886177902927263167863041565491257781227550405368115731464059190159,
#                      447169285435982716467332439542997876345372330045685811964291613238129105735899852114277221,
#                      1183779584357076950937981497685946292711107412152534481102525547387604378262522402526266939))
print(multiple_point(285113634279465403319996581740169338329454608669814309137990174814243655992779447106132850,
                     598700530906084162596261101440667782569915319623798143751082061599951188013331503150304328,
                     550372072170590100495694029192092812338935619925879604230431301199143951074,
                     239614427021073265587611886177902927263167863041565491257781227550405368115731464059190159,
                     447169285435982716467332439542997876345372330045685811964291613238129105735899852114277221,
                     1183779584357076950937981497685946292711107412152534481102525547387604378262522402526266939))
