from flask import redirect, render_template, request, url_for

from application import app, db
from application.candidates.models import Candidate
from application.candidates.forms import CandidateForm

@app.route("/candidates/", methods=["GET"])
@app.route("/candidates", methods=["GET"])
def candidates_index():
    return render_template("candidates/list.html", candidates = Candidate.query.all())

@app.route("/candidates/new/")
def candidates_form():
    return render_template("candidates/new.html", form = CandidateForm())

@app.route("/candidates/<candidate_id>/", methods=["POST"])
def candidates_set_selected(candidate_id):
    candidate = Candidate.query.get(candidate_id)
    candidate.selected = True
    db.session().commit()

    return redirect(url_for("candidates_index"))

@app.route("/candidates/", methods=["POST"])
def candidates_create():
    candidate = Candidate(request.form.get("name"))
    candidate.url = request.form.get("url")
    db.session().add(candidate)
    db.session().commit()

    return redirect(url_for("candidates_index"))