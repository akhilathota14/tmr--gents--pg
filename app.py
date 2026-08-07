from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TMR Gents PG</title>
        <style>
    body {
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 20px;
        background: #f8f8f8;
        color: #222;
    }

    .container {
        max-width: 900px;
        margin: auto;
    }

    h1 {
        text-align: center;
        color: #0b1f3a;
        font-size: 38px;
        font-weight: bold;
    }

    h2 {
        color: #c49a2c;
        margin-top: 35px;
        border-bottom: 2px solid #c49a2c;
        padding-bottom: 8px;
    }

    .card {
        background: white;
        padding: 20px;
        margin: 18px 0;
        border-radius: 15px;
        border-left: 5px solid #c49a2c;
        box-shadow: 0 5px 15px rgba(0,0,0,0.12);
    }

    .price {
        font-size: 22px;
        font-weight: bold;
        color: #0b1f3a;
    }

    .menu-table {
        width: 100%;
        border-collapse: collapse;
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0,0,0,0.12);
    }

    .menu-table th {
        background: #0b1f3a;
        color: white;
        padding: 14px;
    }

    .menu-table td {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: left;
    }

    .map-button {
        display: inline-block;
        padding: 13px 22px;
        background: #c49a2c;
        color: white;
        text-decoration: none;
        border-radius: 25px;
        font-weight: bold;
    }

    .map-button:hover {
        background: #a47d1d;
    }

    @media(max-width:600px){
        body {
            padding: 10px;
        }

        h1 {
            font-size: 30px;
        }

        .menu-table {
            font-size: 13px;
        }
    }
</style>
        </head>

    <body>
    <div class="container">

        <h1>🏠 TMR Gents PG</h1>
        <p style="text-align:center;">
            Your comfortable home away from home.
        </p>

        <h2>🛏️ Rooms & Prices</h2>

        <div class="card">
            <p>1 Sharing - AC</p>
            <p class="price">₹22,000 / month</p>
        </div>

        <div class="card">
            <p>2 Sharing - AC</p>
            <p class="price">₹11,000 / month</p>
        </div>

        <div class="card">
            <p>3 Sharing - AC</p>
            <p class="price">₹8,500 / month</p>
        </div>

        <div class="card">
            <p>4 Sharing - AC</p>
            <p class="price">₹7,500 / month</p>
        </div>

        <div class="card">
            <p>5 Sharing - AC</p>
            <p class="price">₹7,000 / month</p>
        </div>

        <div class="card">
            <p>5 Sharing - Non-AC</p>
            <p class="price">₹6,500 / month</p>
        </div>

        <h2>🍛 Weekly Food Menu</h2>

        <table class="menu-table">
            <tr>
                <th>Day</th>
                <th>Breakfast</th>
                <th>Lunch</th>
                <th>Dinner</th>
            </tr>

            <tr>
                <td><b>Monday</b></td>
                <td>Idli with chutney</td>
                <td>Vegetable Rice & Aloo Curry</td>
                <td>
                    Veg: Rice, Chutney, Rasam, Papad<br>
                    Non-Veg: Boiled Eggs, Rice, Chutney, Rasam
                </td>
            </tr>

            <tr>
                <td><b>Tuesday</b></td>
                <td>Dosa & Chutney</td>
                <td>Rice, Any Fry, Dal</td>
                <td>Chapati & Curry</td>
            </tr>

            <tr>
                <td><b>Wednesday</b></td>
                <td>Pongal & Chutney</td>
                <td>Tomato Rice & Curry</td>
                <td>
                    Veg: Rice, Paneer Curry, Rasam<br>
                    Non-Veg: Rice, Chicken Curry, Rasam
                </td>
            </tr>

            <tr>
                <td><b>Thursday</b></td>
                <td>Idli with chutney</td>
                <td>Sambar, Fry, Rice</td>
                <td>Dosa & Two type Chutney, Sweet</td>
            </tr>

            <tr>
                <td><b>Friday</b></td>
                <td>Bonda with chutney</td>
                <td>Lemon Rice & Aloo Fry</td>
                <td>
                    Veg Fried Rice & Egg Fried Rice (OR)
                    Omelette, Rice, Dal, Chutney, Papad
                </td>
            </tr>

            <tr>
                <td><b>Saturday</b></td>
                <td>Ugani (OR) Uttapam</td>
                <td>Sambar, Oil Fry, Chutney, Rice</td>
                <td>Chapati & Curry</td>
            </tr>

            <tr>
                <td><b>Sunday</b></td>
                <td>Upma & Chutney</td>
                <td>Pulav, Chicken Curry, Paneer Curry, Raita</td>
                <td>Sunday Special</td>
            </tr>
        </table>

        <h2>📍 Location</h2>

        <div class="card">
            <p>TMR Gents PG, Sholinganallur, Chennai, Tamil Nadu</p>

            <a class="map-button"
               href="https://maps.app.goo.gl/Wh1NFb5sM4ozz4vM6"
               target="_blank">
                📍 Open Location in Google Maps
            </a>
        </div>

    </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
