import os
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)
from collections import Counter
from flask_login import (
    login_user,
    login_required,
    logout_user
)
from app import db
from app.models.attack import Attack
from app.models.admin import Admin
from app.utils.tracker import (
    get_device_info,
    get_ip_details
)

main = Blueprint("main", __name__)

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME") or "admin"
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD") or "secure123"


@main.route("/")
def home():
    return render_template("honeypot/login.html")


@main.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Handle standard proxy headers to get client IP in deployed environments
    ip_address = request.headers.get("X-Forwarded-For")
    if ip_address:
        ip_address = ip_address.split(",")[0].strip()
    else:
        ip_address = request.headers.get("X-Real-IP") or request.remote_addr

    user_agent_string = request.headers.get("User-Agent") or ""
    referrer = request.referrer or "Direct"

    device_data = get_device_info(user_agent_string)
    ip_data = get_ip_details(ip_address)

    attack = Attack(
        ip_address=ip_address,
        username=username,
        password=password,
        browser=device_data.get("browser", "Unknown"),
        operating_system=device_data.get("os", "Unknown"),
        device=device_data.get("device", "Unknown"),
        country=ip_data.get("country", "Unknown"),
        city=ip_data.get("city", "Unknown"),
        organization=ip_data.get("org", "Unknown"),
        referrer=referrer,
        user_agent=user_agent_string
    )

    db.session.add(attack)
    db.session.commit()

    return render_template("honeypot/failure.html")


@main.route("/dashboard-access", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            admin = Admin(1)
            login_user(admin)
            return redirect(url_for("main.dashboard"))
        else:
            error = "Invalid Credentials"

    return render_template(
        "dashboard/admin_login.html",
        error=error
    )


@main.route("/dashboard")
@login_required
def dashboard():
    attacks = Attack.query.order_by(
        Attack.timestamp.desc()
    ).all()

    total_attacks = len(attacks)
    usernames = [a.username for a in attacks if a.username]
    passwords = [a.password for a in attacks if a.password]
    countries = [a.country for a in attacks if a.country]

    top_usernames = Counter(usernames).most_common(5)
    top_passwords = Counter(passwords).most_common(5)
    top_countries = Counter(countries).most_common(5)

    return render_template(
        "dashboard/dashboard.html",
        total_attacks=total_attacks,
        top_usernames=top_usernames,
        top_passwords=top_passwords,
        top_countries=top_countries,
        logs=attacks[:20]
    )


@main.route("/api/attacks")
@login_required
def api_attacks():
    attacks = Attack.query.order_by(
        Attack.timestamp.desc()
    ).all()

    total_attacks = len(attacks)
    usernames = [a.username for a in attacks if a.username]
    passwords = [a.password for a in attacks if a.password]
    countries = [a.country for a in attacks if a.country]

    top_usernames = Counter(usernames).most_common(5)
    top_passwords = Counter(passwords).most_common(5)
    top_countries = Counter(countries).most_common(5)

    logs_data = []
    for a in attacks:
        logs_data.append({
            "id": a.id,
            "timestamp": a.timestamp.strftime("%Y-%m-%d %H:%M:%S") if a.timestamp else "",
            "ip_address": a.ip_address or "Unknown",
            "username": a.username or "",
            "password": a.password or "",
            "browser": a.browser or "Unknown",
            "operating_system": a.operating_system or "Unknown",
            "device": a.device or "Unknown",
            "country": a.country or "Unknown",
            "city": a.city or "Unknown",
            "organization": a.organization or "Unknown",
            "referrer": a.referrer or "Direct",
            "user_agent": a.user_agent or "Unknown"
        })

    return {
        "total_attacks": total_attacks,
        "top_usernames": top_usernames,
        "top_passwords": top_passwords,
        "top_countries": top_countries,
        "attacks": logs_data
    }


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.admin_login"))