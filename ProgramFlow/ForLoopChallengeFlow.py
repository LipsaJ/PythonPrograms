ipAddress = input("Please enter the ip address: ")

segment = 1
segment_length = 0

for i in ipAddress:
    if i == ".":
        print("Segment {}'s length is {}".format(segment, segment_length))

        segment += 1
        segment_length = 0
    else:
        segment_length += 1

if i != '.':
    print("Segment {}'s length is {}".format(segment, segment_length))



print("Segment total count is {}".format(segment))
