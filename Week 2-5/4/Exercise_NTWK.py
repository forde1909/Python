scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
 
for items in scan:
 # For each item, execute this code block
 print(items)
 
# extracts the Items of the dictionary, everything
dictionaryItems = scan.items()

# extracts the keys of the dictionary, first value in the pair
dictionaryKeys = scan.keys()

# extracts the values of the dictionary second value in the pair
dictionaryValues = scan.values()

# extracts the Items of the dictionary
dictionaryItems = scan.items()

# function : Output values to the screen, Dos window
print(dictionaryKeys)
print(dictionaryValues)
print(dictionaryItems)

for ipv4, port in scan.items():
 print(f"Found a service on {ipv4} at {port}")