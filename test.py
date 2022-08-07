import models

# model_class, obj = models.storage.find('Base', '1')
# print("model: ", model_class)
# print("instance: ", obj)

# print('all before: ', models.storage.all())
# model, inst = models.storage.delete('BaseModel', '09ebbb11-027b-414d-819a-aca4500a5abe')
# print('return: ', model, inst)
# print('getting deleted after: ', models.storage.all().get('BaseModel.080c8c40-5058-419c-9fab-1678ca866c18'))
# print('getting all after: ', models.storage.all())
# print('calling storage.save')
# models.storage.save()
# print('getting deleted after save: ', models.storage.all().get('BaseModel.080c8c40-5058-419c-9fab-1678ca866c18'))
# print('getting all after save: ', models.storage.all())

# ar = [1,2,3,4,5]
# a,b,c,d = ar[:4]
# print(a,b,c,d)

import re
print("regex...")
str_pat = r"^\"[\S]+\"$"
str_pat_inner = r"[\S]+"
tes = '"hello"'
t = re.match(str_pat, tes)
if (t):
    print(tes)
    print(re.search(str_pat_inner, tes).group())
    print(t.group().removeprefix("\"").removesuffix("\""))
    print(t.group().replace("\"", ""))

# try:
#     value = int('3.2')
# except:
#     value = float('3.2')
#
# print(value)



# old backup logic

# def do_create(self, line):
#     """
#     Creates an instance from the valid model argument
#     """
#
#     if line == "":
#         print("** class name missing **")
#     else:
#         args = line.split(" ")
#         model_class = self.str_to_class(args[0])
#         if model_class is None:
#             print("** class doesn't exist **")
#         else:
#             # print("** class name found **")
#             obj = model_class()
#             models.storage.new(obj)
#             obj.save()
#             print(obj.id)

# def do_show(self, line: str):
#     """
#     Show instance of model with specified id
#     """
#     if line == "":
#         print(self.ERROR_MSGS['no_class'])
#
#     else:
#         argv = line.split()
#         argc = len(argv)
#
#         if argc == 2:
#             model_name, obj_id = argv
#             model_class, instance = models.storage.find(model_name, obj_id)
#             # print(model_class, instance)
#
#             if model_class is None:
#                 print(self.ERROR_MSGS['invalid_class'])
#             elif instance is None:
#                 print(self.ERROR_MSGS['invalid_id'])
#             else:
#                 print(str(instance))
#
#         elif argc == 1:
#             print(self.ERROR_MSGS['no_id'])
#         else:
#             print(self.ERROR_MSGS['too_many'])

# file storage delete
# all_objs = self.all()
# model_class = None
# instance = None
# key_to_pop = None  # popping during loop changes size
# for header, obj in all_objs.items():
#     model_name, obj_id = header.split(".")
#     if model_name == model:
#         # print('Model found')
#         model_class = model_name
#         if obj_id == inst_id:
#             # print('Instance found')
#             # instance = obj
#             # instance = all_objs.pop(header)
#             key_to_pop = header
#
#         else:
#             # print('Instance not found')
#             continue
#     else:
#         # print('Model not found')
#         continue
# if key_to_pop:
#     instance = all_objs.pop(key_to_pop)
# return model_class, instance

from models.base_model import BaseModel
from models.user import User

b = BaseModel()
u = User()
