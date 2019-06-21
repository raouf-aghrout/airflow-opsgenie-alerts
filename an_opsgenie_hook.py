from airflow.contrib.hooks.opsgenie_alert_hook import OpsgenieAlertHook

def opsgenie_hook(context):
    dag = context.get('task_instance').dag_id,
    task = context.get('task_instance').task_id,
    ts = context.get('ts'),
    log_url = context.get('task_instance').log_url

    date_time = dateutil.parser.parse(ts[0])

    message = "Airflow DAG {}, failed to run {}, scheduled at {}.".format(dag[0], task[0], date_time.strftime('%Y-%m-%d %H:%M'))

    json = {
        "message": message,
        "description": message,
        "responders": [
            {
                "id": "SOME-TEAM-ID-HERE",
                "type": "team"
            }
        ],
        "visibleTo": [
            {
                "id": "SOME-TEAM-ID-HERE",
                "type": "team"
            }
        ],
        "tags": [
            "Data Engineering",
            "Airflow"
        ],
        "details": {
            "Logs": log_url.replace("localhost", "YOUR-AIRFLOW-DNS")
        },
        "priority": "P3"
    }
    
    hook = OpsgenieAlertHook('opsgenie_default')
    hook.execute(json)
