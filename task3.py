def get_file_len(filename):
    with open(filename) as f:
        file_len = len(f.readlines())
    return file_len


files = ['1.txt', '2.txt', '3.txt']
lengths = map(get_file_len, files)

with open('result.txt', 'w'):
    pass

with open('result.txt', 'a') as f:
    for file in sorted(zip(lengths, files)):
        f.write(file[1] + '\n')
        f.write(str(file[0]) + '\n')

        with open(file[1]) as readfile:
            f.write(readfile.read())
        f.write('\n')