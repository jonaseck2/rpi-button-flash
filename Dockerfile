FROM hypriot/rpi-python

CMD ./start.py

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    make \
&& rm -rf /var/lib/apt/lists/* \
&& pip install rpi.gpio

ADD start.py /data
