def huffman_encoding(text):
    if text == "":
        return {}, ""

    # считаем частоты
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # создаем список: [частота, символы]
    nodes = []
    for ch in freq:
        nodes.append([freq[ch], ch])

    codes = {}
    for ch in freq:
        codes[ch] = ""

    # строим коды
    while len(nodes) > 1:
        nodes.sort()
        
        left = nodes.pop(0)
        right = nodes.pop(0)

        for ch in left[1]:
            codes[ch] = "0" + codes[ch]
        
        for ch in right[1]:
            codes[ch] = "1" + codes[ch]

        nodes.append([left[0] + right[0], left[1] + right[1]])

    # кодируем строку
    encoded = ""
    for ch in text:
        encoded += codes[ch]

    return codes, encoded

text = "aaabbc"
codes, encoded = huffman_encoding(text)

print(codes)
print(encoded)