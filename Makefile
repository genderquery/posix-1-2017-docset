RESOURCES=POSIX-1-2017.docset/Contents/Resources
DOCUMENTS=${RESOURCES}/Documents

vpath docSet.dsidx ${RESOURCES}

docSet.dsidx: susv4-2018.tar.bz2
	python3 generate.py

install: docSet.dsidx
	find POSIX-1-2017.docset -type f -exec \
		install -D "{}" "${HOME}/.local/share/Zeal/Zeal/docsets/{}" \;

susv4-2018.tar.bz2:
	$(info An archive of the HTML version of the The Open Group Base Specifications)
	$(info Issue 7, 2018 Edition must first be downloaded from The Open Group)
	$(info website.)
	$(info )
	$(info Downloading of any of these files implies agreement with the terms and)
	$(info conditions for accessing the online standard file)
	$(info <http://pubs.opengroup.org/onlinepubs/terms.htm#c082>.)
	$(info )
	$(info If you do not agree, do not proceed. Please note that the downloads are)
	$(info provided "as is" with no support or warranty of fitness for purpose.)
	$(info )
	$(info Do you agree to the terms and conditions? [y/n])
	@read agree; test "$$agree" = "y" -o "$$agree" = "Y"
	mkdir -p ${DOCUMENTS}
	curl -o susv4-2018.tar.bz2 https://pubs.opengroup.org/onlinepubs/9699919799/download/susv4-2018.tar.bz2
	tar -C ${DOCUMENTS} --strip-components=1 -xf susv4-2018.tar.bz2

clean:
	-rm -f susv4-2018.tar.bz2 ${RESOURCES}/docSet.dsidx
	-rm -fr ${DOCUMENTS}/*

.PHONY: install clean
