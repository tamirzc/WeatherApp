# set base image (host OS)
FROM python:latest

# set the working directory in the container
WORKDIR /app

# install dependencies
RUN pip install requests
RUN pip install PySimpleGUI


# copy the dependencies file to the working directory
COPY WeatherInfo.py .



# command to run on container start
CMD [ "python", "./WeatherInfo.py" ]