# code to return hash tag from a given string

def hashtag_enc(s):

    hashtag_enc = []
    words = s.split()

    if len(s) < 1:
        return False
    else:        
        for i in words:
            print(i)
            
            i = i.strip()
            i= i.capitalize()
            
            hashtag_enc.append(i)

        s_enc = ''.join(hashtag_enc)

        if len(s_enc) < 140:
            return '#' + s_enc
        else:
            return(False)

print(hashtag_enc('c i n'))
