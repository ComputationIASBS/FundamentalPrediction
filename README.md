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
4. **Beta:** Beta, often referred to as "Beta coefficient" or simply "Beta," is a financial metric used to measure the sensitivity of a stock's returns to changes in the overall market's returns. It is a fundamental concept in the field of finance and investment analysis, particularly in the context of portfolio management and risk assessment. A stock's Beta is calculated through statistical analysis, typically by regressing the historical returns of the stock against the returns of a relevant market index, such as the S&P 500.  
The formula for Beta is as follows:<br><br>
Beta = Covariance (Stock Returns, Market Returns) / Variance (Market Returns)<br>
In this formula:  
Covariance measures how the returns of the stock and the market move together or diverge from each other over time. A positive covariance indicates that the stock's returns tend to move in the same direction as the market's returns, while a negative covariance suggests they move in opposite directions. Variance measures the overall volatility (risk) of the market's returns.  
The interpretation of Beta values is as follows:<br><br>
A Beta of 1:  
If a stock has a Beta of 1, it means its returns tend to move in line with the market. If the market goes up by 1%, the stock, on average, is expected to go up by 1%, and if the market goes down by 1%, the stock is expected to go down by 1%.<br><br>
A Beta greater than 1:  
If a stock has a Beta greater than 1 (e.g., Beta of 1.2), it is considered more volatile than the market. It is expected to have larger price swings, both up and down, compared to the market.  
A Beta of 1.2 means that if the market goes up by 1%, the stock, on average, is expected to go up by 1.2%, and vice versa.<br><br>
A Beta less than 1:  
If a stock has a Beta less than 1 (e.g., Beta of 0.8), it is considered less volatile than the market. It is expected to have smaller price fluctuations compared to the market. A Beta of 0.8 means that if the market goes up by 1%, the stock, on average, is expected to go up by 0.8%, and vice versa.<br><br>
A Beta of 0:  
If a stock has a Beta of 0, it suggests that its returns are not correlated with the market's returns. This is relatively rare and implies that the stock's performance is driven by factors other than the broader market.<br><br>
A negative Beta:  
A negative Beta suggests that the stock's returns tend to move in the opposite direction of the market. For example, if the market goes up, a stock with a negative Beta may go down.<br><br>
Beta is a useful tool for investors to assess the risk and return potential of a stock within the context of the broader market. A Beta greater than 1 indicates higher volatility and potentially higher returns but also higher risk, while a Beta less than 1 indicates lower volatility and potentially lower returns but also lower risk. It helps investors make informed decisions about portfolio diversification and risk management.

5. **Debt_to_total_assets_ratio:** The "Debt to Total Assets Ratio" is a financial metric that assesses the proportion of a company's total assets that are financed by debt. It is a key indicator of a company's capital structure and financial leverage. The formula to calculate the Debt to Total Assets Ratio is as follows:  
Debt to Total Assets Ratio = (Total Debt / Total Assets) * 100 In this formula: Total Debt represents all of a company's outstanding debt, including both short-term and long-term debt obligations. It encompasses loans, bonds, and other forms of borrowing. Total Assets represent the company's total holdings, including cash, accounts receivable, inventory, property, plant, equipment, and other assets. The Debt to Total Assets Ratio is expressed as a percentage and provides insights into the company's financial risk and the extent to which it relies on debt to finance its operations and acquisitions. A higher ratio suggests a larger proportion of the company's assets are financed by debt, which may indicate higher financial risk due to interest payments and repayment obligations. Investors, creditors, and financial analysts use this ratio to assess a company's financial health and its risk profile. A lower ratio is generally considered more favorable, as it suggests a lower level of financial leverage and potentially less financial risk. However, the optimal Debt to Total Assets Ratio can vary by industry and company, and it's essential to consider industry norms and the company's specific circumstances when interpreting this metric.

6. **Operating_profit_to_sale:** The "Operating Profit to Sales" ratio, often referred to as the "Operating Profit Margin," is a financial metric that assesses the profitability of a company's core operating activities as a percentage of its total sales or revenue. It measures how efficiently a company is generating profit from its primary business operations, excluding non-operating income and expenses such as interest and taxes. The formula to calculate the Operating Profit to Sales ratio is as follows:  
Operating Profit Margin = (Operating Profit / Total Sales) * 100  
In this formula:  
Operating Profit represents the profit generated from a company's core operating activities, calculated by subtracting operating expenses (e.g., cost of goods sold, operating overhead) from total sales or revenue.  
Total Sales, also known as revenue, represents the total income generated from the company's primary business operations. The Operating Profit Margin is expressed as a percentage and provides insight into how effectively a company manages its operating costs and generates profit from its core business activities. A higher operating profit margin indicates that the company is efficient in controlling its operating expenses, resulting in higher profitability. Investors, analysts, and business managers use the Operating Profit Margin to assess a company's operational efficiency and profitability. It helps in evaluating a company's ability to cover its operating costs, make necessary investments, and generate profit from its primary operations. Comparing the operating profit margin to industry benchmarks or historical values can provide valuable insights into a company's financial health and competitiveness.

