def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as cast:
        for c in cast:
            cast_list.append(c.split(",")[0])

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
i=0
for actor in cast_list:
    i+=1
    print(i,actor)