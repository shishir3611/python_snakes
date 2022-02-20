def swap():
    file1 = input('Enter file 1\n')
    file2 = input('Enter file 2\n')
    with open(file1, 'r') as f1:
        fread1 = f1.read()
    
    with open(file2, 'r') as f2:
        fread2 = f2.read()

    with open(file1, 'w') as f1:
        f1.write(fread2)

    with open(file1, 'w') as f2:
        f2.write(fread1)
swap()