**MySQL S3 Backup** is a Python Command Line Tool that makes MySQL backups easy and efficient by using Amazon S3 storage.
The more recent backups are, the highest frequency they will be kept.

```
python mysqldump_save.py mysqldump_save_config.json -c --delete-remote --delete-local -v
```

## Options

```
positional arguments:
  config_file        Backup JSON configuration file.

optional arguments:
  -h, --help         show this help message and exit
  -c--create_dump    Creates a MySQL dump and uploads it to Amazon S3.
  --delete-remote    Delete old backups on Amazon S3.
  --delete-local     Delete old local backups.
  --simulate-delete  Simulate old backups deletion on Amazon S3 or locally.
  -v--verbose        Verbose mode.
```

## Backups frequency

- For 2 days, 1 backup is kept for every 1 hour
- For 7 days, 1 backup is kept for every 1 day
- For 30 days, 1 backup is kept for every 3 day
- For 90 days, 1 backup is kept for every 7 day
- Then, 1 backup is kept for evey month

*In the near future, this will be configurable.*

## Configuration

To work it needs a JSON configuration file. As follows:

```
{
	"aws":{
		"AWS_ACCESS_KEY_ID":"_MY_KEY_",
		"AWS_SECRET_ACCESS_KEY":"_MY_SECRET_KEY",
		"AWS_STORAGE_BUCKET_NAME":"my-bucket"
	},
	"mysql":{
		"NAME":"database",
		"USER":"username",
		"PASSWORD": "password",
		"HOST":"mysql-host",
		"PORT":"3306"
	}
}
```

The "mysql" dictionary is voluntary similar to Django Settings format.

## Limitations

For now there are 2 major limitations that are going to be fixed in the very near future:

- ***No compression***: for MySQL backups, a gzip compression will reduce the size of backups very efficiently
- ***No configuration for frequency of old backups.***
- Code is not easily accessible as a Python module. In the future, it will be accessible also as a Python class, so you can integrate it in other Python-based routines.

## License

Released under the [MIT License](http://opensource.org/licenses/MIT).

Copyright (c) 2013 [Micha Mazaheri](http://micha.mazaheri.me)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
