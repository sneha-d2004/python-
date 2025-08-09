person_info =   {"name":"sneha",
                 "gender":"female",
                 "height":5.3,
                 "age":21,
                 "address":{"do.no":"6-250",
                         "streetname":"bodagunta",
                         "landmark":"c.b.c church",
                         "distic":"krishna",
                         "state":"A.P",
                         "pincode":521125
                        },
               "is_she_married":True,
               "skills":["html","python"]
}
print(person_info)
person_info["height"]=5.9
print(person_info["height"])



names =  {"name":"sneha","no":8639778548,"village":"bodagunta"}
print(type(names))
names["name"]="keerthana"
print(names["name"])
print(names)


list=["hello","welcome","something","hello","apple","apple"]
dict={}
for x in list:
    if(x in dict):
        dict[x]+=1
    else:
        dict[x]=1
print(dict) 

ex="banana"
dic={}
for x in ex:
    if (x in dict):
        dict[x]+=1
    else:
        dict[x]=1
print(dict)  




   
