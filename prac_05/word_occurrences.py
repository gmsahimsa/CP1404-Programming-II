def main():
    input_word = input("Enter a string: ").split()
    count_words(input_word)


def count_words(input_word):
    """Function to count the number of words in a given string and to print their occurence"""
    word_counts = {}
    for word in input_word:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_count = sorted(word_counts.items())
    max_length_word = max(len(word) for word in word_counts)
    for word, count in sorted_word_count:
        print(f"{word:{max_length_word}} : {count}")


main()

print ("A")
