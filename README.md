# simple-imgur-library-python
The simplest imgur library for python.
using only a client-id, this library is best for simple, anonymous actions.

currently supports:
**photos**:
1. create and upload a photo
2. delete a photo
3. save a photo to either a json file or a pickle file if you wish to permanently save the object.
4. full json response from imgur
5. return a dict of a photo


**albums**:
1. create and upload a photo (via either list of existing photos or a list of paths. also supports an album from path. AT LEAST one photo per album) and assiging a title and a description.
2. delete and album and all of its photos (via deleting all the photos first and than deleting the album itself)
3. add photos to the album
4. remove photos in album
5. return a dict of an album
6. save the album to either json or a pickle.

