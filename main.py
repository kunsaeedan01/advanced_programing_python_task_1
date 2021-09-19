def permutations(user_input, ind, end):
    if ind == end:
        print("".join(user_input))
    else:
        for i in range(ind, end + 1):
            user_input[ind], user_input[i] = user_input[i], user_input[ind]
            permutations(user_input, ind + 1, end)
            user_input[ind], user_input[i] = user_input[i], user_input[ind]  # backtrack


characters = input("Please, write the characters for permutations without space: ")
input_len = len(characters)
list_conv = list(characters)
permutations(list_conv, 0, input_len - 1)
