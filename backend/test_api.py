"""Quick test script for the image analysis API."""
import http.client
import json
import io
from PIL import Image

# Create a test image
img = Image.new('RGB', (200, 200), (100, 150, 200))
buf = io.BytesIO()
img.save(buf, format='JPEG')
img_bytes = buf.getvalue()

# Build multipart form data
boundary = '----TestBoundary123'
body = (
    f'--{boundary}\r\n'
    f'Content-Disposition: form-data; name="file"; filename="test.jpg"\r\n'
    f'Content-Type: image/jpeg\r\n\r\n'
).encode() + img_bytes + f'\r\n--{boundary}--\r\n'.encode()

conn = http.client.HTTPConnection('localhost', 8000)
conn.request('POST', '/api/analyze', body=body, headers={
    'Content-Type': f'multipart/form-data; boundary={boundary}'
})

resp = conn.getresponse()
data = json.loads(resp.read().decode())
conn.close()

print(f"Status: {resp.status}")
print(f"Classification: {data.get('classification')}")
print(f"Decision: {data.get('decision')}")
print(f"Label: {data.get('label')}")
print(f"Confidence: {data.get('conf')}%")
print(f"Severity: {data.get('severity')}")
print(f"Scores: {json.dumps(data.get('scores', {}), indent=2)}")
print(f"Has heatmap: {bool(data.get('heatmap_base64'))}")
print(f"Report lines: {len(data.get('report', []))}")
print(f"Badges: {[b['label'] for b in data.get('badges', [])]}")
print(f"Processing time: {data.get('processing_time')}s")
