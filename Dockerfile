#
FROM python:3.9

#
WORKDIR /code

#
COPY ./reqs.txt /code/reqs.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/reqs.txt

#
COPY ./app /code/app
#
COPY ./.env /.env
COPY . .
#
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
