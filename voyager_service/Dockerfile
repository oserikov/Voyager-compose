FROM node:20.1.0-bullseye

# RUN git clone https://github.com/oserikov/Voyager-compose
COPY . Voyager-compose
WORKDIR Voyager-compose
# RUN git submodule update --init --recursive
COPY runner.py Voyager/runner.py
WORKDIR Voyager
RUN DEBIAN_FRONTEND=noninteractive apt update
RUN apt install -y python3-dev python3-pip
RUN python3 -m pip install -e .
RUN cd voyager/env/mineflayer && npm install -g n && n 18 && npm install && cd mineflayer-collectblock && npx tsc && cd .. && npm install

CMD tail -f /dev/null
