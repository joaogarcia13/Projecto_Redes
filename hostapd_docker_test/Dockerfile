FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade
RUN apt-get install net-tools
RUN apt-get -y install python3
RUN apt-get -y install pip
RUN pip install Flask
RUN apt-get -y install hostapd
EXPOSE 5000
COPY firewall ./firewall
COPY networkManager ./networkManager
COPY pi_REST ./pi_REST
COPY qos ./qos
COPY app.py .
COPY updatePi.sh .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

