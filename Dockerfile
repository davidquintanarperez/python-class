# set base image (host OS)
FROM python

# set the working directory in the container
WORKDIR /home

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy secciones
COPY ["secciones/*", "."]

# install jupyterlab
RUN pip install jupyterlab

# command to run on container start
CMD ["jupyter-lab", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
