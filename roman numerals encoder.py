## code to return roman numerals if given a whole number
## from 1 - 3999


def roman_num_gen(num):

        markers = {1:'I', 5:'V', 10:'X',
                   50:'L', 100:'C', 500:'D', 1000:'M'}
        
        j=num
        n=0
        k=len(str(j))
        num_split=[]
        rn_enc = []
        _min = ['', 4, 9, 40, 90, 400, 900]
        ind = list(markers.keys())
        #ind.pop(0)
        
        for i in str(j):
                n=n+1
                if n == k:
                        num_split.append(i)
                else:
                        zc = k-n
                        z = '0'*zc
                        d = i+z
                        num_split.append(d)
        #print(num_split)

        for i in num_split:
                # print (i)
                k = list(i)

                # encode numbers between 1000 to 4999
                if int(i) >= 1000:
                        enc = markers[1000] * int(k[0])
                        rn_enc.append(enc)

                # encode 600, 700, 800
                elif int(i) >= 500 and int(i) < 900:
                        x = int(k[0]) - 5
                        enc = markers[100] * x
                        enc = markers[500] + enc
                        rn_enc.append(enc)

                # encode 100, 200, 300
                elif int(i) >= 100 and int(i) < 400:
                        enc = markers[100] * int(k[0])
                        rn_enc.append(enc)

                # encode 50, 60, 70, 80
                elif int(i) >= 50 and int(i) < 90:
                        x = int(k[0]) - 5
                        enc = markers[10] * x
                        enc = markers[50] + enc
                        rn_enc.append(enc)

                # encode 10, 20, 30, 
                elif int(i) >= 10 and int(i) < 40:
                        enc = markers[10] * int(k[0])
                        rn_enc.append(enc)
                
                # encode 5 to 8
                elif int(i) >= 5 and int(i) < 9:
                        x = int(k[0]) - 5
                        enc = markers[1] * x
                        enc = markers[5] + enc
                        rn_enc.append(enc)
                        
                # encode 4,9,40,90,400,900
                elif int(i) in _min:
                        #print(i)
                        _ind = _min.index(int(i))
                        
                        if '9' in i:
                                pre = markers[ind[_ind - 2]]
                                pos = markers[ind[_ind]]
                                enc = pre+pos
                                rn_enc.append(enc)
                        else:
                                pre = markers[ind[_ind - 1]]
                                pos = markers[ind[_ind]]
                                enc = pre+pos
                                rn_enc.append(enc)                        
                                
                else:
                        # encode 1 to 3
                        enc = markers[1] * int(k[0])
                        rn_enc.append(enc)
                        
        return (''.join(rn_enc))
                        

print(roman_num_gen(1000))
