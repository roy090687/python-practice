class GetSecondHighest:

    def evaluate_second_highest(self, lst, lst_size):
        highest = secondHighest = float('-inf') # assign Min value
        if lst_size < 2:
            print("Invalid Input")
            return

        for i in range(lst_size):
            if lst[i] > highest:
                secondHighest = highest
                highest = lst[i]
            elif lst[i] > secondHighest and lst[i] != highest:
                secondHighest = lst[i]

        return secondHighest

obj = GetSecondHighest()
arr_list = [2, 5, 14, 10, 41, 20, 30, 41, 8, 9]
n = len(arr_list)
second_highest_value = obj.evaluate_second_highest(arr_list, n)
print(f"Second highest value from a list is: {second_highest_value}")



