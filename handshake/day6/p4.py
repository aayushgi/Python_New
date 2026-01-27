
#Write program to find union and intersection of sets.
#method1
set1=set(input("enter the elements of 1st set: ").split())
set2=set(input("enter the elements of 2nd set: ").split())
set_union=set1 | set2
set_intersection=set1&set2
print("intersection=",set_intersection)
print("union=",set_union)
#method2
setA={2,33,45,23,56}
setB={9,89,79,66,23,33}
print("union01=",setA.union(setB))
print("intersection01=",setA.intersection(setB))