def max_3digit_after_k_increment(number, k):
    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10

    # increment for hundreds
    inc = min(k, 9 - hundreds)
    hundreds += inc
    k -= inc

    # increment for tens
    inc = min(k, 9 - tens)
    tens += inc
    k -= inc

    # increment for ones
    inc = min(k, 9 - ones)
    ones += inc

    return hundreds * 100 + tens * 10 + ones * 1

print("Max 3 digit number after k increment", max_3digit_after_k_increment(512, 10))
