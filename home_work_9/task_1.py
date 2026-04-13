def popular_words(text, words):
    result = {}
    text = text.lower().split()
    for word in words:
        count = text.count(word)
        result[word] = count
    return result
print(popular_words('''My name is John ''', ['my', 'name', 'is', 'John']))


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')