from django.db import models




def upload_des(instance, filename):
    return 'ImageProduct/{filename}'.format(filename=filename)
