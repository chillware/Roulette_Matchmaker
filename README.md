# Roulette Simulator

This repository contains a Python script that simulates a roulette betting strategy. The strategy involves progressively increasing bet amounts after losses and optionally splitting large loss amounts to manage bet sizes.

## Betting Strategy Overview

1. **Initialization:**
   - The betting table starts with a predefined sequence (e.g., ten 1's).

2. **Bet Calculation:**
   - The bet amount for each spin is determined by adding the first and last numbers in the table.
   - This amount is placed on both dozens. For example, if the bet amount calculated is 2, then a total of 4 units (2 on each dozen) is bet.

3. **Spin the Wheel:**
   - The roulette wheel is spun to get a result.

4. **Determine Win or Loss:**
   - A win occurs if the spin result falls within one of the two selected dozens (first dozen: 1-12, second dozen: 13-24).

5. **Update Table and Balance:**
   - **Win Case:**
     - If the bet wins, remove the first and last numbers from the table.
     - Increase the balance by the bet amount (since each dozen pays 2:1 but only one dozen can win, we get back the amount we bet).
   - **Loss Case:**
     - If the bet loses, add the total amount lost to the end of the table, with the option to split this amount into smaller parts if it exceeds a certain value.

6. **Check for Session Completion:**
   - A session is complete when the table is emptied (all numbers are removed).

7. **Repeat:**
   - Start a new session with the initial table configuration once a session is completed.

## Configuration Options

- **num_sessions:** Number of sessions to run the simulation for.
- **use_double_zero:** Whether to use a double zero (American) wheel.
- **initial_table:** Initial sequence of numbers for bet calculation (default is ten 1's).
- **dozens_to_bet:** Tuple indicating which dozens to bet on (default is first two dozens).
- **max_split_value:** Maximum value for splitting loss amounts. Set to `None` to disable splitting.

## Usage

1. **Adjust Configuration:**
   - Modify the configuration parameters in the `RouletteSimulator` class initialization as needed.

2. **Run Simulation:**
   - Call the `run_simulation` method to start the simulation.

3. **Analyze Results:**
   - The simulation results include the final balance, total spins, number of sessions, total bet, total loss, total profit, and the highest bet amount during the run.
