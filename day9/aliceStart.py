
with open('alice.txt') as f:
        for line_ in f:
            print("hello")
            print(line_.count('l'))

#hints

#The with statement handles opening and closing the file, including if an exception is raised in the inner block. The for line in f treats the file object f as an iterable, which automatically uses buffered IO and memory management so you don't have to worry about large files.

