# GIK2NX Distributed computing - Lab 1: FSM game
# Group members:
#   - Ali Hasan
#   - Bilal Ahmed Adem
#   - Karim Al Hashoom
#
# The game: a hiker agent tries to reach the top of a mountain (100 m)
# before it gets dark (after 15 hours). Climbing costs energy, resting gives energy
# back but costs time, and sometimes a storm hits and pushes the hiker back down.
# Everything is random, so you never get the same game twice.
#
# How to run:
#   1. Start the SPADE XMPP server in one terminal:   spade run
#   2. Run the game in another terminal:              python mountain_game.py

import asyncio
import random

import spade
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State

# State names. We keep them as constants so a typo in a transition
# gives an error right away instead of silently doing nothing.
START = "START"
CLIMB = "CLIMB"
REST = "REST"
STORM = "STORM"
SUMMIT = "SUMMIT"  # end state - the hiker wins
DARK = "DARK"      # end state - the hiker loses

GOAL_HEIGHT = 100
SUNSET = 15


class HikeFSM(FSMBehaviour):
    async def on_start(self):
        print("=== The hike begins ===")

    async def on_end(self):
        # The FSM is done (we ended in SUMMIT or DARK), so we stop the agent too.
        # Otherwise main() would wait forever.
        print("=== Game over ===")
        await self.agent.stop()


class StartState(State):
    async def run(self):
        # The game values live on the agent, not in the states. Every state is its
        # own object, so the agent is the easiest place they can all reach.
        self.agent.height = 0
        self.agent.energy = 10
        self.agent.time = 0
        print("You stand at the foot of the mountain. Reach 100 m before it gets dark!")
        self.set_next_state(CLIMB)


class ClimbState(State):
    async def run(self):
        a = self.agent
        await asyncio.sleep(0.5)  # small pause so the game is readable when it runs

        # One climb = one hour. How far you get depends on luck and on how tired you are.
        step = random.randint(5, 20)
        if a.energy < 4:
            step //= 2
            print("Your legs are heavy...")
        a.height += step
        a.energy -= random.randint(1, 3)
        a.time += 1
        print(f"[hour {a.time}] Climbed {step} m -> height {a.height} m, energy {a.energy}")

        # Order matters here: reaching the top wins even if it is the last hour.
        if a.height >= GOAL_HEIGHT:
            self.set_next_state(SUMMIT)
        elif a.time >= SUNSET:
            self.set_next_state(DARK)
        elif random.random() < 0.2:
            self.set_next_state(STORM)
        elif a.energy <= 2:
            self.set_next_state(REST)
        else:
            self.set_next_state(CLIMB)


class RestState(State):
    async def run(self):
        a = self.agent
        await asyncio.sleep(0.5)
        # Resting is the trade-off of the game: you get energy back but lose time.
        gained = random.randint(3, 6)
        a.energy += gained
        a.time += 1
        print(f"[hour {a.time}] You sit down and eat something. +{gained} energy (energy {a.energy})")

        if a.time >= SUNSET:
            self.set_next_state(DARK)
        else:
            self.set_next_state(CLIMB)


class StormState(State):
    async def run(self):
        a = self.agent
        await asyncio.sleep(0.5)
        lost = random.randint(5, 15)
        a.height = max(0, a.height - lost)
        a.energy -= 1
        a.time += 1
        print(f"[hour {a.time}] A storm hits! You slide down {lost} m (height {a.height} m)")

        # After a storm you are tired, so you rest if energy is low, otherwise keep going.
        if a.time >= SUNSET:
            self.set_next_state(DARK)
        elif a.energy <= 2:
            self.set_next_state(REST)
        else:
            self.set_next_state(CLIMB)


class SummitState(State):
    async def run(self):
        # No set_next_state here, that is what makes it a final state.
        print(f"You reached the top after {self.agent.time} hours with {self.agent.energy} energy left. You win!")


class DarkState(State):
    async def run(self):
        print(f"It is dark and you are stuck at {self.agent.height} m. You have to camp on the mountain. You lose!")


class HikerAgent(Agent):
    async def setup(self):
        fsm = HikeFSM()
        fsm.add_state(name=START, state=StartState(), initial=True)
        fsm.add_state(name=CLIMB, state=ClimbState())
        fsm.add_state(name=REST, state=RestState())
        fsm.add_state(name=STORM, state=StormState())
        fsm.add_state(name=SUMMIT, state=SummitState())
        fsm.add_state(name=DARK, state=DarkState())

        # SPADE only allows the transitions we register here. If a state
        # tries to go somewhere not listed, the FSM stops with an error.
        fsm.add_transition(source=START, dest=CLIMB)
        fsm.add_transition(source=CLIMB, dest=CLIMB)
        fsm.add_transition(source=CLIMB, dest=REST)
        fsm.add_transition(source=CLIMB, dest=STORM)
        fsm.add_transition(source=CLIMB, dest=SUMMIT)
        fsm.add_transition(source=CLIMB, dest=DARK)
        fsm.add_transition(source=REST, dest=CLIMB)
        fsm.add_transition(source=REST, dest=DARK)
        fsm.add_transition(source=STORM, dest=CLIMB)
        fsm.add_transition(source=STORM, dest=REST)
        fsm.add_transition(source=STORM, dest=DARK)

        self.add_behaviour(fsm)


async def main():
    # Works with the local server from "spade run". If you use another XMPP
    # server, change the JID and password to an account that exists there.
    hiker = HikerAgent("hiker@localhost", "password")
    await hiker.start(auto_register=True)
    await spade.wait_until_finished(hiker)


if __name__ == "__main__":
    spade.run(main())
