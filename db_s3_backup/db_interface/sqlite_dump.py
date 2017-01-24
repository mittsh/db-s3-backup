import subprocess

from shutil import copy2 as copyfile

from .dump_protocol import DumpProtocol

class SQLiteDump(DumpProtocol):

    def dump(self, config, s3_bucket, s3_bucket_key_name, filepath, verbose=False, upload_callback=None):
        if verbose:
    		print('Copying SQLite file to {filepath}'.format(filepath=filepath))

    	copyfile(config['NAME'], filepath)

        with open(filepath, 'r') as f:
            if upload_callback is not None:
        	    upload_callback(f, s3_bucket, s3_bucket_key_name, verbose)
