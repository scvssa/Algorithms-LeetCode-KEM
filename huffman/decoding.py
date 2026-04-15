def huffman_decoding(encoded, codes):
   
    reverse_codes = {}
    for ch in codes:
        reverse_codes[codes[ch]] = ch

    decoded = ""
    current = ""

    for bit in encoded:
        current += bit

        if current in reverse_codes:
            decoded += reverse_codes[current]
            current = ""

    return decoded


codes = {
    'a': '0',
    'b': '10',
    'c': '11'
}

encoded = "0001011"

decoded = huffman_decoding(encoded, codes)

print("Коды:", codes)
print("Закодировано:", encoded)
print("Декодировано:", decoded)