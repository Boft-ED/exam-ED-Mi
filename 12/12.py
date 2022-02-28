a = 98 * '9'
while '4444' in a or '999' in a:
    if '4444' in a:
        a = a.replace('4444', '9',1)
    else:
        a = a.replace('999', '4', 1)
print(a)