## ~~What~~ Why is **TechniFund**


TechniFund is a free, down-to-earth investor's best friend for quality investments in the Indonesian Stock Market (Bursa Saham Indonesia).

TechniFund is more than just a calculator. It is capable of performing tasks that produce valuable insights for your trading and investment strategies in stock equity.

## Permissions Required

No additional permissions or data are required.

## System Requirements

As long as your computer runs Command Prompt/Powershell/Terminal/Notepad, **TechniFund** will always work. However, it requires several applications/packages:
- Python (version 3.11.5 or later; I haven't tested previous versions yet)
- Pandas

## How to Run

1. Go to the `Code` tab, click the green `Code` button, and then `Download ZIP` to download all contents of this repository in ZIP format **(Make sure you have a ZIP extractor program on your PC)**.
2. Extract all the contents into a `/technifund` folder.
3. Go to that folder `technifund` and copy the full address.
4. Simple approach:
   - Windows: Double-click the `run.bat` file to run the program.
   - Mac/Linux: Double-click the `run_mac.sh` file to run the program.
5. Programmer approach: To run this script, execute the command `python technifund.py` in the terminal.


## Features

- **Profit Calculator**  
  Calculate an investor's potential gain/loss of any stock based on the following factors:  
  - Stock quantity
  - Stock entry/buy/long price
  - Stock exit/sell/short price

  Simple formula for your imagination (relax, this calculation only occurs in the back-end process):  
  `(stock_quantity * 100 * sell_price) - (stock_quantity * 100 * buy_price) - deductibles`

- **Average Calculator**  
  Calculate an investor's final potential gain/loss of an investment in any stock based on the following factors:
  - Sum of total funds invested (portfolios)
  - Stock exit/sell/short price

  Simple formula for your imagination (relax, this calculation only occurs in the back-end process):  
  `sum_of_portfolios - (sum_of_stock_quantity * 100 * sell_price) - deductibles`

- **Scalping/Trading Planner** **(Coming soon!)**  
  Calculate an investor's target price based on the given expected target gain/loss, based on the following factors:  
  - Stock quantity
  - Stock entry/buy/long price
  - Gain/loss percentage (%)

- **Dividend Yield Estimator** **(Coming soon!)**  
  Calculate an investor's potential dividend income from any stock equity invested based on the following factors:  
  - Stock quantity
  - Dividend per share
  - Taxpayer status (Yes/No)

- **Money Management** **(Coming soon!)**  
  Calculate how much money you can invest in any stock equity based on the following factors:
  - Cash settled
  - Stock current price
  - Target gain (percentage)
  - Stop loss (percentage)

- **Export Session** **(Coming soon!)**  
  Export current session data and calculations to CSV for further usage/calculations when revisiting the **TechniFund** app again.

- **Import Session** **(Coming soon!)**  
  Import previous or older session data to continue performing calculations based on that data.

## Version Update Remarks
- v1.0.0
  - Added broker's buy and sell-fee rate setting at the app initialization.  
  - Added feature for **editing registered broker's buy/sell rate** after app initialization, now possible under menu "**[1] Edit broker fee setting**".
  - Added feature for saving the result of profit calculation output under menu "**[1] Edit broker fee setting**".
  - Added feature for simulating a **profit/loss calculation** under menu "**[2] Profit Calculator**".
  - Added feature for saving the result of profit calculation output under menu "**[2] Profit Calculator**".

## Developer's Story  
I graduated from the University of Indonesia with a major in Sociology. While I understand there may be some misconceptions about my studies (about what have I learnt and done mostly), I can summarize that I spent most of my time as a student learning both quantitative and qualitative social research, descriptive and inferential statistics, basic calculus, and various data processing tools, including SPSS, Excel, and Gephi. After graduation, I worked as a research and development officer at a governmental institution for about a year and a half. Following that, I transitioned to a senior analyst role in the business advisory department of a public affairs consulting firm. In both positions, my primary responsibilities included quantitative research and end-to-end data processing, from data collection to prediction and visualization. After resigning from my most recent position, I attended and completed a data science bootcamp to further enhance my mathematics and programming skills, which I believe will complement my existing business knowledge and experience.

I started participating in the Indonesian stock market in 2018 and have achieved a +8,000% portfolio growth since committed to delving into securities technical (trading) and fundamental (investing) analysis. I hold titles such as Associate Wealth Planner (AWP), Regular Securities Analyst (RSA), and Certified Risk Associate (CRA) following my full name and academic title.

Many of my colleagues have asked me, "How did you achieve such profitability?" but most often, I encounter questions that imply, "I want to replicate your profitability ASAP."

To be honest, there are no instant results in investing. We all exist on the same time dimension, hence facing equal opportunities and threats. Strategic actions and tactical knowledge differentiate the end result, determining whether we, or one of us, achieve the best profitability, or even the worst loss.

Hence, allow me to introduce you to **TechniFund**, where I found the summarization of both technical and fundamental analysis in stock trading and investment. Basically, users can input numbers, and the machine will automatically perform calculations and provide raw insights.

I understand that this application is just an 'application,' meaning it will not always replace the role of your official financial partners, who may offer further contextual and human approaches to investing consultations. Additionally, minor miscalculations due to rounding, division, or percentage biases are possible to occurs.

As an open-sourced program, your feedback matters. Should you have further suggestions or reports about this program, please create an issue.