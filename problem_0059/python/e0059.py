from itertools import permutations

def ascii_bitwise_xor(ascii_char, ascii_key):
  """return bitwise XOR"""
  return ascii_char ^ ascii_key

def read_cipher_file(filename):
  """return list of ascii chars from cipher file"""
  with open(filename) as f:
    return [int(ascii_char) for ascii_char in f.read().split(',')]

def decode(cipher, password):
  """decode an ascii cipher with a cyclic ascii password"""
  decoded_ascii = []
  password_index = 0
  for ascii_char in cipher:
    ascii_key = password[password_index]
    decoded_ascii.append(ascii_bitwise_xor(ascii_char, ascii_key))
    password_index += 1
    if password_index == len(password):
      password_index = 0

  decoded_text = [chr(ascii_char) for ascii_char in decoded_ascii]
  return ''.join(decoded_text), decoded_ascii

if __name__ == '__main__':
  filename = '../cipher.txt'
  cipher = read_cipher_file(filename)
  passwords = list(permutations(range(ord('a'), ord('z')), 3))
  for password in passwords:
    decoded_text, decoded_ascii = decode(cipher, password)
    #check for 5 most common English words
    if 'the' in decoded_text and 'be' in decoded_text and 'to' in decoded_text and 'of' in decoded_text and 'and' in decoded_text:
      print(decoded_text)
      print(sum(decoded_ascii))
