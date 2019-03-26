#!/usr/bin/env python
import text_processor as tp

if __name__ == '__main__':
    words = tp.get_paragraph_from_file(file_path='words.txt')
    words = tp.remove_special_char(text=words)
    words = tp.make_list_of_lower_word(paragraph=words)

    paragraph = tp.get_paragraph_from_file()
    paragraph = tp.remove_special_char(text=paragraph)
    paragraph = tp.make_list_of_lower_word(paragraph=paragraph)

    word_frequency = {}
    
    for w in paragraph:
        if w in words:
            if w not in word_frequency.keys():
                word_frequency[w] = 0
            word_frequency[w] += 1
    
    if len(word_frequency.keys()) > 0:
        print("Found following occurrences...")
        print("-------------------------------")
        for key, value in word_frequency.items():
            print("{k}\t\t{v}".format(k=key, v=value))
        print("-------------------------------")
    else:
        print("No matching word found.")
        
