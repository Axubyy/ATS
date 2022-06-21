def convert_to_words(num):
    under_20 = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", ]
    tens = ["Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"]
    above_100 = {100: "Hundred", 1000: "Thousand"}

    if num < 20:
        return under_20[num]

    elif num < 100:
        val = tens[(int(num / 10) - 2)] + ("" if num % 10 == 0 else " " + under_20[num % 10])
        # if num % 10 == 0

       # print(val)
        return val

    # find the appropriate pivot - 'Hundred' in 603
    pivot_num = max([key for key in above_100.keys() if key <= num])
    print(pivot_num)

    return (
        convert_to_words((int)(num / pivot_num)) + " " + above_100[pivot_num] + (
            "" if num % pivot_num == 0 else " and " + convert_to_words(num % pivot_num))
    )


print(convert_to_words(4444))
   