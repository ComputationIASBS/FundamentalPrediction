# FundamentalPrediction
Stock market prediction using fundamental features

# Running the Code

To run the code for each approach:

1. **Navigate to the Respective Folder:** Go to the directory related to the specific method you want to run.

2. **Execute "main.py":** Run the "main.py" file within that folder.

   This will create a directory named "Results" where the program's output will be organized in each step.

After completing the execution of "main.py" for each method, you can visualize the final results of each method by running the **"generating_results_tables.ipynb"** file section by section using **Jupyter Notebook**.

Enjoy exploring the results!

The dataset has been prepared by [Kamran Abdi](https://github.com/Rayan1392), and the implementation has been done by [Hossein Rezaei](https://github.com/HosseinRezaei951). 

# Data

Within the repository's root directory, you will find a [Data](https://github.com/ComputationIASBS/FundamentalPrediction/tree/main/Data) folder housing a CSV file. Detailed descriptions for each of the columns can be found here.

1. **CompanyId:** The unique identifier for each company
2. **PersianYear:** Persian Calendar Year
3. **Return:**  "Return" in the context of finance and investment refers to the gain or loss made on an investment over a specific period, typically expressed as a percentage of the initial investment or capital. Returns are a fundamental concept in finance and are used to evaluate the performance and profitability of investments, including stocks, bonds, real estate, and other assets. There are various types of returns, each serving a specific purpose. In this context our mean is Total Return, Total return measures the overall gain or loss on an investment, considering all sources of return, including price appreciation (capital gains) and any income generated (such as dividends or interest). It is often expressed as a percentage of the initial investment or over a specific period.
4. **Beta:** Beta, often referred to as "Beta coefficient" or simply "Beta," is a financial metric used to measure the sensitivity of a stock's returns to changes in the overall market's returns. It is a fundamental concept in the field of finance and investment analysis, particularly in the context of portfolio management and risk assessment.

A stock's Beta is calculated through statistical analysis, typically by regressing the historical returns of the stock against the returns of a relevant market index, such as the S&P 500. The formula for Beta is as follows:

Beta = Covariance (Stock Returns, Market Returns) / Variance (Market Returns)

In this formula:

Covariance measures how the returns of the stock and the market move together or diverge from each other over time. A positive covariance indicates that the stock's returns tend to move in the same direction as the market's returns, while a negative covariance suggests they move in opposite directions.

Variance measures the overall volatility (risk) of the market's returns.

The interpretation of Beta values is as follows:

A Beta of 1: If a stock has a Beta of 1, it means its returns tend to move in line with the market. If the market goes up by 1%, the stock, on average, is expected to go up by 1%, and if the market goes down by 1%, the stock is expected to go down by 1%.

A Beta greater than 1: If a stock has a Beta greater than 1 (e.g., Beta of 1.2), it is considered more volatile than the market. It is expected to have larger price swings, both up and down, compared to the market. A Beta of 1.2 means that if the market goes up by 1%, the stock, on average, is expected to go up by 1.2%, and vice versa.

A Beta less than 1: If a stock has a Beta less than 1 (e.g., Beta of 0.8), it is considered less volatile than the market. It is expected to have smaller price fluctuations compared to the market. A Beta of 0.8 means that if the market goes up by 1%, the stock, on average, is expected to go up by 0.8%, and vice versa.

A Beta of 0: If a stock has a Beta of 0, it suggests that its returns are not correlated with the market's returns. This is relatively rare and implies that the stock's performance is driven by factors other than the broader market.

A negative Beta: A negative Beta suggests that the stock's returns tend to move in the opposite direction of the market. For example, if the market goes up, a stock with a negative Beta may go down.

Beta is a useful tool for investors to assess the risk and return potential of a stock within the context of the broader market. A Beta greater than 1 indicates higher volatility and potentially higher returns but also higher risk, while a Beta less than 1 indicates lower volatility and potentially lower returns but also lower risk. It helps investors make informed decisions about portfolio diversification and risk management.
5. **Debt_to_total_assets_ratio:** The "Debt to Total Assets Ratio" is a financial metric that assesses the proportion of a company's total assets that are financed by debt. It is a key indicator of a company's capital structure and financial leverage. The formula to calculate the Debt to Total Assets Ratio is as follows:

Debt to Total Assets Ratio = (Total Debt / Total Assets) * 100

In this formula:

Total Debt represents all of a company's outstanding debt, including both short-term and long-term debt obligations. It encompasses loans, bonds, and other forms of borrowing.

Total Assets represent the company's total holdings, including cash, accounts receivable, inventory, property, plant, equipment, and other assets.

The Debt to Total Assets Ratio is expressed as a percentage and provides insights into the company's financial risk and the extent to which it relies on debt to finance its operations and acquisitions. A higher ratio suggests a larger proportion of the company's assets are financed by debt, which may indicate higher financial risk due to interest payments and repayment obligations.

Investors, creditors, and financial analysts use this ratio to assess a company's financial health and its risk profile. A lower ratio is generally considered more favorable, as it suggests a lower level of financial leverage and potentially less financial risk. However, the optimal Debt to Total Assets Ratio can vary by industry and company, and it's essential to consider industry norms and the company's specific circumstances when interpreting this metric.
6. **Operating_profit_to_sale:** The "Operating Profit to Sales" ratio, often referred to as the "Operating Profit Margin," is a financial metric that assesses the profitability of a company's core operating activities as a percentage of its total sales or revenue. It measures how efficiently a company is generating profit from its primary business operations, excluding non-operating income and expenses such as interest and taxes.

The formula to calculate the Operating Profit to Sales ratio is as follows:

Operating Profit Margin = (Operating Profit / Total Sales) * 100

In this formula:

Operating Profit represents the profit generated from a company's core operating activities, calculated by subtracting operating expenses (e.g., cost of goods sold, operating overhead) from total sales or revenue.

Total Sales, also known as revenue, represents the total income generated from the company's primary business operations.

The Operating Profit Margin is expressed as a percentage and provides insight into how effectively a company manages its operating costs and generates profit from its core business activities. A higher operating profit margin indicates that the company is efficient in controlling its operating expenses, resulting in higher profitability.

Investors, analysts, and business managers use the Operating Profit Margin to assess a company's operational efficiency and profitability. It helps in evaluating a company's ability to cover its operating costs, make necessary investments, and generate profit from its primary operations. Comparing the operating profit margin to industry benchmarks or historical values can provide valuable insights into a company's financial health and competitiveness.
