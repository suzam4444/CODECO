import random
import string
st=str(input("enter message"))
words=st.split()
print(words)

codin=False
if(codin):
  newword=[]
  for word in words:
    if(len(words)>=3):
      chars=string.ascii_letters
      r1="".join(random.choice(chars) for _ in range(3))
      r2="".join(random.choice(chars) for _ in range(3))
      stnew=r1+word[1:]+word[0]+r2
      newword.append(stnew)

    else:
      newword.append(word[::-1])
  
  print(" ".join(newword))

else:
  newword=[]
  for word in words:
    if(len(words)>=3):
      stnew=word[3:-3]
      stnew=stnew[-1]+stnew[:-1]
      newword.append(stnew)

    else:
      newword.append(word[::-1])

  print(" ".join(newword))

