def word_count(txt_file):
    count_of_words = {}
    
    with open(txt_file) as the_file:
        words = the_file.read().lower().rstrip().split()

        for word in words:
            count_of_words[word] = count_of_words.get(word, 0) + 1

        for word, count in count_of_words.iteritems():
            print word, count

word_count("test.txt")