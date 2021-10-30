def inter(a):
  size=len(a)
  temp=a[0]
  a[0]=a[size-1]
  a[size-1]=temp
  return a
a=[1,2,3,4]
print(inter(a))
