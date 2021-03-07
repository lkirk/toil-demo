Bootstrap: docker
From: python:3.8-slim

%post
	set -e

	# Install Deps
	apt-get update
	apt-get install -y --no-install-recommends \
		gcc \
		libc6-dev \
		locales \
		libssl-dev \
		libffi-dev

	# Fix locale
	echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
	locale-gen en_US.utf8
	/usr/sbin/update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8

	# Create ve; install packages
	cd /opt
	python -m venv ve
	ve/bin/pip install --upgrade pip setuptools
	ve/bin/pip install 'marshmallow==3.10.0' 'toil[all]==5.2.0' ipython ipdb

%runscript
	. /opt/ve/bin/activate
	"$@"
