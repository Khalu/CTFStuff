A common CTF or Wargame challenge is to compress a file multiple times. This script will decompress ZIP, GZ, or TAR archives. 


## Useage

To use create a directory with only the recursively compressed file and specify that directory using --directory or -D

if ./example contains a file test.tar.gz.zip

```
# ./recursiveunzip.py -D ./example
unzip test.tar.gz.zip
Archive:  test.tar.gz.zip
  inflating: test.tar.gz             
gunzipping test.tar.gz
rm: cannot remove 'test.tar.gz': No such file or directory
tar xtracting test.tar
test
Last file is test
Is this what you where looking for?
ctf{flag}

```

## Dependencies

[Filetype](https://pypi.org/project/filetype/)

If you need to use cracking on zip files like I did on one challenge checkout [zipcrack](https://github.com/Khalu/CTFStuff/tree/master/scripts/zipcrack).  
