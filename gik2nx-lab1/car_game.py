# GIK2NX Distributed computing - Lab 1: FSM game
# Group members:
#   - Ali Hasan
#   - Bilal Ahmed Adem
#   - Karim Al Hashoom
#
# The game: a car agent has to drive 100 km home. The tank only has 15 litres,
# which is not really enough, so the driver needs some luck finding a gas station.
# On the way the car can also get a flat tire, and if the spare tire is broken
# too the car is stuck. Everything is random, so every run is a new trip.
#
# How to run:
#   1. Start the SPADE XMPP server in one terminal:   spade run
#   2. Run the game in another terminal:              python car_game.py

import asyncio
import random

import spade
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State

# State names. We keep them as constants so a typo in a transition
# gives an error right away instead of silently doing nothing.
START = "START"
DRIVE = "DRIVE"
GAS_STATION = "GAS_STATION"
FLAT_TIRE = "FLAT_TIRE"
ARRIVED = "ARRIVED"          # end state - the driver wins
BROKEN_DOWN = "BROKEN_DOWN"  # end state - the driver loses

GOAL_KM = 100


class TripFSM(FSMBehaviour):
    async def on_start(self):
        print("=== The trip begins ===")

    async def on_end(self):
        # The FSM is done (we ended in ARRIVED or BROKEN_DOWN), so we stop the
        # agent too. Otherwise main() would wait forever.
        print("=== Game over ===")
        await self.agent.stop()


class StartState(State):
    async def run(self):
        # The game values live on the agent, not in the states. Every state is its
        # own object, so the agent is the easiest place they can all reach.
        self.agent.km = 0
        self.agent.fuel = 15
        self.agent.reason = ""
        print(f"You need to drive {GOAL_KM} km home and you have {self.agent.fuel} litres of fuel.")
        self.set_next_state(DRIVE)


class DriveState(State):
    async def run(self):
        a = self.agent
        await asyncio.sleep(0.5)  # small pause so the game is readable when it runs

        # Each drive is one stretch of road. Both distance and fuel use are random,
        # so sometimes you drive far on little fuel and sometimes the opposite.
        driven = random.randint(10, 20)
        used = random.randint(2, 5)
        a.km += driven
        a.fuel = max(a.fuel - used, 0)  # the tank can't go below empty
        print(f"Drove {driven} km (used {used} l) -> {a.km} km done, {a.fuel} l left")

        # Order matters: if you reach home on the last drop of fuel, you still win.
        if a.km >= GOAL_KM:
            self.set_next_state(ARRIVED)
        elif a.fuel <= 0:
            a.reason = "The tank is empty"
            self.set_next_state(BROKEN_DOWN)
        elif random.random() < 0.1:
            self.set_next_state(FLAT_TIRE)
        elif a.fuel < 8 and random.random() < 0.5:
            # Low on fuel, but you only find a gas station half of the time.
            self.set_next_state(GAS_STATION)
        else:
            self.set_next_state(DRIVE)


class GasStationState(State):
    async def run(self):
        a = self.agent
        await asyncio.sleep(0.5)
        # You only have a little money with you, so you can't always fill the tank.
        bought = random.randint(5, 15)
        a.fuel += bought
        print(f"Found a gas station! Bought {bought} l, now {a.fuel} l in the tank.")
        self.set_next_state(DRIVE)


class FlatTireState(State):
    async def run(self):
        a = self.agent
        await asyncio.sleep(0.5)
        print("BANG! Flat tire. You get out and check the spare tire...")
        # 70% chance the spare is fine. If not, the trip is over.
        if random.random() < 0.7:
            print("The spare tire is fine, you change it and drive on.")
            self.set_next_state(DRIVE)
        else:
            a.reason = "The spare tire was flat too"
            self.set_next_state(BROKEN_DOWN)


class ArrivedState(State):
    async def run(self):
        # No set_next_state here, that is what makes it a final state.
        print(f"You made it home with {self.agent.fuel} l left. You win!")


class BrokenDownState(State):
    async def run(self):
        a = self.agent
        print(f"{a.reason}. You are stuck after {a.km} km and have to call for help. You lose!")


class CarAgent(Agent):
    async def setup(self):
        fsm = TripFSM()
        fsm.add_state(name=START, state=StartState(), initial=True)
        fsm.add_state(name=DRIVE, state=DriveState())
        fsm.add_state(name=GAS_STATION, state=GasStationState())
        fsm.add_state(name=FLAT_TIRE, state=FlatTireState())
        fsm.add_state(name=ARRIVED, state=ArrivedState())
        fsm.add_state(name=BROKEN_DOWN, state=BrokenDownState())

        # SPADE only allows the transitions we register here. If a state
        # tries to go somewhere not listed, the FSM stops with an error.
        fsm.add_transition(source=START, dest=DRIVE)
        fsm.add_transition(source=DRIVE, dest=DRIVE)
        fsm.add_transition(source=DRIVE, dest=GAS_STATION)
        fsm.add_transition(source=DRIVE, dest=FLAT_TIRE)
        fsm.add_transition(source=DRIVE, dest=ARRIVED)
        fsm.add_transition(source=DRIVE, dest=BROKEN_DOWN)
        fsm.add_transition(source=GAS_STATION, dest=DRIVE)
        fsm.add_transition(source=FLAT_TIRE, dest=DRIVE)
        fsm.add_transition(source=FLAT_TIRE, dest=BROKEN_DOWN)

        self.add_behaviour(fsm)


async def main():
    # Works with the local server from "spade run". If you use another XMPP
    # server, change the JID and password to an account that exists there.
    car = CarAgent("car@localhost", "password")
    await car.start(auto_register=True)
    await spade.wait_until_finished(car)


if __name__ == "__main__":
    spade.run(main())
