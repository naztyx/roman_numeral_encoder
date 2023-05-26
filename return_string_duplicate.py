from collections import Counter as cntr

def duplicate_count(text):
    frequencies = cntr(text.lower())
    cnt = 0
    for k,v in frequencies.items():
        if v > 1:
            cnt+=1
    return cnt

print(duplicate_count('iNcreDIbles'))
