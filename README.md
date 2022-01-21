# DevOps Demo

This is a simple web app based on Python. In this demo app, Flask is being used to respond to the requested paths.

In this demo app, I am combining several tools to deploy the application on Google Cloud Platform.

- Git Action Workflow (on push, create docker images, push to registry, build kustomization)
- Google Kubernetes Engine (GKE)
- Google Ingress
- Google Managed Certificates (for Enabling TLS)

## Steps to deploy:

1. Create a Cluster on GKE and configure your `kubectl`
2. Enable GCR (Google Container Registry)
3. Add secrets to GitHub (The required secrets are mentioned in workflow code.)
4. Create a static IP on google
5. Configure your DNS and map your domain to the IP you created on google
6. Run the github workflow. It creates the `manifest.yaml`
7. Deploy the manifest.yaml to GKE (`kubectl apply -f /path/to/manifest.yaml`)
