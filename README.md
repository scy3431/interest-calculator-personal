# Interest Calculator for Joint Bank Accounts

A simple web tool to calculate how interest should be shared between two people who have contributed different amounts to a joint bank account. It also calculates a "fairness" percentage and visualizes the data with interactive charts.

## Features

- **Contribution Input**: Enter each person's initial contribution and the total amount after interest
- **Share Calculation**: Determines each person's fair share based on their contribution percentage
- **Fairness Check**: Computes the fairness of the interest distribution
- **Data Visualization**: Displays a pie chart for shares and a bar chart for contributions
- **Export Options**: Export results to a CSV file or save the charts as PNG images
- **Custom View**: Easily show or hide the charts

## Technologies Used

- **HTML5** for structure
- **CSS3** for styling
- **JavaScript (Vanilla)** for core logic and interactivity
- **Chart.js** for data visualization

## How to Use

1. Open the `index.html` file in your web browser
2. Enter the contributions for **Person 1** and **Person 2**, along with the **Total After Interest**
3. Click the **"Calculate Shares"** button to see the results
4. Use the checkboxes to toggle the visibility of the charts
5. Click the **"Export"** buttons to save your data or charts

## Example

If Person 1 contributed **$4,000**, Person 2 contributed **$6,000**, and the total after interest is **$11,500**:

- **Person 1's Share**: $4,600
- **Person 2's Share**: $6,900
- **Fairness**: 100%

## Installation

**No installation is required!** Simply:

1. Download the `index.html` file
2. Open it directly in a modern web browser
3. Start calculating interest shares

## Browser Compatibility

This tool works in all modern web browsers including:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

## File Structure

```
Interest-Calculator/
├── index.html          # Main application file
├── README.md           # This file
└── assets/             # (if you have separate CSS/JS files)
    ├── style.css
    └── script.js
```

## Contributing

Feel free to enhance this project by adding:
- Support for more than 2 people
- Different interest calculation methods
- Historical tracking of calculations
- Mobile-responsive design improvements
- Additional export formats
