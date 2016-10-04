def word_count(txt_file):
    #dictionary to store each word and their count
    count_of_words = {}
    #open text file and close after done
    with open(txt_file) as word_file:
        #read word_file as string, then lower case all letters, then strip
        #white space, then split into a list of words(no argument in split
        #strips all whitespace)
        words = word_file.read().lower().rstrip().split()

        #iterate through the words in the list
        for word in words:
            #increment by 1 if word appears
            count_of_words[word] = count_of_words.get(word, 0) + 1

        #unpack items from the list of tuples and print
        for word, count in count_of_words.iteritems():
            print word, count

word_count("test.txt")
