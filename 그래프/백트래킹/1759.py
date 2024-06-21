l, c = map(int, input().split(" "))

vowels = {'a', 'e', 'i', 'o', 'u'}

input_list = sorted(list(map(str, input().split(" "))))

temp_list = []

def is_valid(password):
    vowel_count = sum(1 for char in password if char in vowels)
    consonant_count = len(password) - vowel_count
    return vowel_count >= 1 and consonant_count >= 2

def solution(start):
    if len(temp_list) == l:
        if is_valid(temp_list):
            print(''.join(temp_list))
        return

    for i in range(start, c):
        temp_list.append(input_list[i])
        solution(i + 1)
        temp_list.pop()

solution(0)
