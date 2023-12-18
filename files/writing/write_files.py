
writing = "bruh it's working isn't it?\nFor real?\nNice!"

with open('writing.txt', 'w') as file: #r for read, w for write, a to add (append to whats already written)
    file.write(writing)
