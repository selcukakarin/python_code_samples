def pisagorBul():
    for i in range(1,101):
        for j in range(i, 101):
            for k in range(j, 101):
                if(i**2+j**2==k**2):
                    print("{} {} {} üçgeni".format(i,j,k))
                if (i ** 2 + k ** 2 == j ** 2):
                    print("{} {} {} üçgeni".format(i, k, j))
                if (k ** 2 + j ** 2 == i ** 2):
                    print("{} {} {} üçgeni".format(k, j, i))

pisagorBul()
