
def li(l):
          la = [l[0]]
          for x in l:
                    i = 0
                    while i < len(la):
                              if x < la[0]:
                                        la.insert(0,x)
                                        break
                              if x > la[-1]:
                                        la.append(x)
                                        break
                              if x < la[i]:
                                        la.insert(i,x)
                                        break
                              i += 1
          print la

l = [8,3,9,5,1,4,6,2,55,54,5]
li(l)

