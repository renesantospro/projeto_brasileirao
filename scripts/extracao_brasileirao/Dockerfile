# BASE LAYER
FROM python:alpine

# USER root

#--------##--------##--------##--------##--------##--------##--------##--------##--------##--------#
# BASE CHANGES (on ubuntu example, apt and apt-get packages)

# RUN apt update
# RUN apt upgrade -y
# RUN apt-get update
# RUN apt-get upgrade -y

# RUN apt install curl -y
# RUN apt install unzip

# ### install aws-cli
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# RUN unzip awscliv2.zip
# RUN ./aws/install

#--------##--------##--------##--------##--------##--------##--------##--------##--------##--------#
# APP REQUIREMENTS (on ubuntu example, pip packages)

### install python packages
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#--------##--------##--------##--------##--------##--------##--------##--------##--------##--------#
# SOURCE CODE

# trava container aberto
COPY extracao.py extracao.py
CMD [ "python", "./extracao.py" ]
# CMD [ "tail", "-f", "/dev/null"]

#--------##--------##--------##--------##--------##--------##--------##--------##--------##--------#
# ENTRYPOINT