import random

class RouletteSimulator:
    def __init__(self, num_sessions, use_double_zero=False, initial_table=None, dozens_to_bet=(1, 2), max_split_value=None):
        self.num_sessions = num_sessions
        self.use_double_zero = use_double_zero
        self.dozens_to_bet = dozens_to_bet
        self.initial_table = initial_table if initial_table else [1] * 10
        self.max_split_value = max_split_value
        self.reset_simulation()

    def reset_simulation(self):
        self.table = self.initial_table.copy()
        self.balance = 0
        self.total_bet = 0
        self.total_loss = 0
        self.total_profit = 0
        self.current_session = 0
        self.spin_count = 0
        self.highest_bet = 0  # Track the highest bet amount

    def spin_wheel(self):
        if self.use_double_zero:
            wheel = list(range(0, 37)) + [37]  # Adding double zero as 37
        else:
            wheel = list(range(0, 37))  # Single zero wheel
        return random.choice(wheel)

    def bet(self):
        if len(self.table) == 1:
            bet_amount = self.table[0]
        else:
            bet_amount = self.table[0] + self.table[-1]

        total_bet_amount = bet_amount * 2  # Total bet for both dozens

        # Track the highest bet amount
        if total_bet_amount > self.highest_bet:
            self.highest_bet = total_bet_amount

        spin_result = self.spin_wheel()
        dozen_result = self.get_dozen(spin_result)
        win_first = (dozen_result == 1 and self.dozens_to_bet[0] == 1) or (dozen_result == 1 and self.dozens_to_bet[1] == 1)
        win_second = (dozen_result == 2 and self.dozens_to_bet[0] == 2) or (dozen_result == 2 and self.dozens_to_bet[1] == 2)

        win = win_first or win_second

        if win:
            self.balance += bet_amount  # Winning dozen pays 2:1 but we bet on two dozens
            if len(self.table) > 1:
                self.table = self.table[1:-1]
            else:
                self.table = []
        else:
            self.balance -= total_bet_amount  # We lose both bets
            self.add_to_table(total_bet_amount)

        self.total_bet += total_bet_amount
        if not win:
            self.total_loss += total_bet_amount
        self.total_profit = self.balance
        self.spin_count += 1

        return spin_result, dozen_result, win_first, win_second, total_bet_amount

    def get_dozen(self, number):
        if number == 0 or (self.use_double_zero and number == 37):
            return 0
        elif 1 <= number <= 12:
            return 1
        elif 13 <= number <= 24:
            return 2
        else:
            return 3

    def add_to_table(self, amount):
        if self.max_split_value and amount > self.max_split_value:
            split_parts = amount // self.max_split_value
            remainder = amount % self.max_split_value
            for _ in range(split_parts):
                self.table.append(self.max_split_value)
            if remainder > 0:
                self.table.append(remainder)
        else:
            self.table.append(amount)

    def run_simulation(self):
        results = []
        while self.current_session < self.num_sessions:
            while self.table:
                spin_result, dozen_result, win_first, win_second, total_bet_amount = self.bet()
                win_dozen = "First" if win_first else "Second" if win_second else "None"
                results.append([self.current_session, self.spin_count, spin_result, dozen_result, total_bet_amount,
                                self.total_bet, self.total_loss, self.total_profit, win_dozen])

            self.current_session += 1
            self.table = self.initial_table.copy()

        return results, {
            "final_balance": self.balance,
            "total_spins": self.spin_count,
            "num_sessions": self.current_session,
            "total_bet": self.total_bet,
            "total_loss": self.total_loss,
            "total_profit": self.total_profit,
            "highest_bet": self.highest_bet  # Include the highest bet amount in the final results
        }

# Run the simulation for 100 sessions with splitting disabled
simulator = RouletteSimulator(num_sessions=100, use_double_zero=False)
spin_results, final_results = simulator.run_simulation()

# Display the first 100 spins and the final results for brevity
print("First 100 Spins:")
print(f"{'Session':<8}{'Spin':<6}{'Result':<8}{'Dozen':<6}{'Total Bet Amount':<16}{'Total Bet':<12}{'Total Loss':<12}{'Profit':<8}{'Win Dozen':<10}")
for result in spin_results[:100]:
    print(f"{result[0]:<8}{result[1]:<6}{result[2]:<8}{result[3]:<6}{result[4]:<16}{result[5]:<12}{result[6]:<12}{result[7]:<8}{result[8]:<10}")

print("\nFinal Results:")
print(f"Final Balance: {final_results['final_balance']}")
print(f"Total Spins: {final_results['total_spins']}")
print(f"Number of Sessions: {final_results['num_sessions']}")
print(f"Total Bet: {final_results['total_bet']}")
print(f"Total Loss: {final_results['total_loss']}")
print(f"Total Profit: {final_results['total_profit']}")
print(f"Highest Bet Amount: {final_results['highest_bet']}")

# Run the simulation for 100 sessions with a max split value of 100
simulator_with_split = RouletteSimulator(num_sessions=100, use_double_zero=False, max_split_value=100)
spin_results_with_split, final_results_with_split = simulator_with_split.run_simulation()

# Display the first 100 spins and the final results for brevity with splitting enabled
print("\nFirst 100 Spins with Splitting:")
print(f"{'Session':<8}{'Spin':<6}{'Result':<8}{'Dozen':<6}{'Total Bet Amount':<16}{'Total Bet':<12}{'Total Loss':<12}{'Profit':<8}{'Win Dozen':<10}")
for result in spin_results_with_split[:100]:
    print(f"{result[0]:<8}{result[1]:<6}{result[2]:<8}{result[3]:<6}{result[4]:<16}{result[5]:<12}{result[6]:<12}{result[7]:<8}{result[8]:<10}")

print("\nFinal Results with Splitting:")
print(f"Final Balance: {final_results_with_split['final_balance']}")
print(f"Total Spins: {final_results_with_split['total_spins']}")
print(f"Number of Sessions: {final_results_with_split['num_sessions']}")
print(f"Total Bet: {final_results_with_split['total_bet']}")
print(f"Total Loss: {final_results_with_split['total_loss']}")
print(f"Total Profit: {final_results_with_split['total_profit']}")
print(f"Highest Bet Amount: {final_results_with_split['highest_bet']}")
