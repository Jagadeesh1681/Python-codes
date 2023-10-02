n=input("Enter a aplhabetical string : ")
vowels=['a','e','i','o','u']
remove=[ch for ch in n if ch.lower() not in vowels]
remove=''.join(remove)
print(remove)
