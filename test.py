import models

model_class, obj = models.storage.find('Base', '1')
print("model: ", model_class)
print("instance: ", obj)
