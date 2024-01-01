def count_words(words):
    count = 0
    for word in words:
        if word == "Dan":
            print(word, "is being counted")
            count += 1
    return count


words = ["Dan", "danger", "Leo"]
print(count_words(words))
