AWS SQS worker application.
Checks SQS queue for messages, and if present sends JSON payload to Cisco's Network Services Orchestrator via a REST call.

Run from a virtualenv as follows:

    cd to the directory where requirements.txt is located.
    activate your virtualenv.
    run: pip install -r requirements.txt in your shell.
