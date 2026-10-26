# API Security Testing Framework (Defensive Demo)

A small, local-only project demonstrating API authentication, object-level authorization checks, security headers, and repeatable automated tests.

## Why this project?
Broken Object Level Authorization (BOLA) can occur when an API checks who a user is but fails to check whether that user may access a specific record. This demo uses fictional users and documents to demonstrate the expected secure behavior.

## Features
- Bearer-token authentication for a controlled demo
- Per-document owner authorization
- Safe responses for unauthorized access
- Baseline security headers
- Automated pytest test suite
- Tests for allowed access, denied cross-user access, missing/invalid credentials, missing records, and headers

## Requirements
Python 3.10+ recommended.

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests
```bash
pytest -v
```

## Run the local demo
```bash
python app.py
```
The app listens only on `127.0.0.1:5000`.

In another terminal, try:
```bash
# Alice can access her own document
curl -i -H "Authorization: Bearer demo-token-alice" http://127.0.0.1:5000/documents/doc-101

# Bob must not access Alice's document (expected: 404)
curl -i -H "Authorization: Bearer demo-token-bob" http://127.0.0.1:5000/documents/doc-101

# Missing token (expected: 401)
curl -i http://127.0.0.1:5000/documents/doc-101
```

Demo identities:
- Alice token: `demo-token-alice`, owns `doc-101`
- Bob token: `demo-token-bob`, owns `doc-202`

These are intentionally fake, public demo values—not secrets.

## Suggested demo script (2–3 minutes)
1. Explain the BOLA risk: changing an object ID must not grant access.
2. Run `pytest -v` and show the passing test cases.
3. Show Alice's authorized request.
4. Show Bob's denied request to Alice's document.
5. Explain the control: the server checks ownership on every object access.
6. State limitations and production improvements.

## Security design notes
- Authorization is enforced server-side for every document request.
- The demo returns 404 for cross-user access to reduce record-existence disclosure.
- Security headers are included as examples; header needs depend on the application and deployment.
- The app is bound to loopback (`127.0.0.1`) and uses fictional in-memory data.

## Limitations (be transparent)
- Static demo tokens; no real login, token expiry, rotation, or secure session management.
- In-memory records; no database.
- No rate limiting, audit trail, schema validation, or production deployment.
- The sample demonstrates one authorization rule, not a comprehensive API audit.
- Tests cover defined cases only; passing tests do not prove an application is secure.

## Next improvements
1. Replace demo authentication with a vetted identity provider.
2. Add role-based permissions and negative tests for each endpoint.
3. Add structured audit logging and rate limiting.
4. Add an OpenAPI spec and schema validation.
5. Integrate checks into a CI workflow.

## Responsible testing
Use this project locally. Test only systems you own or have explicit authorization to assess.
