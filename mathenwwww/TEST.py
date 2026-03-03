# lexiko test dictionary
lexiko = {
    "apple": "a fruit that is typically round and red or green",
    "banana": "a long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe",
    "cat": "a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws",
    "dog": "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell"
}

for word, definition in lexiko.items():
    print(f"{word}: {definition}")
    
#print apple 
print(lexiko["apple"])