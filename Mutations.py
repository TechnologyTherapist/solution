def mutate_string(string, position, character):

    l=list(string)
    i=position
    l[i]=character
    string=''.join(l)
    return string

if __name__ == '__main__':
    s = input("Enter a String your:")
    i, c = input("Enter a index position and character:").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)