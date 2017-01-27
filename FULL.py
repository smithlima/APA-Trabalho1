import sys

def selection(list1):
    for i in range(0,len(list1)):
        menor=i
        for k in range(i,len(list1)):
            if list1[k]<list1[menor]:
                menor=k
        list1[menor],list1[i]=list1[i],list1[menor]
    return list1
#####################################################
def insertion(list1):
  for i in range( 1, len(list1)):
    key = list1[i]
    k = i
    while k > 0 and key < list1[k - 1]:
        list1[k] = list1[k - 1]
        k -= 1
    list1[k] = key
#################################################

def merge(list1):
    if len(list1)>1:
        mid = len(list1)//2
        lefthalf = list1[:mid]
        righthalf = list1[mid:]

        merge(lefthalf)
        merge(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list1[k]=lefthalf[i]
                i=i+1
            else:
                list1[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            list1[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list1[k]=righthalf[j]
            j=j+1
            k=k+1

########################################################

def quick(list1, ini, end):
	i = ini
	j = end
	pivot = list1[(ini+end)//2]
	while i<j:
		while list1[i] < pivot:
			i+=1
		while list1[j] > pivot:
			j-=1
		if i<=j:	
			aux = list1[i]
			list1[i] = list1[j]
			list1[j] = aux
			i+=1
			j-=1
	if j> ini:
		quick(list1, ini, j)
	if i<end:
		quick(list1, i, end)

######################################################


def heap(list1):
	n = len(list1)
	i = len(list1)//2
	while True:
		if i>0:
			i-=1
			t = list1[i]
		else:
			n-=1
			if n == 0:
				return
			t = list1[n]
			list1[n] = list1[0]
		parent = i
		child = i*2 +1;
		while child < n:
			if child +1 < n and list1[child + 1] > list1[child]:
				child += 1
			if(list1[child] > t):
				list1[parent] = list1[child]
				parent = child
				child = parent*2 + 1
			else:
				break
		list1[parent] = t

########################################################################
def main(argv):
	print(argv)
	
	size = int(input())
	list1 =[]
	for i in range(size):
		list1.append(int(input()))

	
	if argv[1]=="1":
		print("SELECTION SORT \n")
		selection(list1)
	elif argv[1]=="2":
		print("INSERTION SORT \n")
		insertion(list1)
	elif argv[1]=="3":
		print("MERGE SORT \n")
		merge(list1)
	elif argv[1]=="4":
		print("QUICK SORT \n")
		quick(list1,0,len(list1)-1)
	elif argv[1]=="5":
		print("HEAPSORT \n")
		heap(list1)
	else:
		return (print("Valor invalido"))
	
	for i in list1:
		print(i)

	
if __name__ == "__main__":

	main(sys.argv)

