import math
import os

os.system("./Convert")
# get input
def Factor(Input, V0, V1):
  D = 0
  for b in range(len(Input)):
   
    # process input
   
    if Input[b] == "0":
      D = D + math.log(V0[b])
    if Input[b] == "1":
      D = D + math.log(V1[b])
 
  return D
def Nsplit(string, length):
    return " ".join(string[i:i+length] for i in range(0,len(string),length))
# Define Variables
global G8
i=1
i1=0
i2=0
G8 = 0
 
Val_bin_1 = []
Val_bin_0 = []
Data = 0
Data_bin = ""
Input = open("Buffer", "r").read().replace(r"/n", '')
#print(len(Input))
if len(Input) > 8:
  Input = Nsplit(Input, 8).split(None)
  G8 = 1
#print(len(Input))
#print(G8)
CP1 = [23.2636, 24.6857, 25.0512] #8 bit
# get primes list
Primes = open("primes_cache").read()
Primes = Primes.replace("\n", " ")
Primes = Primes.split(None)
Primes.append(0)
 
# split into two lists
while i < 1000000:
  Val_bin_1.append(int(Primes[i+1]))
  i=i+2
i=1
while i < 1000000:
  Val_bin_0.append(int(Primes[i]))
  i=i+2

file=open("DATA", "w")
#print(Input)
Data1=""
Data2=""
Data3=""
for G in range(len(Input)):
  Data1=""
  Data2=""
  Data3=""

  Data = Factor(Input[G], Val_bin_0, Val_bin_1)

  # check invalid values
  if Data < CP1[0]:
      print("Invalid Input In Byte: "+str(G))
      #quit(0)
  elif Data > CP1[2]:
      print("Invalid Input In Byte: "+str(G))
      #quit(0)
  else:
      pass
  Data = str(Data).split(".")
  Data2 = Data[1]
  for i in range(3):
    Data1 = Data1+Data2[i]
  Data3 = Data[0]+"."+Data1
  file.write(str(Data3)+" ")
file.close()
