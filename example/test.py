from basicImgur import *

#here you need to enter the client id recieved from imgur.
set_headers('####')


# create a photo object via path of photo
d1 = photo("paint.png")
d2 = photo("paint2.png")


# creates an album from already existing photo objects.
a1 = album(title = "hey youtube", desc = "description", photos= [d1,d2])


# creates an album of one picture, from path
a2 = album(title= 'from path', desc='photos from path', photos=["paint2.png"])

print(a1.json)
# > {'data': {'id': 'qB6bQoz', 'deletehash': 'Gaj8YhEZbtmqdMW'}, 'success': True, 'status': 200}


print(a1.text())
# > {'link': 'https://imgur.com/a/qB6bQoz', 'id': 'qB6bQoz', 'delete_hash': 'Gaj8YhEZbtmqdMW', 'photo_dict': [{'photo_num': 1, 'id': 'Wx0Kbi2', 'delete_hash': 'PCCvabuOjuzMJ6m', 'link': 'https://i.imgur.com/Wx0Kbi2.png'}, {'photo_num': 2, 'id': '8t0VOmk', 'delete_hash': '2JjoJG1iGNT7uhG', 'link': 'https://i.imgur.com/8t0VOmk.png'}]}

print(d1.title)
# > paint

# save a dict of album
a1.save()

# save a dict of photo
d1.save()

# saves a pickle of photo
# NOTE: FOR SECURITY PURPOSE, THE PICKLED FILE WAS DELETED FROM THE EXAMPLE.
d2.pickle()



# NOTE: FOR SECURITY PURPOSE, THE PICKLED FILE WAS DELETED FROM THE EXAMPLE.
# unpickles a photo
d3 = unpickle('paint2.pkl')

#deletes photo via using the update hash
d3.delete()
# > picture deleted successfully



#deletes full album by deleting full photos first and than deleting the album
a1.delete()
# > 
# picture deleted successfully
# picture deleted successfully
# album deleted successfully