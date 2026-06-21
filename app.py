from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    formula_type = request.form.get('formula_type', 'indices')

    # Retain input values so they stay on screen after calculating
    inputs = {
        'base': '', 'pow1': '', 'pow2': '', 'indices_op': 'multiply',
        'side_a': '', 'side_b': '', 'side_c': '', 'pythag_find': 'hypotenuse'
    }

    if request.method == 'POST':
        # Capture form values
        for key in inputs.keys():
            if request.form.get(key):
                inputs[key] = request.form.get(key)

        try:
            # ==========================================
            # 1. LAWS OF INDICES LOGIC (Grade 7)
            # ==========================================
            if formula_type == 'indices':
                base = float(inputs['base'])
                m = float(inputs['pow1'])
                n = float(inputs['pow2'])
                op = inputs['indices_op']

                if op == 'multiply':
                    # Law 1: a^m * a^n = a^(m+n)
                    ans_pow = m + n
                    ans_val = base ** ans_pow
                    result = f"Law: {base}^{m} × {base}^{n} = {base}^({m}+{n}) = {base}^{ans_pow} = {ans_val}"
                elif op == 'divide':
                    # Law 2: a^m / a^n = a^(m-n)
                    ans_pow = m - n
                    ans_val = base ** ans_pow
                    result = f"Law: {base}^{m} ÷ {base}^{n} = {base}^({m}-{n}) = {base}^{ans_pow} = {ans_val}"
                elif op == 'power_of_power':
                    # Law 3: (a^m)^n = a^(m*n)
                    ans_pow = m * n
                    ans_val = base ** ans_pow
                    result = f"Law: ({base}^{m})^{n} = {base}^({m}×{n}) = {base}^{ans_pow} = {ans_val}"

            # ==========================================
            # 2. PYTHAGORAS THEOREM LOGIC
            # ==========================================
            elif formula_type == 'pythagoras':
                find = inputs['pythag_find']

                if find == 'hypotenuse':
                    a = float(inputs['side_a'])
                    b = float(inputs['side_b'])
                    # c = sqrt(a^2 + b^2)
                    c = math.sqrt(a**2 + b**2)
                    result = f"Formula: c = √({a}² + {b}²) = √({a**2} + {b**2}) = √({a**2 + b**2}) = {round(c, 4)}"
                
                elif find == 'leg_a':
                    b = float(inputs['side_b'])
                    c = float(inputs['side_c'])
                    if c <= b:
                        result = "Error: Hypotenuse (c) must be larger than side b!"
                    else:
                        # a = sqrt(c^2 - b^2)
                        a = math.sqrt(c**2 - b**2)
                        result = f"Formula: a = √({c}² - {b}²) = √({c**2} - {b**2}) = √({c**2 - b**2}) = {round(a, 4)}"

        except ValueError:
            result = "Error: Please enter valid numbers!"

    return render_template('index.html', formula_type=formula_type, inputs=inputs, result=result)

if __name__ == '__main__':
    app.run(debug=True)
