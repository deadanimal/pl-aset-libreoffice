import uuid
import os
import datetime
from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = "/Users/pipeline-dev/pipeline-work/aset_render" 

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        # filename_ = datetime.datetime.utcnow().strftime("%s") + uuid.uuid4().hex
        filename_ = str(datetime.datetime.utcnow().timestamp()).split('.', 1)[0] + uuid.uuid4().hex
        filename = '{}.{}'.format(filename_, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)
