**DB S3 Backup** is a Python Command Line Tool that makes database (MySQL, SQLite) backups easy and efficient by using Amazon S3 storage.
The more recent backups are, the highest frequency they will be kept.

It currently supports databases:

- MySQL
- SQLite

But feel free to fork and add more!

## Quick Start

This is a very simple quick start guide, to make you backup easily your MySQL or SQLite database to Amazon S3, and schedule that as an hourly [crontab](https://en.wikipedia.org/wiki/Cron).

### Clone this repo into your server

```git clone https://github.com/mittsh/db-s3-backup```

### Create a JSON file to setup your backup configuration

#### MySQL Configuration
 
```json
{
	"aws":{
		"AWS_ACCESS_KEY_ID":"_MY_KEY_",
		"AWS_SECRET_ACCESS_KEY":"_MY_SECRET_KEY",
		"AWS_STORAGE_BUCKET_NAME":"my-bucket"
	},
	"database":{
		"ENGINE":"mysql",
		"NAME":"database",
		"USER":"username",
		"PASSWORD": "password",
		"HOST":"mysql-host",
		"PORT":"3306"
	}
}
```

#### SQLite Configuration

```json
{
	"aws":{
		"AWS_ACCESS_KEY_ID":"_MY_KEY_",
		"AWS_SECRET_ACCESS_KEY":"_MY_SECRET_KEY",
		"AWS_STORAGE_BUCKET_NAME":"my-bucket"
	},
	"database":{
		"ENGINE":"sqlite",
		"NAME":"MyDatabase.sqlite"
	}
}
```

### Try

It's recommended to use options ```--delete-remote``` and ```--delete-local``` so it will automatically cleanup your old backups, and prevent to fill up your disk!

```
python /path/to/db_s3_backup.py /path/to/your/db_backup_dir/ /path/to/db_backup_config.json -c --delete-remote --delete-local -v
```

Also, you can use ```--simulate-delete``` and ```-v``` to see which files are going to be deleted or kept.

```
python /path/to/db_s3_backup.py /path/to/your/db_backup_dir/ /path/to/db_backup_config.json -c --delete-remote --delete-local -v
```

### Schedule your crontab

Edit your crontab: ```crontab -e``` and add the line:

```@hourly /usr/local/bin/python /path/to/db_s3_backup.py /path/to/your/db_backup_dir/ /path/to/db_backup_config.json -c --delete-remote --delete-local -v```

Now, you're all set up and safe! Your backups are going to be saved on Amazon S3, see 'Backups frequency'.

## Options

```
positional arguments:
  backup_directory   Directory where local backups will be stored.
  config_file        Backup JSON configuration file.

optional arguments:
  -h, --help         show this help message and exit
  -c--create_dump    Creates a database dump and uploads it to Amazon S3.
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

To work it needs a JSON configuration file. The "database" dictionary is voluntary similar to Django Settings format.
For examples, see the 'Quick Start' section.

## Limitations

For now there are 2 major limitations that are going to be fixed in the very near future:

- ***No compression***: for backups, a gzip compression will reduce the size of backups very efficiently
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
