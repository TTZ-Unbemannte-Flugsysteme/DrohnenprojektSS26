#!/usr/bin/env python3

'''
Programm zum Auslesen von Telemetrie-Parametern
'''

import asyncio
from mavsdk import System

async def run():
    # Connect to the drone
    drone = System()
    #await drone.connect(system_address="udp://:14540")
    await drone.connect(system_address="serial:///dev/ttyAMA0:57600")

    # Get the list of parameters
    all_params = await drone.param.get_all_params()

    # # Iterate through all int parameters
    # for param in all_params.int_params:
    #     if param.name == 'TRIG_MODE':
    #         print(f"{param.name}: {param.value}")
        
    # Iterate through all int parameters
    for param in all_params.int_params:
        print(f"{param.name}: {param.value}")

    for param in all_params.float_params:
        print(f"{param.name}: {param.value}")

# Run the asyncio loop
asyncio.run(run())
