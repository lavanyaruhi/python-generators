#given string is palindrome or not using generators

def palindrome_strings(strings):
    for str in strings:
        if str == str[::-1]:
            yield str
strlist = ['level', 'hello', 'radar', 'world', 'madam']
palindrome_gen = palindrome_strings(strlist)
for pal in palindrome_gen:
    print(pal)

