# dapper-oz-profiles

##About
The Dapper Oz Profiles package contains the application profiles used to construct sandboxed applications with Oz. This repository contains application profiles, seccomp system call whitelists and blacklists, and scripts to "install" Oz for the included applications.

##Building
To build this package, first install an RPM development chain:

```bash
$ sudo dnf install fedora-packager fedora-review

```

Next, setup rpmbuild directories with

```bash
$ rpmdev-setuptree
```
And place the file dapper-oz-profiles.spec in the SPECS directory, and all the rest of the files to a folder called dapper-oz-profiles-1 and compress it:
```bash
$ mv dapper-oz-profiles.spec ~/rpmbuild/SPECS/
$ mkdir -p ~/rpmbuild/SOURCES/dapper-oz-profiles-1
$ mv * ~/rpmbuild/SOURCES/dapper-oz-profiles-1
$ cd ~/rpmbuild/SOURCES/
$ tar -czvf dapper-oz-profiles-1.tar.gz dapper-oz-profiles-1
```

and finally, you can build RPMs and SRPMs with:
```bash
$ cd ~/rpmbuild/SPECS
$ rpmbuild -ba dapper-oz-profiles.spec
```

##Creating Oz Profiles
Howto coming soon.



