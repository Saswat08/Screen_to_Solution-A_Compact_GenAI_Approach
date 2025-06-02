# Screen_to_Solution-A_Compact_GenAI_Approach

# Genius Calculator: From Screen to Solution 🧠📷➕
An AI-powered web-based educational tool that interprets handwritten math and physics problems and generates step-by-step solutions using computer vision, symbolic computation, and generative AI.

---

## 🚀 Project Overview

**Genius Calculator** enables users to upload or draw mathematical or physics problems, and receive step-by-step solutions along with natural language explanations. Designed for students, educators, and self-learners, this tool mimics a human tutor using technologies like OCR, Flask, SymPy, and GPT-based models.

---

## 🔧 Features

- ✍️ Accepts handwritten math/physics problem images
- 🔍 Uses OCR and deep learning for character recognition
- 🧮 Symbolic computation with `SymPy`
- 🤖 Generates step-by-step solutions via `GPT` or `Gemini`
- 🗣️ Optional Text-to-Speech output for accessibility
- 🌐 Flask-based web app with a responsive UI

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Flask
- **AI & Libraries:** OpenCV, PIL, Tesseract OCR, SymPy, GPT/Gemini API
- **Utilities:** MathJax (for rendering equations), pyttsx3 or Google TTS

---

## 📷 How It Works

1. **User Uploads Image**  
   → via web interface  
2. **Preprocessing & OCR**  
   → OpenCV filters + CNN for symbol recognition  
3. **Expression Parsing**  
   → Recognizes structure (fractions, exponents, etc.)  
4. **Solution Generation**  
   → Solved with SymPy and explained with GPT  
5. **Output Display**  
   → Markdown + LaTeX rendered to HTML 
