# Security review checklist

Customer/project:  
Prepared by:  
Date/version:  
Data classification: synthetic training / approved internal

- [ ] Authorized scope, synthetic data and named review owner.
- [ ] Identity validated; tenant context derived from trusted claims.
- [ ] Permissions checked before evidence enters model context.
- [ ] Document revocation and deletion propagate to indexes/caches.
- [ ] Prompt injection tested through both users and retrieved content.
- [ ] Tools allowlisted with validated arguments and least-privilege credentials.
- [ ] Consequential actions have explicit, bound, expiring approvals.
- [ ] Model output never executed as code or unescaped HTML.
- [ ] Input, time, retry, token, concurrency and spend limits defined.
- [ ] Dependencies/model provenance, licenses and artifact integrity reviewed.
- [ ] Logs minimized; retention, access and incident escalation documented.
- [ ] Failure, rollback, backup and recovery paths exercised.
- [ ] Privacy, fairness and applicable legal obligations reviewed by qualified owners.

For each item record evidence or a gap, owner and due date. Unchecked controls remain explicit residual risks. This checklist does not certify compliance.
