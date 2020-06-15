def tri_recursion(k):
  if(k > 0):
    print('here',k)
    result = k + tri_recursion(k - 1)
    print(result,'k>0')
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
