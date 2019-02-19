
with open("sample.txt", "a") as sample:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{:>2} times {} is {}".format(j, i, j*i), file=sample)
        print("="*20, file=sample)
