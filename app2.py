import matplotlib.pyplot as plt
from flask import Flask, render_template
import io
import base64

app = Flask(__name__)

def generate_line_plot():
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Plot')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the plot image to base64
    plot_base64 = base64.b64encode(buffer.getvalue()).decode()

    return plot_base64

@app.route('/')
def index():
    plot_base64 = generate_line_plot()
    return render_template('index2.html', plot_base64=plot_base64)

if __name__ == '__main__':
    app.run(debug=True)
