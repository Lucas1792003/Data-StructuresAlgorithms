table_size = int(input())

a = list(map(int, input().split()))

hash_table = {}

 

def insert(s, v):

    # Return 0 on successful insertion

    # Return -1 if s has already been in the hash table

    if s in hash_table:

        return -1

    hash_table[s] = v

    return 0

 

def search(s):

    # Return value of the key or

    # Return -1 if s does not exist in hash table

    return hash_table.get(s, -1)

 

def delete(s):

    # Return 0 on successful deletion

    # Return -1 if s does not exist in hash table

    if s in hash_table:

        del hash_table[s]

        return 0

    return -1

 

count = 0

for i in range(table_size):

    iKey = a[i] + (i + 1) * (i + 1)

    value = search(iKey)

    if value == -1:

        insert(iKey, 1)

    else:

        delete(iKey)

        insert(iKey, value + 1)

 

for i in range(table_size):

    jKey = a[i] - (i + 1) * (i + 1)

    value = search(jKey)

    if value != -1:

        count += value

 

print(count)