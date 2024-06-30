from collections import deque

def ladder_length(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    while queue:
        current_word, length = queue.popleft()
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word == end_word:
                    return length + 1
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, length + 1))
    return 0

# Example
print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Output: 5
