alphabet = "abcdefghijklmnopqrstuvwxyz"

special_characters = ['.', '?', '!',' ', '\'', ',']

first_encoded_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

encoded_location = 0

decoded_location = 0

def caesar_decode(encoded_message, offset):
  decoded_message = ''
  for letter in encoded_message:
    if letter not in special_characters:
      encoded_location = alphabet.find(letter)
      decoded_location = encoded_location + offset
      if decoded_location > 25:
        decoded_location = decoded_location % 26
      decoded_message += alphabet[decoded_location]
    else:
      decoded_message += letter
  return(decoded_message)

# Task 1
# print(caesar_decode(first_encoded_message, 10))

my_first_decoded_message = "Hey man! Cool encoding, it took me a while but I figured it out! Hope all is fine. xoxo"

def caesar_encode(my_decoded_message, offset):
  my_encoded_message = ''
  for letter in my_decoded_message:
    if letter not in special_characters:
      decoded_location = alphabet.find(letter)
      encoded_location = decoded_location - offset
      if encoded_location < 0:
        encoded_location = encoded_location + 26
      my_encoded_message += alphabet[encoded_location]
    else:
      my_encoded_message += letter
  return(my_encoded_message)

# Task 2
# print(caesar_encode(my_first_decoded_message, 10))

# Task 3a
# print(caesar_decode('jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.', 10))

# Task 3b
# print(caesar_decode('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14))

# Task 4
#for i in range(0,26):
 # print(caesar_decode('vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.', i))

# Task 5
def vigenere_decode(encoded_message, keyword):
  decoded_message = ''
  keyword_phrase = ''
  offset = 0
  i =  0
  j = 0
  # Keywording
  for i in range(0, len(encoded_message)):
    if j > len(keyword) - 1:
      j = 0
    if encoded_message[i] not in special_characters:
      keyword_phrase += keyword[j]
      j += 1
    else:
      keyword_phrase += encoded_message[i]
  # Offsetting
  for i in range(0, len(encoded_message)):
    if encoded_message[i]  not in special_characters:
      offset = alphabet.find(keyword_phrase[i])
      encoded_location = alphabet.find(encoded_message[i])
      decoded_location = encoded_location + offset
      if decoded_location > 25:
        decoded_location = decoded_location % 26
      decoded_message += alphabet[decoded_location]
    else:
      decoded_message += encoded_message[i] 
  return(decoded_message)

#print(vigenere_decode('txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!', 'friends'))

def vigenere_encode(decoded_message, keyword):
  encoded_message = ''
  keyword_phrase = ''
  offset = 0
  i =  0
  j = 0
  # Keywording
  for i in range(0, len(decoded_message)):
    if j > len(keyword) - 1:
      j = 0
    if decoded_message[i] not in special_characters:
      keyword_phrase += keyword[j]
      j += 1
    else:
      keyword_phrase += decoded_message[i]
  # Offsetting
  for i in range(0, len(decoded_message)):
    if decoded_message[i] not in special_characters:
      decoded_location = alphabet.find(decoded_message[i])
      offset = alphabet.find(keyword_phrase[i])
      encoded_location = decoded_location - offset
      if encoded_location < 0:
        encoded_location = encoded_location + 26
      encoded_message += alphabet[encoded_location]
    else:
      encoded_message += decoded_message[i]
  return(encoded_message)

vigenere_encoded_message = vigenere_encode('dude, you are killing me!', 'zeplin')

print(vigenere_encoded_message)

print(vigenere_decode(vigenere_encoded_message, 'zeplin'))
