FROM python:3.9.5-alpine3.13
ADD curl.py /usr/local/bin/curl.py
RUN pip3 install requests
RUN chmod 777 /usr/local/bin/curl.py
CMD python3 /usr/local/bin/curl.py