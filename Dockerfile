FROM public.ecr.aws/lambda/python:3.12

# Install dependencies required to run ffmpeg (e.g., for extracting packages)
RUN microdnf install -y wget
RUN microdnf install -y tar
RUN microdnf install -y xz

# Download and install ffmpeg static build (you can change the version if needed)
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz && \
    tar -xf ffmpeg-release-i686-static.tar.xz && \
    mv ffmpeg-*-static/ffmpeg /usr/local/bin/ && \
    rm -rf ffmpeg-release-i686-static.tar.xz ffmpeg-*-static/

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Set the working directory inside the container
WORKDIR /var/task

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]