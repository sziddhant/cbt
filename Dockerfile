FROM python:3.7.0-slim-stretch
LABEL maintainer="sziddhant@gmail.com"

# Web Site Home
ENV HOME_SITE "/home/site/wwwroot"

#Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
        openssh-server \
        vim \
        curl \
        wget \
        tcptraceroute \
    && pip install --upgrade pip \
    && pip install mysql-connector \
    && pip install subprocess32 \
    && pip install gunicorn \
    && pip install virtualenv \
	&& pip install pymessenger \
    && pip install flask

WORKDIR ${HOME_SITE}

EXPOSE 8000
# setup SSH
RUN mkdir -p /home/LogFiles \
     && echo "root:Docker!" | chpasswd \
     && echo "cd /home" >> /etc/bash.bashrc

COPY sshd_config /etc/ssh/
RUN mkdir -p /opt/startup
COPY init_container.sh /opt/startup/init_container.sh

# setup default site
RUN mkdir /opt/defaultsite
COPY hostingstart.html /opt/defaultsite
COPY application.py /opt/defaultsite

# configure startup
RUN chmod -R 777 /opt/startup
COPY entrypoint.py /usr/local/bin

ENTRYPOINT ["/opt/startup/init_container.sh"]