7. **Fixed_asset_turnover:** The fixed asset turnover, also known as fixed asset turnover ratio, is a financial metric that measures how efficiently a company is using its fixed assets (such as buildings, machinery, equipment) to generate sales or revenue. It is calculated by dividing the company's net sales or revenue by its average fixed assets. This ratio indicates how effectively a company is deploying its fixed assets to generate income. A higher fixed asset turnover ratio generally implies better asset utilization and operational efficiency.

8. **Return_from_market:** "Return from the market" typically refers to the profits or gains obtained from investments made in the financial markets, such as stocks, bonds, or other securities. This return is a measure of how well an investment has performed and is usually expressed as a percentage or a monetary amount. It reflects the increase (positive return) or decrease (negative return) in the value of an investment over a specific period (in this context Yearly return of TEDPIX), taking into account factors like capital appreciation, dividends, or interest earned.

9. **Current_assets_ratio:** The "current assets ratio" is a financial ratio that measures a company's ability to cover its short-term liabilities with its current assets. It is calculated by dividing the total current assets by the total current liabilities. This ratio provides insight into a company's liquidity and its capacity to meet its short-term financial obligations. A higher current assets ratio indicates a stronger ability to pay off short-term debts and suggests a more financially stable position.

10. **Working_capital_return:** "Working capital return" typically refers to the return or profit generated from the working capital of a business. Working capital is the difference between a company's current assets (e.g., cash, accounts receivable, inventory) and its current liabilities (e.g., accounts payable, short-term debt). The return on working capital measures how effectively a company is utilizing its short-term assets and liabilities to generate profits. It is not a standard financial ratio but rather a concept that can be evaluated in the context of a specific business or investment strategy.

11. **Longterm_debt_to_equity_ratio:** The "long-term debt to equity ratio" is a financial metric that assesses a company's financial leverage or solvency by comparing its long-term debt (such as loans, bonds, or other obligations with maturities exceeding one year) to its shareholders' equity. It is calculated by dividing long-term debt by shareholders' equity. This ratio provides insight into how much of a company's capital structure is financed through long-term debt as opposed to equity. A high long-term debt to equity ratio can indicate that a company has a significant amount of debt relative to its equity, which may imply higher financial risk. Conversely, a lower ratio suggests a more conservative capital structure with a greater reliance on equity financing. It's an important metric for investors and creditors to assess a company's financial health and risk profile.

12. **Return_ratio_without_risk:** The "return ratio without risk" typically refers to the measure of investment returns or profits achieved without considering or factoring in the associated risk. In finance, such a return is often referred to as the "nominal return" or "gross return." It represents the percentage increase in an investment's value or the profit earned from an investment without adjusting for the level of risk involved.  
It's essential to note that in practice, all investments carry some level of risk, and calculating the actual or realized return often takes into account factors like volatility, market fluctuations, and the potential for loss. Therefore, while a nominal return may provide an initial assessment of an investment's performance, it's crucial to consider risk-adjusted measures like the Sharpe ratio or the risk-free rate when evaluating investment performance in a more comprehensive manner. These measures help assess returns relative to the level of risk taken.

13. **Profit_margin_growth_rate:** The "profit margin growth rate" is a financial metric that measures the rate at which a company's profit margins are changing or increasing over a specific period. It assesses how efficiently a company is managing its costs and generating profits.  
To calculate the profit margin growth rate, you typically compare the profit margin from one period to the profit margin from a previous period and then calculate the percentage change. The formula is as follows:  
Profit Margin Growth Rate = [(Current Period Profit Margin - Previous Period Profit Margin) / Previous Period Profit Margin] * 100  
This metric provides insight into a company's ability to improve its profitability over time. A positive profit margin growth rate suggests that the company is becoming more efficient in managing costs or increasing its revenue relative to the previous period. Conversely, a negative growth rate indicates a decline in profitability.
Investors and analysts often use the profit margin growth rate to assess a company's financial health and its ability to sustain or improve profitability in the future.

14. **Stock_market_value:** The "stock market value" refers to the total market capitalization of a publicly-traded company. It represents the total value of a company's outstanding shares of stock in the financial markets. To calculate the stock market value of a company, you multiply the current market price per share by the total number of outstanding shares.  
Mathematically, Stock Market Value = Current Market Price Per Share × Total Number of Outstanding Shares
This metric is important for investors, analysts, and stakeholders because it provides an estimate of the company's overall worth as perceived by the stock market. It can also be used to compare the relative size of different companies in the stock market and is often used as a key indicator in financial analysis and investment decision-making.

