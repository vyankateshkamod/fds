"""
It is decided that weekly greetings are to be furnished to wish the students
having their birthdays in that week. The consolidated sorted list with desired
categorical information is to be provided to the authority. Write a python
program to store students PRNs with date and month of birth.
Let List_A and List_B be the two list for two SE Computer divisions.
Lists are sorted on date and month. Merge these two lists into third list
List_SE_Comp_DOB resulting in sorted information about Date of Birth of
SE Computer students
"""

def accept_students_information(List_SE_Comp,Str) :
   N = int(input("Enter the total no. of students of SE Computer Div %s : "%Str))
   for i in range(N) :
      print("Enter details of Student %d : "%(i+1))
      prn = input("\tPRN of the Student : ")
      dob = input("\tDate of birth (DD/MM) : ")
      temp = dob.split('/')
      A = [prn, int(temp[0]),int(temp[1])]
      List_SE_Comp.append(A)

def display_students_information(List_SE_Comp,Str) :
   N = len(List_SE_Comp)
   print("List of SE Computer Engineering students Division %s"%Str)
   for i in range(N) :
      print("\tStudent %d : %10s  %d/%d"%((i+1),List_SE_Comp[i][0],List_SE_Comp[i][1],List_SE_Comp[i][2]))
   print("\n")
   
def Sort_list_on_date_and_month(L) :
   N = len(L)
   for passes in range(1, N) :
      for i  in range(N-passes) :
         if((L[i][2] > L[i+1][2]) or ((L[i][2] == L[i+1][2]) and (L[i][1] > L[i+1][1]))) :
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp
            
def merging_two_lists(L1,L2,L3) :
   n1 = len(L1)
   n2 = len(L2)
   i = j = 0
   while (i < n1 and j < n2 ) :
      if((L1[i][2] < L2[j][2]) or ((L1[i][2] == L2[j][2]) and (L1[i][1] < L2[j][1]))) :
         L3.append(L1[i])
         i+=1
      else :
         L3.append(L2[j])
         j += 1
   while (i < n1 ) :
      L3.append(L1[i])
      i+=1
   while (j < n2 ) :
      L3.append(L2[j])
      j+=1
   
   
def main():
   while True :
      print ("\t\t1 : Accept Students Information")
      print ("\t\t2 : Display Students Information")
      print ("\t\t3 : Sort the list on date and month")
      print ("\t\t4 : Merge two lists into third")      
      print ("\t\t5 : Exit")
      ch = int(input("Enter your choice : "))
      if (ch == 5):
         print ("End of Program")
         quit()
      elif (ch == 1) :
         List_A = []
         accept_students_information(List_A,"A")
         List_B = []
         accept_students_information(List_B,"B")
      elif (ch == 2) :
         display_students_information(List_A,"A")
         display_students_information(List_B,"B")         
      elif (ch == 3) :
         Sort_list_on_date_and_month(List_A)
         Sort_list_on_date_and_month(List_B)
         display_students_information(List_A,"A")
         display_students_information(List_B,"B")
      elif (ch == 4) :
         display_students_information(List_A,"A")
         display_students_information(List_B,"B")
         List_C = []
         merging_two_lists(List_A,List_B,List_C)
         display_students_information(List_C,"Common")
      else :
         print ("Wrong choice entered !! Try again")

main()