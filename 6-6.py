favorite_language={
    'jen'   :   'python',
    'sarah' :   'c',
    'edward':   'ruby',
    'phil'  :   'python'
    }
names=['usman','jen','ahsan','edward','ali','taha','sarah']

#Keys Upper Case
#for k in favorite_language.keys():
#    a=k.upper()
#print('AAAAAAAA',a)

#Condition
for n in names:
   if n in favorite_language.keys():
        print(n,'ha')
   else:
       print(n, 'nahi ha')
#for n in names:
#            if n in favorite_language.keys():
#        print(n.title(),'thank you')
#    else:
#       print(n.title(),'you are invited')


