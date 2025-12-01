def revStr(str):
    rev_str = ''
    for char in str:
        rev_str = char + rev_str
        #print(rev_str)
    return rev_str

str = 'Firstbit solution'
str =revStr(str)
print(str)

#Try using reverse indexing

