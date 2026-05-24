scores = [85, 90, 78, 92, 88]
offset = 0
while offset < len(scores): 
    print(scores[offset])
    offset += 1

max_value = scores[0]
offset = 1
while offset < len(scores):
    if scores[offset] > max_value:
        max_value = scores[offset]
    offset += 1