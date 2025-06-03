from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Error: At least one character type must be selected"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    error = ''
    
    if request.method == 'POST':
        try:
            length = int(request.form.get('length', 12))
            use_uppercase = 'uppercase' in request.form
            use_lowercase = 'lowercase' in request.form
            use_numbers = 'numbers' in request.form
            use_special = 'special' in request.form
            
            if length < 8:
                error = "Password length must be at least 8 characters"
            elif not any([use_uppercase, use_lowercase, use_numbers, use_special]):
                error = "At least one character type must be selected"
            else:
                password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        except ValueError:
            error = "Please enter a valid number for password length"
    
    return render_template('index.html', password=password, error=error)

if __name__ == '__main__':
    app.run(debug=True)