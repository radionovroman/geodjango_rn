FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

ENV GDAL_CONFIG=/usr/local/bin/gdal-config

ENV C_INCLUDE_PATH=/path/to/gdal/headers

ENV LD_LIBRARY_PATH=/usr/local/lib



RUN apt-get update && \
    apt-get install -y -y pkg-config \
    build-essential \
    python3-dev \
    python-gdal  \
    python3-gdal \
    libgdal-dev \
    libgeos-dev\
    binutils \
    libproj-dev \
    gdal-bin \
    ffmpeg\
    postgresql-client \
    postgis && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev \
    libavutil-dev libswscale-dev libswresample-devpython --verwsion libpostproc-dev \
    libsdl2-dev libsdl-dev \libgstreamer1.0-dev libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev libpangoft2-1.0-0










WORKDIR /app

RUN pip install --upgrade pip

RUN pip install numpy




COPY requirements.txt /app/requirements.txt
RUN pip install --verbose -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]