from datetime import datetime


def calculate_case_age(created_at):

    created = datetime.strptime(
        created_at,
        "%Y-%m-%d %H:%M:%S"
    )

    today = datetime.now()

    return (
        today - created
    ).days


def get_sla_status(
    age,
    sla_days
):

    if age > sla_days:
        return "🔴 Breached"

    return "🟢 Within SLA"