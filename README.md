# Python School Math Assistant

A responsive, dark-themed web application built using Python Flask, HTML5, and CSS3. This project acts as a functional math engine designed to automate school formulas, specifically focusing on 7th-grade laws of indices and the Pythagoras theorem.

## Core Python Concepts Applied

- **Lecture 2 Conditional Logic (`if/elif/else`):** Manages dropdown selection configurations to isolate user topics, math operators, and target solving elements cleanly.
- **Python Exponent Operators (`**`):** Implemented native double-asterisk syntax power flags to calculate multi-layered algebraic exponential indices.
- **Built-in Math Library Functions:** Imported the standard Python `math` module to leverage geometric algorithms like `math.sqrt()` to compute triangles.
- **Validation Logic Handling:** Engineered safety validation structures to catch division anomalies, invalid text values (`ValueError`), or breaking operations (like checking that the hypotenuse remains the longest side).

## Covered Equations & Laws

### 1. Laws of Indices (Grade 7)
* **Product Rule:** $a^m \times a^n = a^{m+n}$
* **Quotient Rule:** $a^m \div a^n = a^{m-n}$
* **Power of a Power Rule:** $(a^m)^n = a^{m \times n}$

### 2. Pythagoras Theorem
* **Hypotenuse Verification Check:** $c = \sqrt{a^2 + b^2}$
* **Leg Length Calculations:** $a = \sqrt{c^2 - b^2}$

## Tech Stack Used

- **Backend Logic Server:** Python 3, Flask Web Routing Node
- **Frontend Presentation:** HTML5, Embedded JavaScript Switchers, Styled UI CSS3

## Local Server Installation Instructions

1. Clone this project repository folder to your local desktop environment.
2. Verify that you have the Flask package manager installed:
   ```bash
   pip install flask
   ```
3. Initialize the backend engine script:
   ```bash
   python app.py
   ```
4. Navigate your target web browser window address node to: `http://127.0.0.1:5000`
