# ⚡ Quick Reference Guide

## 📋 Pre-Flight Checklist

Before starting, verify you have:
```
✓ Python 3.10+     (check: python --version)
✓ Node.js 18+      (check: node --version)
✓ FFmpeg           (check: ffmpeg -version)
✓ Git              (optional, check: git --version)
```

## 🚀 One-Command Setup (Windows)

```bat
start.bat
```

This will automatically:
1. Setup backend virtual environment
2. Install all Python packages
3. Setup frontend npm packages
4. Start both servers

## 🚀 One-Command Setup (macOS/Linux)

```bash
chmod +x start.sh
./start.sh
```

## 🔧 Manual Setup (3 Steps)

### Step 1: Backend Setup
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Frontend Setup
```bash
cd frontend
npm install
# or: yarn install
```

### Step 3: Start Servers (2 terminals)

**Terminal A - Backend:**
```bash
cd backend
source venv/bin/activate  # (Windows: venv\Scripts\activate)
uvicorn main:app --reload --port 8000
```

**Terminal B - Frontend:**
```bash
cd frontend
npm run dev
```

## 🌐 URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |
| Health Check | http://localhost:8000/api/health |

## 📝 Testing Quick Commands

```bash
# Health check
curl http://localhost:8000/api/health

# Upload video (replace path)
curl -X POST http://localhost:8000/api/upload \
  -F "file=@C:\path\to\video.mp4"

# Check status (replace job_id)
curl http://localhost:8000/api/status/your-job-id-here
```

## 🔧 Common Issues & Quick Fixes

| Issue | Fix |
|-------|-----|
| FFmpeg not found | `winget install ffmpeg` (Windows) / `brew install ffmpeg` (Mac) |
| Module not found | `pip install -r requirements.txt` |
| Port 8000 already in use | `lsof -ti:8000` then `kill -9 <PID>` |
| Port 3000 already in use | Change port: `npm run dev -- -p 3001` |
| Model won't download | Check internet, delete `~/.cache/deepfake_detector/` |
| CORS error | Check backend CORS settings in `main.py` |

## 📊 Project Structure
```
.
├── backend/           ← Python/FastAPI backend
├── frontend/          ← React/Next.js frontend
├── README.md          ← Full documentation
├── SETUP.md           ← Detailed setup guide
└── IMPLEMENTATION.md  ← Technical details
```

## 🎨 Customization Quick Links

| What | Where |
|------|-------|
| Colors | `frontend/tailwind.config.js` |
| API URL | `frontend/.env.local` |
| Backend Port | `backend/main.py` (line ~60) |
| Frame Rate | `backend/jobs.py` (fps parameter) |
| Model | `backend/pipeline/deepfake_model.py` |

## 📱 Using the Application

1. **Upload**: Drag & drop or click to select video
2. **Wait**: Real-time progress updates appear
3. **Preview**: Video plays automatically
4. **Review**: Results show confidence scores
5. **Export**: Optional print/export results
6. **Reset**: Analyze another video

## 🎯 Key Features

✨ **Instagram Reels Style** - Modern drag-and-drop UI
⚡ **Real-time Processing** - Live progress updates
🤖 **Advanced AI** - EfficientNet-B4 deepfake detection
📊 **Detailed Results** - Three confidence scores
🎨 **Beautiful UI** - Dark theme with animations
📱 **Responsive** - Works on desktop/tablet

## 🔗 Endpoints Summary

```
GET  /api/health                    Health check
POST /api/upload                    Upload video
GET  /api/status/{job_id}          Check job status
```

## 💾 Environment Variables

**Frontend (.env.local):**
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## 📖 Documentation Files

- `README.md` - Main project overview
- `SETUP.md` - Complete step-by-step guide
- `IMPLEMENTATION.md` - Technical implementation details
- `frontend/README.md` - Frontend-specific docs
- This file - Quick reference

## ⚠️ Important Notes

- **First Run**: Model weights (~350MB) download automatically
- **Processing Time**: 20 seconds to 5+ minutes per video
- **GPU Optional**: Runs on CPU, ~10-20x faster with GPU
- **Authentication**: Not implemented (add for production)
- **Data Persistence**: No (jobs cleared on restart)

## 🆘 Get Help

1. **Setup Issues?** → Read `SETUP.md`
2. **Technical Details?** → Read `IMPLEMENTATION.md`
3. **API Help?** → Visit http://localhost:8000/docs
4. **Code Questions?** → Code is well-commented

## 🚀 Next Steps

```
1. Run start.bat or start.sh
2. Wait for both servers to start
3. Open http://localhost:3000
4. Upload a test video
5. Review results
6. Customize colors if desired
7. Deploy to production when ready
```

---

**Version**: 1.0.0
**Status**: ✅ Ready to Use
**Last Updated**: March 2026
