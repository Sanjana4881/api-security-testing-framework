from flask import Flask, jsonify, request

app = Flask(__name__)

# Demo-only identities. Never hard-code real credentials or use this auth pattern in production.
TOKENS = {"demo-token-alice": "alice", "demo-token-bob": "bob"}
DOCUMENTS = {
    "doc-101": {"owner": "alice", "title": "Alice sample resume"},
    "doc-202": {"owner": "bob", "title": "Bob sample resume"},
}

def current_user():
    header = request.headers.get("Authorization", "")
    if not header.startswith("Bearer "):
        return None
    return TOKENS.get(header.removeprefix("Bearer ").strip())

@app.after_request
def security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Cache-Control"] = "no-store"
    response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'"
    return response

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/documents/<document_id>")
def get_document(document_id):
    user = current_user()
    if not user:
        return jsonify(error="Authentication required"), 401

    document = DOCUMENTS.get(document_id)
    if not document:
        return jsonify(error="Not found"), 404

    # Object-level authorization: only the document owner may read it.
    if document["owner"] != user:
        # 404 avoids disclosing whether another user's document exists.
        return jsonify(error="Not found"), 404

    return jsonify(id=document_id, title=document["title"])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
