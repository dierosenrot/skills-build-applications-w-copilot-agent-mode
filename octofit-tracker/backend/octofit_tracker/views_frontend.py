import os
from django.http import HttpResponse

# Serve React build index.html

def serve_react(request):
    build_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend', 'build')
    index_path = os.path.join(build_dir, 'index.html')
    try:
        with open(index_path, 'r') as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        return HttpResponse("React build not found. Please run 'npm run build' in the frontend directory.", status=501)
