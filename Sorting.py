
def bubble_sort(arr):
     
    i=0 
    
    while i<len(arr)-1:
        j=0
        while j<len(arr)-i-1:
            if arr[j]>arr[j+1]:
                gecici=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=gecici
            j=j+1
        i=i+1
    return arr


def selection_sort(arr):
    
    size=len(arr)
    for ind in range(size):
         min_index = ind

         for j in range(ind+1,size):
              if arr[j]<arr[min_index]:
                   min_index=j
         gecici=arr[ind]
         arr[ind]=arr[min_index]
         arr[min_index]=gecici
         
    return arr

def insertion_sort(arr):
     
     n=len(arr)
     if n<=0:
          return
     for i in range(1,n):
          key=arr[i]
          j=i-1
          while j>=0 and arr[j]>key:
               arr[j+1]=arr[j]
               j-=1
          arr[j+1]=key
     return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1
    return arr


def main():
     print("Welcome to Useful Sorting Script :)")
     choise=input("Choise :Bubble Sort 1, Selection Sort 2, Insertion Sort 3,Merge Sort 4: ")
     arrayfile=input("Array file:")
     f = open(str(arrayfile), "r")
     arr=f.read().split(";")

     print("File readed")
     for i in range(0, len(arr)):
          arr[i] = int(arr[i])
     print(arr)
     print("Array converted to int")
     if str(choise)=="1":
          conc=bubble_sort(arr)
          print("Sorted")
          print(conc)
     elif str(choise)=="2":
          conc=selection_sort(arr)
          print("Sorted")
          print(conc)
     elif str(choise)=="3":
          conc=insertion_sort(arr)
          print("Sorted")
          print(conc)
     elif str(choise)=="4":
          conc=merge_sort(arr)
          print("Sorted")
          print(conc)
     else:
          print("Not Found")
          
main()
          
