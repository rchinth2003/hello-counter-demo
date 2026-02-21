Absolutely, Ravi — let’s build you a **clean, production‑ready PRD** that you can drop directly into **GHCP**, **GitHub MCP**, or **Azure DevOps MCP** and run as an **end‑to‑end demo**: PRD → Backlog → Repo → Code Gen → PRs → QA → CI/CD → Deployment.

This version is intentionally **simple, deterministic, and agent‑friendly**, so GHCP can execute it without ambiguity.  
It uses **generic authenticated MCP connections** (safe, recommended) and avoids any real secrets.

Below is the full PRD you can copy‑paste as a single `.md` file.

---

# **📄 Product Requirements Document (PRD)**  
## **HelloCounter API — Autonomous Delivery Demo**

### **1. Purpose**
Demonstrate an end‑to‑end autonomous workflow using:

- GitHub Copilot (GHCP) Coding Agent  
- GitHub MCP  
- Azure DevOps MCP  
- ADO Boards  
- GitHub repository  
- CI/CD pipeline to Azure App Service  

The system should go from **PRD → Backlog → Repo → Code → PR → Review → Merge → Deploy** with minimal human intervention.

---

## **2. Product Overview**
Build a simple **HelloCounter API** with two endpoints:

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/hello` | GET | Returns `"Hello, World!"` |
| `/counter` | POST | Increments and returns a persistent counter |

Persistence can be **in‑memory** for simplicity.

---

## **3. Functional Requirements**

### **3.1 API Requirements**
- Implement a minimal REST API in **Python (FastAPI)** or **Node.js (Express)**.
- `/hello` returns a static string.
- `/counter` increments a counter stored in memory and returns the updated value.
- Include basic input validation and error handling.

### **3.2 Non‑Functional Requirements**
- Code must include unit tests.
- API must run in a container.
- CI/CD pipeline must deploy to Azure App Service.
- All work must be traceable from PRD → Backlog → Code → PR.

---

## **4. Backlog Decomposition (for ADO Boards)**

### **Epic: HelloCounter API**
**User Story 1 — Create Project Structure**  
- Create repo  
- Add folder structure  
- Add README  
- Add initial scaffolding  

**User Story 2 — Implement `/hello` Endpoint**  
- Add route  
- Add unit tests  
- Add documentation  

**User Story 3 — Implement `/counter` Endpoint**  
- Add route  
- Add in‑memory counter  
- Add unit tests  
- Add documentation  

**User Story 4 — Containerization**  
- Add Dockerfile  
- Add local run instructions  

**User Story 5 — CI/CD Pipeline**  
- Add GitHub Actions workflow  
- Build → Test → Deploy to Azure App Service  

**User Story 6 — QA Validation**  
- Automated tests  
- API contract validation  
- Smoke test after deployment  

---

## **5. Repo Structure (GHCP should create this)**

```
/src
  /api
    main.py (or index.js)
  /tests
    test_hello.py
    test_counter.py
Dockerfile
README.md
.github/workflows/deploy.yml
```

---

## **6. Agent Instructions (for GHCP Coding Agent)**

### **6.1 Environment Assumptions**
- Use the authenticated **GitHub MCP** connection for repo operations.
- Use the authenticated **Azure DevOps MCP** connection for backlog creation.
- Use the authenticated **Azure MCP** connection for deployment.
- Do **not** request credentials; use what is already available.

### **6.2 Required Agent Behaviors**
1. **Read this PRD** and extract backlog items.  
2. **Create ADO work items** (Epic → Stories → Tasks).  
3. **Create a new GitHub repository** named:  
   `hello-counter-demo`  
4. **Generate code** for each backlog item in a feature branch.  
5. **Open a Pull Request** for each story.  
6. **Run unit tests** and ensure they pass.  
7. **Perform self‑review** (GHCP Reviewer Agent).  
8. **Request human approval** before merging.  
9. **Merge PRs** after approval.  
10. **Trigger CI/CD pipeline** to deploy to Azure App Service.  
11. **Run smoke tests** after deployment.  
12. **Post deployment summary** as a comment in the PR.

---

## **7. Branching & PR Conventions**
- Branch naming: `feature/<story-id>-<short-description>`
- PR naming: `Implement <Story Name>`
- PR description must include:
  - Linked ADO work item  
  - Summary of changes  
  - Test results  

---

## **8. CI/CD Requirements**
### **8.1 Build**
- Install dependencies  
- Run unit tests  
- Build container  

### **8.2 Deploy**
- Deploy container to Azure App Service  
- Run smoke tests  
- Post deployment status  

### **8.3 Example GitHub Actions Workflow**
(Agents should generate this)

```
name: Deploy API

on:
  push:
    branches: [ main ]

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Build container
        run: docker build -t hellocounter .
      - name: Deploy to Azure
        uses: azure/webapps-deploy@v3
        with:
          app-name: hello-counter-demo
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          package: .
```

---

## **9. Definition of Done**
A story is complete when:

- Code is generated  
- Unit tests pass  
- PR is reviewed by GHCP Reviewer Agent  
- Human approves  
- PR is merged  
- CI/CD deploys successfully  
- Smoke tests pass  
- Deployment summary is posted  

---

## **10. Demo Script (Optional)**
1. Drop this PRD into GHCP.  
2. Say: **“Generate backlog and begin execution.”**  
3. Watch ADO Boards populate.  
4. Watch repo creation.  
5. Watch branches, PRs, reviews, merges.  
6. Watch deployment logs.  
7. Hit the live endpoint:  
   - `/hello`  
   - `/counter`  

---

