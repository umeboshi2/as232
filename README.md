# AS-232


## Setup

Use a recent version of git-annex.  Here is the version I currently use:

```
umeboshi@bard:~$ git-annex version
git-annex version: 5.20151208-1
build flags: Assistant Webapp Webapp-secure Pairing Testsuite S3 WebDAV Inotify DBus DesktopNotify XMPP DNS Feeds Quvi TDFA TorrentParser Database
key/value backends: SHA256E SHA256 SHA512E SHA512 SHA224E SHA224 SHA384E SHA384 SHA3_256E SHA3_256 SHA3_512E SHA3_512 SHA3_224E SHA3_224 SHA3_384E SHA3_384 SKEIN256E SKEIN256 SKEIN512E SKEIN512 SHA1E SHA1 MD5E MD5 WORM URL
remote types: git gcrypt S3 bup directory rsync web bittorrent webdav tahoe glacier ddar hook external
```

It may be convenient to install git-annex from sid in a chroot.  The 
[schroot](http://packages.debian.org/schoot) program is excellent for 
doing this on a stable system.


I may also be necessary to use a virtualenv, if the dependencies are not 
available in the debian repository.


