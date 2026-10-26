# Project Summary

## Title
Automated API Security Testing Framework for Authentication and Object-Level Authorization

## Problem
APIs may expose private records when they authenticate users but do not verify each user's permission to access each requested object.

## Objective
Demonstrate a repeatable defensive test approach for authentication, object ownership enforcement, and selected HTTP security headers.

## Scope
A local Flask API with two fictional users and two sample documents. Automated tests validate expected allow/deny behavior.

## Methodology
1. Define access-control expectations.
2. Implement a server-side ownership check.
3. Write positive and negative automated tests.
4. Run the test suite.
5. Document results, limitations, and next steps.

## Test cases
- Health endpoint works.
- Owner can access their document.
- Different user cannot access the document.
- Missing authentication is rejected.
- Invalid token is rejected.
- Unknown document returns not found.
- Selected security headers are present.

## Expected result
All defined tests pass, showing that the demo's implemented access-control rules behave as expected.

## Resume bullet (use only after running and verifying)
Built a Python/Flask API security demo with automated pytest checks for authentication, object-level authorization (BOLA-style access-control cases), and HTTP security headers; documented test coverage and design limitations.

## Limitations
This is an educational proof of concept, not a production security product or proof of overall security.
