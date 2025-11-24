# AI Speech Evaluation System - Quick Start Guide

## 🚀 Quick Setup (Windows)

### Backend Setup

1. **Open Command Prompt or PowerShell**
2. **Navigate to backend directory:**
   ```bash
   cd backend
   ```
3. **Run setup script:**
   ```bash
   setup.bat
   ```
4. **Start the server:**
   ```bash
   start.bat
   ```

The backend will be available at: http://localhost:8000

### Frontend Setup

1. **Open a NEW Command Prompt or PowerShell**
2. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```
3. **Run setup script:**
   ```bash
   setup.bat
   ```
4. **Start the dev server:**
   ```bash
   start.bat
   ```

The frontend will be available at: http://localhost:5173

## 📝 Manual Setup

If the scripts don't work, follow the manual setup instructions in the main README.md

## 🧪 Testing

After starting the backend, you can test it:

```bash
cd backend
venv\Scripts\activate
python test_api.py
```

## 🎯 Usage

1. Open http://localhost:5173 in your browser
2. Enter a self-introduction transcript
3. Click "Evaluate Speech"
4. Review your detailed results!

## 📚 Example Transcript

```
Hello everyone! My name is Sarah Johnson. I am 15 years old and I study at 
Lincoln High School in grade 10. I live with my parents and my younger brother. 
I love reading books, especially mystery novels, and I enjoy playing basketball 
on weekends. I'm also interested in learning new languages. Thank you for 
listening to my introduction!
```

## ❓ Troubleshooting

### Backend Issues

- **Port 8000 already in use**: Change the port in `start.bat` or kill the process using port 8000
- **Module not found**: Make sure you activated the virtual environment and installed dependencies
- **NLTK data missing**: Run `python -c "import nltk; nltk.download('punkt')"`

### Frontend Issues

- **Port 5173 already in use**: Vite will automatically use the next available port
- **Cannot connect to backend**: Check that backend is running and update `.env` with correct URL
- **npm install fails**: Try deleting `node_modules` and `package-lock.json`, then run `npm install` again

## 📞 Need Help?

Check the main README.md for detailed documentation and troubleshooting.
