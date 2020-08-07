# POSIX.1-2017 Docset Generator for Dash/Zeal

## Automated build
```shell
make
```
Will download the HTML archive from the Open Group website, extract it, and run
the generator.

Additionally you can install the Docset for Zeal on Linux:
```shell
make install
```
Will install the Docset to `${HOME}/.local/share/Zeal/Zeal/docsets/`.

## Manual build
- Download an archive in the format of your choice from
  http://pubs.opengroup.org/onlinepubs/9699919799/download/
- Extract the archive into `POSIX-1-2017.docset/Contents/Resources/Documents`
  such that `index.html` is in `Documents`, not `susv4-2018`
- Run `python generate.py`
- Install `POSIX-1-2017.docset` as appropriate

## TODO
- ~~Add an icon~~
- Get/make better icon?
- Add table of contents (requires rewrite)
- ~~Package for https://github.com/Kapeli/Dash-User-Contributions~~
- Submit the package to Dash User Contributions
- Replace Makefile for portability
