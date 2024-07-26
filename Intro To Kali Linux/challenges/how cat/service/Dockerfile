FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat

RUN useradd -m nullsecuser

COPY /shell.sh /shell.sh

RUN chmod +x /shell.sh

USER nullsecuser

WORKDIR /home/nullsecuser

EXPOSE 12100

CMD ["socat", "-T60", "TCP-LISTEN:12100,reuseaddr,fork", "EXEC:/shell.sh"]

