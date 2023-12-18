from flask import Flask, render_template, send_file
from your_line_plot_script import generate_line_plot

app = Flask(__name__)

@app.route('/')
def index():
    plot = generate_line_plot()
    plot_filename = 'line_plot.png'
    plot.savefig(plot_filename)
    return render_template('index.html', plot_filename=plot_filename)

if __name__ == '__main__':
    app.run(debug=True)
