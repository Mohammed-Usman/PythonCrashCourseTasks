def make_album(artist_name,album_title,number_traks=''):
    dic1 = {}
    if number_traks:
        dic1[artist_name]=album_title
        dic1['Number of traks']=number_traks
    else:
        dic1[artist_name] = album_title
    return dic1
print(make_album('atif','tig zinda ha'))
print(make_album('kashif','newlife',5))
print(make_album('e','f'))


#function calling me dictionary bnaw method ke andr se dictionary hta ke
