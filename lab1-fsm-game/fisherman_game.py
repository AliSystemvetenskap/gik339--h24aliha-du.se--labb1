# Lab 1 - FSM game, Distributed computing GIK2NX
# Group members:
#   Name 1
#   Name 2
#   Name 3
#
# The Fisherman
# A fisherman agent rows out to sea and has to catch 10 fish to feed the village.
# The problem is the weather. Storms can show up at any time and damage the boat,
# and if the boat breaks the fisherman sinks and the game is lost. Even on the way
# home a seagull might steal some fish, so he may have to turn around and fish more.
# Almost everything is decided by random numbers, so no two games end the same way.
#
# How to run: start the built-in SPADE server with "spade run" in one terminal,
# then run "python fisherman_game.py" in another one.

import asyncio
import random

import spade
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State

# Names of all states. We keep them as constants so we don't misspell them
# when we add transitions further down.
START = "START"
SAIL_OUT = "SAIL_OUT"
FISHING = "FISHING"
STORM = "STORM"
GO_HOME = "GO_HOME"
WIN = "WIN"
SUNK = "SUNK"

FISH_GOAL = 10      # how many fish the village needs
BOAT_HEALTH = 3     # how many hits the boat can take before it breaks


class FishermanBehaviour(FSMBehaviour):
    # The FSM itself. on_start/on_end run once, before the first state and after the last.
    async def on_start(self):
        print("=== The Fisherman ===")

    async def on_end(self):
        print("=== Game over ===")
        # When the FSM is done there is nothing more for the agent to do, so we stop it.
        await self.agent.stop()


class StartState(State):
    async def run(self):
        # The agent object is shared between all states, so we store the game
        # values there. That way every state can read and change them.
        self.agent.fish = 0
        self.agent.boat = BOAT_HEALTH
        self.agent.trips = 0
        print(f"The village needs {FISH_GOAL} fish before dark. The boat can take {BOAT_HEALTH} hits.")
        await asyncio.sleep(1)
        self.set_next_state(SAIL_OUT)


class SailOutState(State):
    async def run(self):
        self.agent.trips += 1
        print(f"\nThe fisherman rows out to sea (trip {self.agent.trips}).")
        await asyncio.sleep(1)

        # 1 in 4 chance that the weather is already bad when he gets out there.
        if random.random() < 0.25:
            print("Dark clouds are coming in...")
            self.set_next_state(STORM)
        else:
            print("The sea is calm, time to throw out the net.")
            self.set_next_state(FISHING)


class FishingState(State):
    async def run(self):
        caught = random.randint(0, 3)
        self.agent.fish += caught
        print(f"Caught {caught} fish. Total: {self.agent.fish}/{FISH_GOAL}")
        await asyncio.sleep(1)

        # Enough fish -> head home. Otherwise keep fishing, but each round
        # there is a 30 % chance that a storm interrupts.
        if self.agent.fish >= FISH_GOAL:
            self.set_next_state(GO_HOME)
        elif random.random() < 0.3:
            self.set_next_state(STORM)
        else:
            self.set_next_state(FISHING)


class StormState(State):
    async def run(self):
        damage = random.randint(0, 2)   # 0 means he got lucky and the boat held
        self.agent.boat = max(0, self.agent.boat - damage)
        print(f"STORM! The boat takes {damage} damage. Boat health: {self.agent.boat}/{BOAT_HEALTH}")
        await asyncio.sleep(1)

        if self.agent.boat <= 0:
            self.set_next_state(SUNK)
        else:
            # The storm passes and he rows out again to find a new fishing spot.
            print("The storm passes.")
            self.set_next_state(SAIL_OUT)


class GoHomeState(State):
    async def run(self):
        print("\nThe fisherman has enough fish and rows back to the village.")
        await asyncio.sleep(1)

        # A seagull might steal some fish on the way. If he ends up under the
        # goal he has to turn around, so this state can lead back to FISHING.
        if random.random() < 0.4:
            stolen = random.randint(1, 3)
            self.agent.fish -= stolen
            print(f"A seagull steals {stolen} fish! Now he has {self.agent.fish}.")

        if self.agent.fish >= FISH_GOAL:
            self.set_next_state(WIN)
        else:
            print("Not enough anymore, back out to sea.")
            self.set_next_state(FISHING)


class WinState(State):
    # End state: we don't call set_next_state, so the FSM stops here.
    async def run(self):
        print(f"\nHe made it home with {self.agent.fish} fish after {self.agent.trips} trip(s). "
              f"The village eats tonight. YOU WIN!")


class SunkState(State):
    # The other end state.
    async def run(self):
        print(f"\nThe boat breaks apart and sinks with {self.agent.fish} fish on board. YOU LOSE!")


class FishermanAgent(Agent):
    async def setup(self):
        fsm = FishermanBehaviour()

        fsm.add_state(name=START, state=StartState(), initial=True)
        fsm.add_state(name=SAIL_OUT, state=SailOutState())
        fsm.add_state(name=FISHING, state=FishingState())
        fsm.add_state(name=STORM, state=StormState())
        fsm.add_state(name=GO_HOME, state=GoHomeState())
        fsm.add_state(name=WIN, state=WinState())
        fsm.add_state(name=SUNK, state=SunkState())

        # SPADE only allows a state to move to another state if the transition
        # is registered here, so this list is basically our FSM diagram in code.
        fsm.add_transition(source=START, dest=SAIL_OUT)
        fsm.add_transition(source=SAIL_OUT, dest=FISHING)
        fsm.add_transition(source=SAIL_OUT, dest=STORM)
        fsm.add_transition(source=FISHING, dest=FISHING)
        fsm.add_transition(source=FISHING, dest=STORM)
        fsm.add_transition(source=FISHING, dest=GO_HOME)
        fsm.add_transition(source=STORM, dest=SAIL_OUT)
        fsm.add_transition(source=STORM, dest=SUNK)
        fsm.add_transition(source=GO_HOME, dest=FISHING)
        fsm.add_transition(source=GO_HOME, dest=WIN)

        self.add_behaviour(fsm)


async def main():
    # Same login as in the Hello Dummy Agent example. Change it if you use your own XMPP server.
    agent = FishermanAgent("fisherman@localhost", "password")
    await agent.start(auto_register=True)

    # Wait until the agent has stopped itself in on_end().
    await spade.wait_until_finished(agent)


if __name__ == "__main__":
    spade.run(main())
