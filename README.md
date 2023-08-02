Run Voyager without paying attention to dependencies, NPM etc. 

Now you only need to have Minecraft and docker+compose installed.
Just clone the repo, provide port and openai key, and do `docker-compose up` to instantiate agent (***multiple agents supported!*** )

The only difference from original MS repo is bots have distinguishable usernames. Every bot is named bot_ID where ID is its hostname based on docker container ID
tl;dr:
- provide OpenAI key and LAN port in the .env file
- `docker-compose up --scale voyager=NUMBER` is your command to run NUMBER of Voyager agents in your Minecraft world (or you can simply write `docker-compose up` to instantiate just a single vanilla Voyager agent)

Problems: 
- agents pause and unpause world independently, I'm not sure if this is OK
- agents pay no attention to each other