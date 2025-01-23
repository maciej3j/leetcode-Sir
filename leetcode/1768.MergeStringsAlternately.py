def mergeAlternately(word1: str, word2: str) -> str:
    new_string = ''
    word1_len = len(word1)
    word2_len = len(word2)
    if word1_len == word2_len:
        for i in range(word1_len):
            new_string += word1[i]
            new_string += word2[i]
        return new_string
    else:
        if word1_len < word2_len:
            for i in range(word1_len):
                new_string += word1[i]
                new_string += word2[i]
            else:
                new_string += word2[word1_len:]
        else:
            for i in range(word2_len):
                new_string += word1[i]
                new_string += word2[i]
            else:
                new_string += word1[word2_len:]
        return new_string


result1 = mergeAlternately("abc", "pqr")
assert result1 == "apbqcr", f"Should be apbqcr, it is {result1}"

result2 = mergeAlternately("ab", word2 = "pqrs")
assert result2 == "apbqrs", f"Should be apbqrs, it is {result2}"

result3 = mergeAlternately(word1 = "abcd", word2 = "pq")
assert result3 == "apbqcd", f"Should be apbqcd, it is {result3}"

print("Well done.")