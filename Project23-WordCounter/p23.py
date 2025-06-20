import re


def initialize():
    print("====Word Counter====")
    print("Count words, characters, and sentences in your text")
    print("Choose an option:")
    print("1. Enter text to analyze")
    print("2. Exit")

    text = ""
    while True:
        choice = int(input("Enter choice : "))
        if choice == 1:
            text_now = input("Enter or paste your text below\n")
            text = "".join(text_now)
            break
        elif choice == 2:
            break
        else:
            print("Choose a Valid option")
    return text


def count_words(sentence):
    word_count = 0
    sent = sentences(sentence)
    for se in sent:
        words = se.split(" ")
        word_count += len(words)
    return word_count


def sentences(sentence):
    sentences = re.split(r'[!,.,?]', sentence)
    return sentences


def character_spaces_count(sentence):
    count = 0
    for word in sentence:
        for character in word:
            count += 1
    return count


def character_count(sentence):
    count = 0
    for word in sentence:
        for character in word:
            if character != " ":
                count += 1
    return count


def sentences_count(sentence):
    count = 0
    sentences = re.split(r'[!,.,?]', sentence)
    for _ in sentences:
        count += 1
    return count


def avg_words_per_sentence(sentence):
    sentence_count = sentences_count(sentence)
    word_count = count_words(sentence)
    return word_count/sentence_count


def avg_character_per_word(sentence):
    word_count = count_words(sentence)
    char_count = character_count(sentence)
    return char_count/word_count


def time_to_read(sentence):
    word_count = count_words(sentence)
    avg_time_min = word_count/225
    return 60*avg_time_min


def final(sentence):
    print("====Text Analysis Result====")
    word_count = count_words(sentence)
    char_space_count = character_spaces_count(sentence)
    char_count = character_count(sentence)
    sent_count = sentences_count(sentence)
    words_per_sentence = avg_words_per_sentence(sentence)
    character_per_word = avg_character_per_word(sentence)
    time_taken = time_to_read(sentence)

    print(f"• Word count: {word_count}")
    print(f"• Character count(with spaces): {char_space_count}")
    print(f"• Character count(without spaces): {char_count}")
    print(f"• Sentences count: {sent_count-1}")
    print(f"• Word count per Sentence: {words_per_sentence}")
    print(f"• Character count per Word: {character_per_word}")
    print(f"• Time to Read: {time_taken} seconds")

    print("Thank you for using Word Counter.Goodbye!")


def main():

    sentence = initialize()
    final(sentence)


main()
