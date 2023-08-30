import os
import socket
from voyager import Voyager

openai_api_key = os.getenv("MINECRAFT_OPENAI_KEY", 'your openai key')
mc_port = os.getenv("MINECRAFT_LAN_PORT", 40000)
mc_host = os.getenv("MINECRAFT_LAN_HOST", "minecraft")
machine_name = socket.gethostname()
voyager = Voyager(
    mc_port=mc_port,
    mc_host=mc_host,
    env_wait_ticks=100,
    openai_api_key=openai_api_key,
    bot_name=f"bot_{machine_name}"
)

# start lifelong learning
voyager.learn()
