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

def reverseList(L):
   '''This function takes a list as an input and makes it reversed'''
    if len(L) == 0:
        return

    if len(L) == 1:
        if isinstance(L[0], list):
            return [reverseList(L[0])]
        else:
            return L
    else:
        return reverseList(L[1:]) + reverseList(L[:1])

