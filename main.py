#my_list = (1,2,3,4,5,7,10)

#print(my_list[0] + my_list[6])

#list_iten=iter(my_list)

#print(list_iten)

#print(next(list_iten))
#print(next(list_iten))
#print(next(list_iten))

#next(list_iten)

#print(next(list_iten))

#class Human:
    #def __init__(self,name,age):
        #self.Name=name
        #self.Age=age

#huml=Human("Andriy",23)
#huml2=Human("Bohdan",18)
#huml3=Human("Artem",34)


#human_list=[huml,huml2,huml3]

#print(human_list)


#human_iter=iter(human_list)

#print(next(human_iter).Name)
#print(next(human_iter).Name)
#print(next(human_iter).Name)


#class employee:
#    def __init__(self,name,age):
#        self.Name=name
#        self.Age=age
#
#empl = employee("Макс",16)
#empl2 = employee("Василь",17)
#empl3 = employee("Іван",20)
#empl4 = employee("Саша",40)
#empl5 = employee("лол",19)

#empl_list=[empl,empl2,empl3,empl4,empl5]

#print(empl_list)

#empl_list=iter(empl_list)

#for elem in empl_list:
#    print(elem.Name,elem.Age)

#class Counter:
#    def __init__( self, max_Value):
#        self.value = 0
#        self.max_Value = max_Value

#    def __int__(self):
#        self.value=0
#        return self

#    def __next__(self):
#        self.value += 1
#        if self.value > self.max_Value:
#            raise StopIteration
#        return self.value


#timer = Counter(10)

#print(next(timer))
#print(next(timer))
#print(next(timer))
#print(next(timer))
#print(next(timer))
#print(next(timer))
#print(next(timer))
#print(next(timer))
#print(next(timer))
#print(next(timer))


#def reise_tu_the_degrees(nuber,max_degrees):
#    i=0
#    for  _ in range(max_degrees):
#        yield nuber**i
#        i+=1

#res = reise_tu_the_degrees (10000,3)

#for _ in res:
#    print(_)

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode = "w",
                    format="%(asctime)s: %(levelname)s - %(message)s"
                    )

logging.debug("debug")
#logging.info("info")
#logging.warning("warning")
#logging.error("error")
#logging.critical("critical")

try:
    print(16/0)
except Exception:
    logging.exception("Exception")

