books=[("Python Crash Course","Eric Matthes","2019","Programming"),("Automate the Boring Stuff","Al Sweigart","2020","Programming"),("Artificial Intelligence:A Modern Approach","Stuart Russell","2021","AI"),("Clean Code","Robert C. Martin","2008","Software Engineering")]

l=set()
for title, author, year, category in books:
    l.add(category)
sw={"AI","Cloud Computing"}
print("==========================================================")
print("LIBRARY  BOOK AND CATEGORY MANAGER ")
print("==========================================================")
while True:
    s=input("Select an operation \n 1.View Cataloged Books \n 2.Add New Book \n 3.View Unique Library Categories \n 4.Add Category To Student Wishlist \n 5.Run Category Gap Analysis \n 6.Exit :")
    if s=="1":
        print("---Current Library Catalog(Fixed Records)---")
        for title,author,year,category in books:
            print(f"{title} by {author}({year})|Genre:{category}")
        print(f"Total Books:{len(books)}") 
    if s=="2":
        print("---Add New Book Record---")
        title=input("title:")
        author=input("author:")
        year=input("year:")
        category=input("category:")
        if title and author and year and category:
            nb=(title,author,year,category)
            books.append(nb)
            l.add(category)
            print(f"{title} added as a catalog record.")
            print(f"Category set updated with:{category}")
        else:
            print("All fields are required.")
    if s=="3":
        print("---Unique Categories Available in Library---")
        for category in sorted(l):
            print(category)
        print(f"Total Unique Genre:{len(l)}")
    if s=="4":
        print("---Add to Student Wishlist---")
        ct=input("category:")
        if ct:
            sw.add(ct)
            print(f"{ct} added to Student Wishlist")
        else:
            print("Category cannot be empty.")
    if s=="5":
        print("---Category Gap Analysis---")
        print(f"Library Holdings:{sorted(l)}")
        print(f"Student Wishlist:{sorted(sw)}")
        inter=l&sw
        union=l|sw
        diff=sw-l
        print(f"Already in stock:{sorted(inter)}")
        print(f"Purchase order need:{sorted(diff)}")
        print(f"Full combined genre coverage:{sorted(union)}")
    if s=="6":
        print("Thank you for using the Library Manager.Goodbye!")
        break