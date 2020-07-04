.PHONY: all test

test:
	#@cat  tox.ini | grep MOLECULE_DISTRO= | awk -F '=' '{ print $2 }'  | xargs -L1 docker pull
	@cat  tox.ini | grep MOLECULE_DISTRO= | grep  -oP '[\=]\K(.+)' | xargs -L1 docker pull
#	$(shell cat  tox.ini | grep MOLECULE_DISTRO= | awk -F = '{ print $2 }'
	#@cat  tox.ini | grep MOLECULE_DISTRO= > ./tmp
	#@cat  ./tmp | grep  -oP '[\=]\K(.+)'
	#| awk -F '=' '{ print $2 }'  | xargs -L1 docker pull
	tox
