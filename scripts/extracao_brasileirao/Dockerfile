# from python-alpine as base image ###########################################
# Define global args
ARG FUNCTION_DIR="/home/app/"
ARG RUNTIME_VERSION="3.10"
ARG DISTRO_VERSION="3.16"

# Stage 1 - bundle base image + runtime
# Grab a fresh copy of the image and install GCC
FROM python:${RUNTIME_VERSION}-alpine${DISTRO_VERSION} AS python-alpine
# Create function directory
# RUN mkdir ${FUNCTION_DIR}
# Copy handler dependencies
COPY requirements.txt requirements.txt
# Optional – Install the function's dependencies
RUN python${RUNTIME_VERSION} -m pip install -r requirements.txt
# Copy handler function
COPY extracao_brasileirao.py extracao_brasileirao.py

# Stage 2 - build execution image and dependencies
# 
# RUN 

# Stage 3 - final runtime
# Start execution
# CMD [ "tail", "-f", "/dev/null"]
CMD ["python", "extracao_brasileirao.py"]


# # from aws_public_ecr python as base image to lambda function ####################################
# FROM public.ecr.aws/lambda/python:${RUNTIME_VERSION}

# # Copy function code
# # COPY app.py ${LAMBDA_TASK_ROOT}
# COPY extracao_brasileirao.py extracao_brasileirao.py

# # Install the function's dependencies using file requirements.txt
# # from your project folder.

# # COPY requirements.txt  .
# COPY requirements.txt requirements.txt
# # RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
# RUN python${RUNTIME_VERSION} -m pip install -r requirements.txt

# # Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
# # CMD [ "app.handler" ]
# CMD [ "extracao_brasileirao.handler" ]



# # from python-alpine as base image  to lambda function ###########################################
# # Stage 1 - bundle base image + runtime
# # Grab a fresh copy of the image and install GCC
# FROM python:${RUNTIME_VERSION}-alpine${DISTRO_VERSION} AS python-alpine
# # Install GCC (Alpine uses musl but we compile and link dependencies with GCC)
# RUN apk add --no-cache \
#     libstdc++

# # Stage 2 - build execution image and dependencies
# FROM python-alpine AS build-image
# # Install aws-lambda-cpp build dependencies
# RUN apk add --no-cache \
#     build-base \
#     libtool \
#     autoconf \
#     automake \
#     libexecinfo-dev \
#     make \
#     cmake \
#     libcurl
# # Include global args in this stage of the build
# ARG FUNCTION_DIR
# ARG RUNTIME_VERSION
# # Create function directory
# RUN mkdir -p ${FUNCTION_DIR}
# # Copy handler dependencies
# COPY requirements.txt ${FUNCTION_DIR}requirements.txt
# # Optional – Install the function's dependencies
# RUN python${RUNTIME_VERSION} -m pip install -r ${FUNCTION_DIR}requirements.txt 
# # Install Lambda Runtime Interface Client for Python
# RUN python${RUNTIME_VERSION} -m pip install awslambdaric --target ${FUNCTION_DIR}
# # Copy runtime switch
# COPY entry.sh /
# # Copy handler function
# COPY extracao_brasileirao.py ${FUNCTION_DIR}extracao_brasileirao.py

# # Stage 3 - final runtime image
# # Grab a fresh copy of the Python image
# FROM build-image
# # Include global arg in this stage of the build
# ARG FUNCTION_DIR
# # Set working directory to function root directory
# WORKDIR ${FUNCTION_DIR}
# # Copy in the built dependencies
# # COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}
# # (Optional) Add Lambda Runtime Interface Emulator and use a script in the ENTRYPOINT for simpler local runs
# ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
# # Set working runtime
# RUN chmod 755 /usr/bin/aws-lambda-rie /entry.sh
# ENTRYPOINT [ "/entry.sh" ]
# # Start execution
# CMD [ "extracao_brasileirao.handler" ]