FROM ubuntu:latest
RUN apt update && apt install  openssh-server sudo -y
RUN mkdir /root/.ssh
COPY --chown=root:root ".ssh/authorized_keys" /root/.ssh/authorized_keys
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
