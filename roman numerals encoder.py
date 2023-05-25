## code to return roman numerals if given a whole number
## from 1 - 3999


def roman_num_gen(num):

        markers = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL',
                   50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D',
                   900:'CM', 1000:'M'}

        r_sorted_keys = reversed(sorted(markers.keys()))
        
        rn_enc = []

        for k in r_sorted_keys:
            #print(k)
            while k <= num:
                num -= k
                rn_enc.append(markers[k])
                                
        return (''.join(rn_enc))
                        

print(roman_num_gen(49))
