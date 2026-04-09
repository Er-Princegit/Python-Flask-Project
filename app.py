from flask import Flask, render_template, request
from planner import generate_plan
from model import predict_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    plan = None
    prediction = None

    if request.method == "POST":
        # Get all inputs
        branch = request.form.get("branch")
        semester = request.form.get("semester")
        subject = request.form.get("subject")
        hours = request.form.get("hours")
        days = request.form.get("days")

        # Safety check (VERY IMPORTANT)
        if hours and days:
            hours = int(hours)
            days = int(days)

            # Generate plan
            difficulty = request.form["difficulty"]
            goal = request.form["goal"]

            plan = generate_plan(subject, hours, days, difficulty, goal)

            # Predict score
            prediction = predict_score(hours)

    return render_template("index.html", plan=plan, prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)