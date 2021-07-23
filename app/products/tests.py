# from django.test import TestCase
import uuid
# Create your tests here.
uid = uuid.uuid4()
uid = str(uid).upper().split('-')[4]
print(uid)
