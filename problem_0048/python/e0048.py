if __name__ == '__main__':
  last_ten = str(sum((n**n for n in range(1, 1001))))[-10:]
  print(last_ten)
