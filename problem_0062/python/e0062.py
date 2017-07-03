if __name__ == '__main__':
  cubes = [n**3 for n in range(1, 10000)]
  permutations_count = {}
  for cube in cubes:
    cube_str = str(cube)
    sorted_cube_str = ''.join(sorted(cube_str))
    if sorted_cube_str in permutations_count:
      permutations_count[sorted_cube_str]['count'] = permutations_count[sorted_cube_str]['count'] + 1
    else:
      permutations_count[sorted_cube_str] = {'count': 1, 'lowest': cube_str}

  print([(perm['count'], perm['lowest']) for perm in permutations_count.values() if perm['count'] > 4])
