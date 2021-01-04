
# Mike's Auto Image Rotator

This program is quite simple: It will look through your jpeg image's exif data and apply rotation automatically.

This is useful for preprocessing images before sending them through a second program that may not support orientation via exif data.

by Mike Peralta

# Requirements

* Python3
* pipenv

# Installation

Enter the repo's directory and install dependencies using pipenv, like so:

```shell script
$ cd /path/to/repo
$ pipenv install
```

# Usage

## Invocation

Invoke directly like so:

```shell script
$ cd /path/to/repo
$ pipenv run python ./main.py --help
```

Invoke in a persistent environment shell like so:

```shell script
$ cd /path/to/repo
$ pipenv shell
$ python main.py --help
```

## Arguments

Use the ***--help*** argument shown above to see all available options.

