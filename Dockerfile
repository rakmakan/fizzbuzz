# start by pulling the python image
FROM python


# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY . /app
RUN ["chmod", "+x", "./gunicorn.sh"]
ENTRYPOINT ["./gunicorn.sh"]