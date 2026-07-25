class MaxDigitSumSmallerNumber:

    def solution(self, s):
        n = len(s)
        best = None
        maxDigit = -1

        for i in range(n):
            arr = list(s)
            if arr[i] == '0':
                continue
            arr[i] = str(int(arr[i]) - 1)
            for j in range(i+1, n):
                arr[j] = '9'
            candidate = "".join(arr)
            if candidate[0] == '0':
                candidate = candidate[1:]
            if len(candidate) < n or candidate < s:
                digitSum = 0
                for ch in candidate:
                    digitSum += int(ch)
                if digitSum > maxDigit:
                    maxDigit = digitSum
                    best = candidate
        return best

obj = MaxDigitSumSmallerNumber()
input = "980"
max_smaller_sum_number = obj.solution(input)
print(f"For {input}, the smaller string that returns the max sum is: {max_smaller_sum_number}")

