import models

# model_class, obj = models.storage.find('Base', '1')
# print("model: ", model_class)
# print("instance: ", obj)

print('all before: ', models.storage.all())
model, inst = models.storage.delete('BaseModel', '09ebbb11-027b-414d-819a-aca4500a5abe')
print('return: ', model, inst)
print('getting deleted after: ', models.storage.all().get('BaseModel.080c8c40-5058-419c-9fab-1678ca866c18'))
print('getting all after: ', models.storage.all())
print('calling storage.save')
models.storage.save()
print('getting deleted after save: ', models.storage.all().get('BaseModel.080c8c40-5058-419c-9fab-1678ca866c18'))
print('getting all after save: ', models.storage.all())