15. **Net_profit_to_sale:** The "Net Profit to Sales" ratio, often referred to as the "Net Profit Margin," is a financial metric that assesses the profitability of a company's operations by measuring the percentage of its total sales revenue that remains as net profit (or net income) after accounting for all expenses, including operating expenses, interest, taxes, and other costs.  
The formula to calculate the Net Profit Margin is as follows:  
Net Profit Margin = (Net Profit / Total Sales) * 100  
In this formula:  
Net Profit, also known as net income or net earnings, represents the profit remaining after all expenses have been deducted from total sales or revenue.  
Total Sales, often referred to as revenue, represents the total income generated from the company's primary business operations.  
The Net Profit Margin is expressed as a percentage and provides a comprehensive view of a company's profitability. It takes into account all income and expenses, including non-operating items and taxes, to assess how effectively a company generates profit from its operations. A higher net profit margin indicates that the company is efficient in managing its expenses and generating profit for each dollar of sales revenue.
Investors, analysts, and business managers use the Net Profit Margin to assess a company's overall financial health, profitability, and ability to generate returns for shareholders. A healthy and consistent net profit margin is generally considered a positive indicator of a company's financial performance. Comparing the net profit margin to industry benchmarks and historical values can help stakeholders evaluate the company's competitive position and financial stability.

16. **Net_profit_to_Gross_profit:** The "Net Profit to Gross Profit" ratio is a financial metric that measures the portion of a company's gross profit that remains as net profit (or net income) after accounting for all operating and non-operating expenses, including interest, taxes, and other costs. This ratio assesses the efficiency of a company in managing its operating expenses and generating profit from its core business operations. The formula to calculate the Net Profit to Gross Profit ratio is as follows:  
Net Profit to Gross Profit Ratio = (Net Profit / Gross Profit) * 100  
In this formula:  
Gross Profit represents the profit remaining after deducting the direct costs associated with producing or purchasing the goods or services that were sold during a specific period. It includes expenses such as raw materials, labor, manufacturing costs, and other directly related costs.  
Net Profit, also known as net income or net earnings, represents the profit remaining after all expenses, including operating expenses, interest expenses, taxes, and other costs, have been deducted from total sales or revenue.  
The Net Profit to Gross Profit ratio is expressed as a percentage and provides insight into how effectively a company manages its operating expenses to generate net profit from its core business activities. A higher ratio indicates that the company is efficient in controlling its operating expenses and retaining a larger proportion of gross profit as net profit. Investors, analysts, and business managers use this metric to assess a company's profitability and operational efficiency. It helps evaluate how well the company converts its gross profit into net profit, considering all income and expenses. A higher ratio is generally considered favorable, as it suggests stronger profitability and efficient cost management.

17. **:** The "Current Ratio" is a financial ratio that measures a company's short-term liquidity and its ability to cover its short-term obligations using its current assets. It's an important indicator of a company's financial health and its capacity to meet its immediate financial needs.<br><br>
The formula to calculate the Current Ratio is as follows:<br><br>
Current Ratio = Current Assets / Current Liabilities<br><br>
In this formula:<br><br>
Current Assets represent assets that are expected to be converted into cash or used up within one year or one operating cycle, whichever is longer. Typical current assets include cash, accounts receivable, inventory, and short-term investments.<br><br>
Current Liabilities represent the company's short-term financial obligations that are due within one year or one operating cycle. These liabilities may include accounts payable, short-term debt, and other short-term obligations.<br><br>
The Current Ratio provides a numerical representation of the company's ability to cover its short-term debts using its short-term assets. A Current Ratio greater than 1 indicates that the company has more current assets than current liabilities, which is generally considered a positive sign of liquidity and the ability to meet short-term obligations<br><br>
However, it's important to note that an excessively high Current Ratio may suggest that a company is not efficiently utilizing its assets and may have too much capital tied up in non-productive assets. Therefore, while a Current Ratio greater than 1 is generally desired, the optimal ratio can vary depending on the industry and the company's specific circumstances.<br><br>
Investors, creditors, and financial analysts use the Current Ratio to assess a company's liquidity and short-term financial health. It is often compared to industry averages and historical values to evaluate changes in a company's financial position over time.  

18. **Net_working_capital:** Net Working Capital, often abbreviated as NWC, is a financial metric that measures the difference between a company's current assets and its current liabilities. It provides insight into a company's short-term liquidity and its ability to cover its short-term financial obligations using its short-term assets. Net Working Capital is a fundamental component of a company's financial health and stability.<br><br>
The formula to calculate Net Working Capital is as follows:<br><br>
Net Working Capital = Current Assets - Current Liabilities<br><br>
In this formula:<br><br>
Current Assets are assets that are expected to be converted into cash or used up within one year or one operating cycle, whichever is longer. Typical current assets include cash, accounts receivable, inventory, and short-term investments.<br>
Current Liabilities are the company's short-term financial obligations that are due within one year or one operating cycle. These liabilities may include accounts payable, short-term debt, and other short-term obligations.<br>
The resulting Net Working Capital figure can be either positive or negative:<br>
A Positive Net Working Capital indicates that a company has more current assets than current liabilities. This suggests that the company has a cushion of liquidity to cover its short-term financial obligations.<br>
A Negative Net Working Capital indicates that a company's current liabilities exceed its current assets. This may indicate a potential liquidity problem, as the company may struggle to meet its short-term obligations with its current resources.<br>
Net Working Capital is a crucial metric for assessing a company's ability to manage its short-term financial needs and its overall financial health. It is used by investors, creditors, and financial analysts to evaluate the company's liquidity position and its capacity to withstand financial challenges. A positive Net Working Capital is generally preferred, but the optimal amount can vary depending on the industry and the company's specific circumstances.

