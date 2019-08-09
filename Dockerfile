FROM python:3.7-slim

RUN mkdir -p /code

WORKDIR /code
ADD . /code

RUN pip install --no-cache --upgrade pip && \
	# Hack to stop pyhcl install from complaining
	pip uninstall ply; pip uninstall pyhcl; pip install ply; pip install pyhcl && \
	pip install --no-cache -r requirements.txt

WORKDIR /data

ENTRYPOINT [ "/code/generate.py" ]
