def countSort(arr):
    n = len(arr)

    freq = [0] * 100

    for i in range(n):
        num = int(arr[i][0])
        freq[num] += 1

    cu = [0] * 100
    cu[0] = freq[0]

    for i in range(1, 100):
        cu[i] = cu[i - 1] + freq[i]

    print(' '.join(map(str, cu)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)