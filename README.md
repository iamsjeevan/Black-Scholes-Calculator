
# Black-Scholes Option Pricing Calculator

This project implements the Black-Scholes model to calculate the theoretical price of European call and put options. It is a Python-based tool designed to aid traders, students, and financial enthusiasts in understanding and applying the Black-Scholes formula for options pricing.

## Features

- Calculate the price of European **Call** and **Put** options.
- Input parameters include:
  - Current stock price (S)
  - Strike price (K)
  - Time to maturity (T, in years)
  - Risk-free interest rate (r, as a decimal)
  - Volatility (σ, as a decimal)

## Requirements

- Python 3.7 or later
- Libraries:
  - `math`
  - `scipy.stats` (for normal distribution calculations)

Install required Python libraries using:
```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/black-scholes-calculator.git
   cd black-scholes-calculator
   ```

2. Run the script:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Input the required parameters as prompted:
   - Stock price (S)
   - Strike price (K)
   - Time to maturity (T)
   - Risk-free rate (r)
   - Volatility (σ)
   
2. The script calculates and displays the option prices for:
   - Call Option
   - Put Option


## Formula

The Black-Scholes formula is defined as:

### Call Option:
\[ C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2) \]

### Put Option:
\[ P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1) \]

Where:
\[ d_1 = \frac{\ln(S / K) + (r + σ^2 / 2) \cdot T}{σ \cdot \sqrt{T}} \]
\[ d_2 = d_1 - σ \cdot \sqrt{T} \]

- \( N(d) \): Cumulative distribution function of the standard normal distribution.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [Wikipedia: Black-Scholes Model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
- [scipy.stats Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)

---

Happy Calculating!
