c = 0

def szukajKombinacji(arr, index, num, reducedNum):
    global c
    if reducedNum < 0:
        return

    if reducedNum == 0:

        for i in range(index):
            file_write.write(str(arr[i]))
            file_write.write(" ")
        file_write.write('\n')
        c += 1
        return

    if index == 0:
        prev = 1
    else:
        prev = arr[index - 1]

    for k in range(prev, num + 1):
        arr[index] = k

        szukajKombinacji(arr, index + 1, num, reducedNum - k)


def algorytmSzukajacy(n):
    arr = [0] * n

    szukajKombinacji(arr, 0, n, n)


try:
    file_read = open("appIn.txt", 'r')

    file_write = open("appOut.txt", 'w+')

    for x in file_read:
        try:
            algorytmSzukajacy(int(x))
            file_write.write("=====")
            file_write.write('\n')
            file_write.write(f'Liczba kombinacji: {c}')
            file_write.write('\n')
            file_write.write('\n')
            c = 0

        except ValueError:
            print("Błąd danych wejściowych!")
            print("Błędny argument został pominięty.")
            file_write.write("XXX")
            file_write.write('\n')
            file_write.write('\n')

    file_read.close()
    file_write.close()

    print("Skrypt app.py wykonał się poprawnie.")

except IOError:
    print("Błąd otwierania pliku appIn.txt")
