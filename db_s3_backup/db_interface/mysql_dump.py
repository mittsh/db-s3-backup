import subprocess

from .dump_protocol import DumpProtocol

class MySQLDump(DumpProtocol):

    def dump(self, config, s3_bucket, s3_bucket_key_name, filepath, verbose=False, upload_callback=None):
        sqldump_cmd = ['mysqldump', config['NAME'], '-h', config['HOST'], '-P', config['PORT'], '-u', config['USER'], '-p{password}'.format(password=config['PASSWORD'])]
    	proc = subprocess.Popen(sqldump_cmd, stdout=subprocess.PIPE)

        if verbose:
    		print('Dumping MySQL database: {database} to file {filepath}'.format(database=config['NAME'], filepath=filepath))

        with open(filepath, 'w+') as f:
            while True:
        		buf = proc.stdout.read(4096*1024) # Read 4 MB
        		if buf != '':
        			f.write(buf)
        			if verbose:
        				print('- Written 4 MB')
        		else:
        			break

            if verbose:
                print('+ Dump finished')

            if upload_callback is not None:
                upload_callback(f, s3_bucket, s3_bucket_key_name, verbose)
