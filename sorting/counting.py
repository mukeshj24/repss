class Counting:

    def counting(self, arr):

        count = [0] * (max(arr) + 1)

        for i in range(0, len(arr)):
            count[arr[i]] += 1

        index = 0

        for j in range(0, len(count)):
            if count[j] > 0:
                arr[index] = j
                index += 1
                count[j] -= 1


arr = [4, 5, 3, 1, 2]
print(arr)

sort = Counting()
sort.counting(arr)
print(arr)
