import requests, json, pickle
upload_image = "https://api.imgur.com/3/upload.json"
access_album = "https://api.imgur.com/3/album/"
access_image = 'https://api.imgur.com/3/image/'
headers = None

def unpickle(name):
    pkl_file = open(name, 'rb')
    data1 = pickle.load(pkl_file)
    pkl_file.close()
    return data1

def set_headers(client_id):
    global headers
    headers = {"Authorization": "Client-ID {}".format(client_id)}

class photo():
    #creates a photo object from PATH of object
    def __init__(self, path):
        item = (open(path, "rb"))
        data = {
            'image': item.read()
        }
        j1 = requests.post(upload_image, headers=headers, data=data)
        try:
            self.title = item.name.split('.')[0]
            self.json = j1.json()
            self.id = self.json['data']['id']
            self.delete_hash = self.json['data']['deletehash']
            self.link = self.json['data']['link']
        except Exception as e:
            print(e)
            del self
            raise SystemExit('ERROR OCCOURED')


    def delete(self):
        #deletes photo
        requests.delete(access_image + self.delete_hash, headers=headers)

    def text(self):
        return {
            'id': self.id,
            'delete_hash': self.delete_hash,
            'link': self.link
        }

    def save(self):
        with open('{}.json'.format(self.title), 'w', encoding='utf-8') as f:
            json.dump(self.text(), f, ensure_ascii=False, indent=4)


    def pickle(self):
        output = open('{}.pkl'.format(self.title), 'wb')
        pickle.dump(self, output)
        output.close()


class album():
    #creates an album object from photo objects, OR path of photos. In the case of the latter, album() would automatically create photos.
    def __init__(self, title, desc, photos):


        if not isinstance(photos[-1], photo): #check if we get a list of photo objects or photo PATHS. If the latter, we create a list of photo objects from path.
            temp = []
            for photo_path in photos:
                temp.append(photo(photo_path))
            photos = temp


        self.images = photos
        self.id = None
        self.json = None
        self.delete_hash = None
        self.link = None
        self.desc = desc
        self.title = title
        self.images_links = []
        self.create_album(desc,title)
        for image in self.images:
            self.images_links.append(image.link)

    # creates album. happens automatically when you create the object. Not very pythony
    def create_album(self, desc, title):
        delete_hash = []
        for image in self.images:
            delete_hash.append(image.delete_hash)

        j1 = requests.post(access_album, headers=headers, data={
            'deletehashes[]': delete_hash,
            'description': desc,
            'title': title,
            'privacy': 'hidden',
            'cover': delete_hash[0]})

        self.json = j1.json()
        self.id = self.json['data']['id']
        self.delete_hash = self.json['data']['deletehash']
        self.link = "https://imgur.com/a/" +self.id


    # deletes images in album, than delete the album itself
    def delete(self):
        for images in self.images:
            images.delete()

        j1 = requests.delete(access_album + self.delete_hash, headers=headers)
        print(j1.json())
        del self

    # adds photo objects to the album
    def add(self, images_to_add):
        self.images = self.images + images_to_add
        delete_hash = []
        for image in self.images:
            delete_hash.append(image.delete_hash)

        requests.put(access_album + self.delete_hash, headers=headers,data={'deletehashes[]':delete_hash})

    # removes photos in a given range. for example, [0, 1 , 2] or [5,6,7] and so on
    # possible errors: index not in list, index is bigger than list or smaller than list

    def remove(self, indexs):
        for index in indexs:
            try:
                flag =  self.images[index] in self.images
            except:
                raise SystemExit('ERROR: INDEX {} IS NOT IN ALBUM.'.format(index))

        for index in indexs:
            self.images[index].delete()

    def text(self):
        photos = []
        for i, photo in enumerate(self.images, start = 1):
            temp = {
                'photo_num': i
            }
            temp.update(photo.text())
            photos.append(temp)

        temp_dict = {
            'link': self.link,
            'id': self.id,
            'delete_hash':self.delete_hash,
            'photo_dict': photos
        }

        return temp_dict

    def save(self):
        with open('{}.json'.format(self.title), 'w', encoding='utf-8') as f:
            json.dump(self.text(), f, ensure_ascii=False, indent=4)

    def pickle(self):
        output = open('{}.pkl'.format(self.title), 'wb')
        pickle.dump(self, output)
        output.close()
