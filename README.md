# CFD Predictor Deployment Demo

# Python API Deployment with Docker, Kubernetes, Helm, and Argo CD

This repository demonstrates an end-to-end deployment workflow for a simple Python-based prediction API, progressing from local development to containerisation, Kubernetes orchestration, Helm templating, and GitOps-style deployment with Argo CD.

The project was built as a hands-on engineering exercise to demonstrate practical familiarity with:
- Python API development
- Docker-based containerisation
- Kubernetes Deployment and Service resources
- Helm chart templating, upgrade, and rollback
- Argo CD application management and GitOps synchronisation
- Git/GitHub-based version-controlled deployment workflows

## Project Overview

The application is a lightweight Flask-based API that exposes:
- `/` — a basic service health/status endpoint
- `/predict` — a simple prediction-style JSON response endpoint

Although the API itself is intentionally minimal, the main purpose of the project is to demonstrate how a locally developed Python service can be transformed into a deployable, reproducible, and version-controlled cloud-native application.

## Tech Stack

- Python
- Flask
- Docker
- Kubernetes
- Helm
- Argo CD
- Git / GitHub

## Repository Structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── chart/
│   └── cfd-predictor/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
└── README.md

Application Endpoints

The Flask API exposes two basic routes:

/
Returns a simple service status message.
/predict
Returns a lightweight JSON response representing a placeholder prediction result.

Example response:

{
  "velocity": 3.14,
  "pressure_drop": 12.5,
  "status": "success"
}
What This Project Demonstrates
1. Local Python API Development

A simple Flask-based API was first created and validated locally.

2. Docker Containerisation

The service was packaged into a Docker image to support portable and reproducible execution.

3. Kubernetes Deployment

The containerised application was deployed to Kubernetes using Deployment and Service manifests, enabling replicated execution and service exposure.

4. Helm Templating

Static Kubernetes manifests were converted into a reusable Helm chart, allowing key deployment settings such as replica count and image configuration to be parameterised.

5. Helm Release Lifecycle

The Helm deployment workflow was validated through:

install
template rendering
upgrade
history
rollback
6. Argo CD GitOps Workflow

The Helm chart was integrated with Argo CD and GitHub, allowing deployment state to be synchronised from version-controlled configuration.

Key Deployment Workflow
Local Run

Run the Flask service locally:

python app.py
Docker Build

Build the Docker image:

docker build -t cfd-predictor:v1 .

Run the container locally:

docker run -p 5000:5000 cfd-predictor:v1
Kubernetes Deployment with Raw YAML

Deploy using Kubernetes manifests:

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Check resources:

kubectl get deployments
kubectl get pods
kubectl get services

Access via port-forward:

kubectl port-forward service/cfd-predictor-service 8080:80

Then open:

http://127.0.0.1:8080/
http://127.0.0.1:8080/predict
Helm Deployment

Move into the chart directory:

cd chart/cfd-predictor

Render the manifests locally:

helm template my-cfd .

Install the Helm release:

helm install my-cfd .

Check deployment status:

kubectl get deployments
kubectl get pods
kubectl get services

Access via port-forward:

kubectl port-forward service/my-cfd-service 8081:80

Then open:

http://127.0.0.1:8081/
http://127.0.0.1:8081/predict
Helm Upgrade Example

Increase the replica count from 2 to 3:

helm upgrade my-cfd . --set replicaCount=3
kubectl get pods
Helm Rollback Example

Check release history:

helm history my-cfd

Rollback to revision 1:

helm rollback my-cfd 1
kubectl get pods
Argo CD

Argo CD was installed into the Kubernetes cluster and configured to track the Helm chart from this GitHub repository.

The workflow demonstrated:

GitHub as the source of truth
Argo CD application creation from repository
manual synchronisation into Kubernetes
GitOps-style deployment management

A typical local access workflow for the Argo CD UI is:

kubectl port-forward svc/argocd-server -n argocd 8090:443

Then open:

https://localhost:8090

Potential Extensions

Possible future improvements include:

replacing the placeholder prediction logic with a real ML or simulation model
adding structured request validation and error handling
introducing a frontend UI
adding CI/CD automation with GitHub Actions
exposing the service through Ingress or cloud deployment rather than local port-forwarding
