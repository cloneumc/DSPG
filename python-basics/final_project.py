def flatter(non_flatL):
  '''This function takes a list as an input and makes it flat '''
  flat = []
  while non_flatL: #runs until the given list is empty.
    e = non_flatL.pop(0)
    if type(e) == list: #checks the type of the poped item.
      non_flatL.extend(e) #if list extend the item to given list.
    else:
      flat.append(e) #if not list then add it to the flat list.
  return flat

def list_rev(A):
   '''This function takes a list as an input and makes it reversed'''
  neww = []
  def reverser (A_L):
    for i in A_L:
      if isinstance(i,list):
        reverser(i)
      else:
        neww.append(A_L[::-1])
        print(neww)
        return neww
  reverser(A)
  print(neww)
  return neww
## it only works with 2d if you use something like A = [[1,2[3,4,5,6]],[3,4],[5,6,7]] it does not work 
