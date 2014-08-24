'''
Created on Aug 23, 2014

@author: pawel
'''
############ 1 #############
def suma_kwadratow(x):
    wynik = 0
    for x in range(1, x+1):
        wynik += x*x

    return wynik

def kwadrat_sumy(x):
    wynik = sum([x for x in range(1, x+1)])

    return wynik*wynik

print "Roznica wynosi: ", kwadrat_sumy(100) - suma_kwadratow(100)

############ 2 #############

#i = 0
numbers_dict = {}
for n in xrange(1, 100):
    numbers_dict.update({
                         n-1: n,
                    })
#    i += 1

print numbers_dict

# even_numbers = []
# for k, v in numbers_dict.items():
#     if v % 2 == 0:
#         even_numbers.append(v)
#     else:
#         pass
even_numbers = [v for k, v in numbers_dict.items() if v % 2 == 0]

print "Ilosc liczb parzystych: " + str(even_numbers.__len__())

try:
    size = even_numbers.size
except Exception:
    size = None
    
print "Size = " + str(size)


############ 3 #############

string = "g65 fmnc wms3443 bgb4lr 6rp5ylq7jyr5c8 5g78r z6w f05ylb."

print ''.join([chr(ord(ch) + 2) for ch in string if not ch.isdigit()])

print "Powyzszy kod dla wszystkich niecyfr w napisie string zwieksza wartosc liczbowa znaku o 2 i zamienia go z powrotem na znak"





if __name__ == '__main__':
    pass