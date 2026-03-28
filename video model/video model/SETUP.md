# 🚀 Complete Setup Guide - Deepfake Detection Application

## Prerequisites Checklist

Before you start, ensure you have the following installed:

- [ ] **Python 3.10+** - Check with: `python --version`
- [ ] **Node.js 18+** - Check with: `node --version`
- [ ] **FFmpeg** - Check with: `ffmpeg -version`
- [ ] **Git** (optional) - For version control

### Installing FFmpeg

**Windows:**
```powershell
winget install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

---

## Step 1: Set Up Backend

### 1.1 Navigate to Backend Directory
```bash
cd backend
```

### 1.2 Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 1.3 Install Python Dependencies
```bash
pip install -r requirements.txt
```

**First-time installation note:** The model weights (~350MB) will download automatically on first run from HuggingFace.

### 1.4 Verify Setup
```bash
python check_dependencies.py
python setup.py
python test.py
```

---

## Step 2: Set Up Frontend

### 2.1 Navigate to Frontend Directory
```bash
cd frontend
```

### 2.2 Install Node Dependencies
```bash
npm install
```

Or with Yarn:
```bash
yarn install
```

### 2.3 Create Environment File
Create `.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

Or copy from example:
```bash
cp .env.example .env.local
```

---

## Step 3: Run the Application

### Quick Start (Automated)

**Windows:**
```bash
start.bat
```

**macOS/Linux:**
```bash
chmod +x start.sh
./start.sh
```

### Manual Start (Separate Terminals)

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or: venv\Scripts\activate (Windows)
uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Access the Application

Once both servers are running:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs (interactive Swagger UI)

---

## Step 4: Test the Application

### Health Check
```bash
curl http://localhost:8000/api/health
```

Expected response:
```json
{"status": "ok", "version": "1.0.0"}
```

### Upload a Test Video (using curl)

```bash
curl -X POST http://localhost:8000/api/upload \
  -F "file=@/path/to/test_video.mp4"
```

Expected response:
```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "video_url": "/uploads/550e8400.mp4"
}
```

### Check Job Status
```bash
curl http://localhost:8000/api/status/550e8400-e29b-41d4-a716-446655440000
```

---

## Troubleshooting

### Issue: "FFmpeg not found"
**Solution:**
- Ensure FFmpeg is installed and added to PATH
- Test: `ffmpeg -version`
- Windows: Use `winget install ffmpeg`

### Issue: Model Download Fails
**Solution:**
- Check internet connection
- Model cache location: `~/.cache/deepfake_detector/`
- Delete cache folder to retry download (will re-download on next run)
- Models are ~350MB

### Issue: "ModuleNotFoundError: No module named 'torch'"
**Solution:**
```bash
pip install -r requirements.txt
```

If PyTorch installation fails, try:
```bash
# CPU version (smaller)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# GPU version (CUDA 11.8)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Issue: "Frontend can't connect to backend"
**Solution:**
- Verify backend is running on port 8000
- Check `.env.local` has `NEXT_PUBLIC_API_URL=http://localhost:8000/api`
- Check CORS settings in `backend/main.py` include `http://localhost:3000`

### Issue: "CUDA out of memory" (if using GPU)
**Solution:**
- The app will automatically fall back to CPU
- Or disable GPU in code (forces CPU mode)

---

## Development Tips

### Hot Reload
- **Frontend**: Changes to `.tsx` files auto-reload
- **Backend**: Changes to `.py` files auto-reload with `--reload` flag

### API Documentation
Visit http://localhost:8000/docs to see interactive API documentation with Swagger UI.

### Database-like UI State
Job data is stored in memory during runtime. Restarting the backend clears all jobs.

### Logging
- Backend logs appear in terminal running `uvicorn`
- Frontend logs appear in browser console and terminal

---

## Building for Production

### Frontend Build
```bash
cd frontend
npm run build
npm start
```

### Backend Server
For production, use a production ASGI server:
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

Or use Docker (see deployment guide).

---

## Performance Notes

### Processing Times (approximate)
- **Short video (15 seconds)**: 20-30 seconds total
- **Medium video (1 minute)**: 45-60 seconds
- **Long video (5 minutes)**: 3-5 minutes

Times vary based on:
- CPU/GPU availability
- Video resolution
- Number of faces detected
- System load

### Optimization Tips
- Shorter videos process faster
- Lower resolution videos = faster processing
- GPU acceleration (CUDA) is ~10-20x faster than CPU

---

## Directory Structure
```
project/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── jobs.py              # Background processing
│   ├── requirements.txt
│   ├── pipeline/
│   │   ├── frame_extractor.py
│   │   ├── face_detector.py
│   │   ├── deepfake_model.py
│   │   └── aggregator.py
│   ├── uploads/             # Temp video storage
│   ├── frames/              # Temp frame storage
│   └── venv/                # Python virtual env
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx         # Main page
│   │   ├── layout.tsx       # Root layout
│   │   ├── globals.css      # Styles
│   │   ├── components/      # React components
│   │   └── utils/           # API client
│   ├── package.json
│   ├── next.config.js
│   └── .env.local           # Environment vars (create this)
│
├── README.md
├── SETUP.md (this file)
├── start.bat (Windows)
└── start.sh (macOS/Linux)
```

---

## Next Steps

1. ✅ Complete this setup
2. 📺 Upload a test video via the web interface
3. 🧪 Review results and accuracy
4. 🎨 Customize colors/branding in `frontend/tailwind.config.js`
5. 📚 Read the main `README.md` for detailed documentation
6. 🚀 Deploy to production (see deployment guide)

---

## Support & Documentation

- **API Docs**: http://localhost:8000/docs
- **Main README**: See `../README.md`
- **Frontend README**: See `../frontend/README.md`
- **Backend README**: See `../backend/README.md`

---

## ⚠️ Important Disclaimer

This tool is for educational and research purposes. Results should not be the sole basis for critical decisions. Always verify with additional sources and domain experts before taking action based on detection results.

---

**Last Updated**: March 2026
**Version**: 1.0.0
