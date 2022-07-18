from hashlib import new


def books(library,book_name):
    # library= [["Harry Potter and the Philosophers Stone","Harry Potter and the Chamber of Secrets", "The Adventures of Sherlock Holmes","The Adventures of Sherlock Holmes"]]
    new_list=[]
    for b in range(len(library)):
        
        if book_name in library[b]:
            new_list.append(library[b])
    return new_list
           
    
print(books(["Harry Potter and the Philosophers Stone","Harry Potter and the Chamber of Secrets", "The Adventures of Sherlock Holmes","The Adventures of Sherlock Holmes"],"Harry Potter"))


   



