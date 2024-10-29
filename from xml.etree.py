from xml.etree.ElementTree import Element, SubElement, ElementTree
import xml.dom.minidom

# Project details
projects = [
    {
        "title": "Real-Time Collaborative Document Editor",
        "description": "Real-time document editor with live collaboration, similar to Google Docs",
        "core_technologies": "WebSocket/Socket.IO, Django Channels/FastAPI, Redis, PostgreSQL, React",
        "key_challenges": "Managing concurrency, real-time updates, data consistency",
        "deployment_architecture": "Kubernetes, load-balanced containers on AWS/GCP, Dockerized"
    },
    {
        "title": "AI-Powered E-Learning Platform",
        "description": "Personalized learning platform with AI-based content suggestions",
        "core_technologies": "Django/FastAPI, TensorFlow/PyTorch, PostgreSQL, React",
        "key_challenges": "Optimizing AI models, low latency for content, large-scale analytics",
        "deployment_architecture": "Cloud model hosting, autoscaling, CDN for content delivery"
    },
    {
        "title": "Social Media Platform with Sentiment Analysis",
        "description": "Social media app with sentiment analysis on posts and recommendation engine",
        "core_technologies": "Django/Flask, ElasticSearch, Redis, BERT-based NLP models",
        "key_challenges": "High read/write speed, NLP model optimization, handling high traffic",
        "deployment_architecture": "Managed database (RDS), scalable microservices, load-balanced setup"
    },
    {
        "title": "Video Streaming Platform with Recommendations",
        "description": "Video streaming app with personalized content recommendations",
        "core_technologies": "Flask/Django, AWS S3, CDN, AI recommendation algorithms",
        "key_challenges": "Video compression/storage, efficient streaming, recommendation engine",
        "deployment_architecture": "Video CDN, autoscaling servers, content caching"
    },
    {
        "title": "Health Monitoring & Consultation App",
        "description": "Tracks health data, provides insights, and connects users with doctors in real-time",
        "core_technologies": "Django/FastAPI, ML models, PostgreSQL, WebSocket",
        "key_challenges": "Real-time data processing, security for health data, high data volume",
        "deployment_architecture": "Serverless on cloud, HIPAA-compliant storage, secure data handling"
    },
    {
        "title": "Crypto Trading Bot with Predictive Analytics",
        "description": "Analyzes market data to make trading decisions based on predictions",
        "core_technologies": "FastAPI, NumPy/Pandas, ML models, Kafka",
        "key_challenges": "Low-latency processing, high-frequency data handling, API security",
        "deployment_architecture": "Kubernetes, serverless functions, cloud-based monitoring"
    },
    {
        "title": "Real-Time Inventory & Order Management System",
        "description": "Tracks inventory and orders in real time for e-commerce",
        "core_technologies": "Django/FastAPI, Redis, PostgreSQL, Celery, React",
        "key_challenges": "Real-time updates, stock consistency, high-frequency database queries",
        "deployment_architecture": "Cloud SQL, Kubernetes for scalability, distributed caching"
    },
    {
        "title": "AI-Powered Customer Support Chatbot",
        "description": "Customer support chatbot for handling high volumes of simultaneous queries",
        "core_technologies": "FastAPI, Transformers for NLP, PostgreSQL, Redis",
        "key_challenges": "Conversational accuracy, NLP optimization, conversation state management",
        "deployment_architecture": "Cloud GPU for NLP models, serverless API, autoscaling database"
    }
]

# Create XML root
root = Element('Projects')

# Populate XML with project details
for proj in projects:
    project_el = SubElement(root, "Project")
    for key, value in proj.items():
        el = SubElement(project_el, key)
        el.text = value

# Convert the ElementTree to a pretty-printed XML string
xml_str = xml.dom.minidom.parseString(ElementTree(root).write(encoding='unicode')).toprettyxml(indent="   ")

# Write to XML file
file_name = "advanced_python_projects.xml"
with open(file_name, "w") as f:
    f.write(xml_str)

print(f"XML file '{file_name}' created successfully.")
