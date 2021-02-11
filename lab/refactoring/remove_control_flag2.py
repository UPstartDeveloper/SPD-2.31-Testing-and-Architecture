# by Kami Bigdely
# Remove control flag
# Reference: https://stackoverflow.com/a/10140333/81306
# This code snippet reads up to the end of the file
n = 16
with open('foobar.file', 'rb') as fp:
    chunk = fp.read(n)
    while not (chunk == ''):  # end of file, stop running.
        print(chunk)
        # process(chunk)
        # get the next chunk
        chunk = fp.read(n)
