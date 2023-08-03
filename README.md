Run Voyager without paying attention to dependencies, NPM etc. 

It runs Minecraft server and voyager (or many voyagers) so that you don't need to manage dependencies, fabric etc.

Just clone the repo, provide your openai key, and do `docker-compose up` to instantiate agent (***multiple agents supported!*** )
You will first see logs of the minecraft server starting (open to LAN via port 25565 by default), then voyager service will start.

The only difference from original MS-Voyager repo is bots have distinguishable usernames. Every bot is named bot_ID where ID is its hostname based on docker container ID
tl;dr:
- provide OpenAI key in the `openai.env` file
- `docker-compose up --scale voyager=NUMBER` is your command to run NUMBER of Voyager agents in your Minecraft world (or you can simply write `docker-compose up` to instantiate just a single vanilla Voyager agent)

Problems: 
- agents pause and unpause world independently, I'm not sure if this is OK
- agents pay no attention to each other
- I haven't tested if I can connect to the server from my Minecraft client. Yet shouldn't be a problem