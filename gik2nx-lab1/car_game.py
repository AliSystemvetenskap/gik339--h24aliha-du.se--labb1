# Lab 1 GIK2NX, group 11 - Ali Hasan, Bilal Ahmed Adem, Karim Al Hashoom
# Car has to drive 100 km home with 15 l fuel. Can find gas or get a flat tire.
# Run "spade run" first, then this file.

import asyncio
import random

import spade
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State

START = "START"
DRIVE = "DRIVE"
GAS_STATION = "GAS_STATION"
FLAT_TIRE = "FLAT_TIRE"
ARRIVED = "ARRIVED"  # win
BROKEN_DOWN = "BROKEN_DOWN"  # lose

GOAL_KM = 100


class TripFSM(FSMBehaviour):
    async def on_start(self):
        print("=== The trip begins ===")

    async def on_end(self):
        # stop the agent so the program ends
        print("=== Game over ===")
        await self.agent.stop()


class StartState(State):
    async def run(self):
        # saved on the agent so all states can use them
        self.agent.km = 0
        self.agent.fuel = 15
        self.agent.reason = ""
        print(f"You need to drive {GOAL_KM} km home and you have {self.agent.fuel} litres of fuel.")
        self.set_next_state(DRIVE)


class DriveState(State):
    async def run(self):
        a = self.agent
        await asyncio.sleep(0.5)

        driven = random.randint(10, 20)
        used = random.randint(2, 5)
        a.km += driven
        a.fuel = max(a.fuel - used, 0)
        print(f"Drove {driven} km (used {used} l) -> {a.km} km done, {a.fuel} l left")

        # check home first so you win even if the tank is empty
        if a.km >= GOAL_KM:
            self.set_next_state(ARRIVED)
        elif a.fuel <= 0:
            a.reason = "The tank is empty"
            self.set_next_state(BROKEN_DOWN)
        elif random.random() < 0.1:
            self.set_next_state(FLAT_TIRE)
        elif a.fuel < 8 and random.random() < 0.5:
            self.set_next_state(GAS_STATION)
        else:
            self.set_next_state(DRIVE)


class GasStationState(State):
    async def run(self):
        a = self.agent
        await asyncio.sleep(0.5)
        bought = random.randint(5, 15)
        a.fuel += bought
        print(f"Found a gas station! Bought {bought} l, now {a.fuel} l in the tank.")
        self.set_next_state(DRIVE)


class FlatTireState(State):
    async def run(self):
        a = self.agent
        await asyncio.sleep(0.5)
        print("BANG! Flat tire. You get out and check the spare tire...")
        if random.random() < 0.7:
            print("The spare tire is fine, you change it and drive on.")
            self.set_next_state(DRIVE)
        else:
            a.reason = "The spare tire was flat too"
            self.set_next_state(BROKEN_DOWN)


class ArrivedState(State):
    async def run(self):
        # no next state = end of the FSM
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
    # 127.0.0.1 instead of localhost, on Windows localhost can fail to connect.
    # Sometimes the first try still fails, so we try a few times.
    for attempt in range(5):
        car = CarAgent("car@127.0.0.1", "password")
        try:
            await car.start(auto_register=True)
            break
        except Exception:
            print("Could not connect to the server, trying again...")
            await asyncio.sleep(2)
    else:
        print("No connection. Is the server running (spade run)?")
        return
    await spade.wait_until_finished(car)


if __name__ == "__main__":
    spade.run(main())
