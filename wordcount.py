# put your code here.
def word_count(filename):
    new_file = open(filename)
    word_dictionary = {}
    for line in new_file:
        line = line.rstrip()
        words = line.split(" ")
        for word in words:
            word_dictionary[word] = word_dictionary.get(word, 0) + 1
    
    for key, value in word_dictionary.iteritems():
        print key, value      

word_count('test.txt')