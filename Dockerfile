#
FROM python:3.9

#
WORKDIR /code

#
COPY ./requirments.txt /code/requirments.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirments.txt

#
COPY ./app /code/app
#
COPY ./.env /.env
COPY . .
#
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
