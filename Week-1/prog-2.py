x = [int(x) for x in input("Enter words: ").split(",")]
oddNumber = []
evenNumber =[]
largestNumber = max(x)
for i in x:
    if i%2==0:
        evenNumber.append(i)
    else:
        oddNumber.append(i)
print("OddNumber: ", oddNumber)
print("EvenNumber: ",evenNumber)
print("LargestNumber: ",largestNumber)
    
