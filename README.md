**Overview**

This Python script is designed to analyze financial data and identify optimal buy indices based on a predefined trading strategy. Additionally, it calculates the portfolio value based on the performance of the trading strategy.

**Approach**

The find_optimal_buy_indices() function is defined to perform the core analysis. It takes a list of prices as input and returns a list of optimal buy indices along with the calculated portfolio value.

The function iterates over the prices to calculate the rate of return (r) between consecutive price points.
Based on the rate of return, the script assigns a state value (state) to each data point. A state of 1 indicates a positive trend, 0 indicates a sideways movement, and -1 indicates a negative trend.

The function identifies optimal buy indices based on the defined trading strategy. It looks for transitions from a sideways movement and negative trend to a positive trend (state != 1 and next_state == 1).
Retrieving Dates of Optimal Buy Indices:

Once the optimal buy indices are identified, the script retrieves the corresponding dates from the dataset.
