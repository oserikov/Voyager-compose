Run Voyager without paying attention to dependencies, NPM etc. 

*** multiple agents supported!***


It runs Minecraft server and voyager (or many voyagers) so that you don't need to manage dependencies, fabric etc.
You will first see logs of the minecraft server starting (open to LAN via port 25565 by default), then voyager service will start.
The only difference from original MS-Voyager repo is bots have distinguishable usernames. Every bot is named bot_ID where ID is its hostname based on docker container ID

**tl;dr:**
1. `git clone --recurse-submodules https://github.com/oserikov/Voyager-compose`
2. provide OpenAI key in the `openai.env` file
3. `docker-compose up` will run Voyager agent and Minecraft server (or `docker-compose up --scale voyager=NUMBER` to run NUMBER of Voyager agents in your Minecraft world)

Problems: 
- agents pause and unpause world independently, I'm not sure if this is OK
- agents pay no attention to each other
- I haven't tested if I can connect to the server from my Minecraft client. Yet shouldn't be a problem
