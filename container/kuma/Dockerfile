FROM debian:stable

VOLUME uptime:/usr/local 

WORKDIR /usr/local/
RUN apt update && apt dist-upgrade -y && apt autoclean -y && apt autoremove -y 
RUN apt install git npm -y
RUN git clone https://github.com/louislam/uptime-kuma.git
WORKDIR /usr/local/uptime-kuma
RUN npm run setup
RUN npm install pm2 dayjs -g && pm2 install pm2-logrotate
RUN pm2 start server/server.js --name uptime-kuma && pm2 save && pm2 startup
COPY kuma-entrypoint.sh /usr/local/
RUN chmod +x /usr/local/kuma-entrypoint.sh

ENTRYPOINT [ "/usr/local/kuma-entrypoint.sh" ]