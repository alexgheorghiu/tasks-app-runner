FROM amazonlinux:2

RUN yum -y install httpd
RUN yum -y install python3 
RUN yum -y install python3-pip
# RUN systemctl start httpd
# RUN systemctl enable httpd

COPY ./*.py /var/www/cgi-bin/
RUN chmod 755 /var/www/cgi-bin/*.py

COPY requirements.txt /tmp/
RUN pip3 install --requirement /tmp/requirements.txt

EXPOSE 80:80
CMD apachectl -D FOREGROUND

