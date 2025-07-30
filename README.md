# ♂️ Gachimuchi API – Right Version

A fun yet fully-functional RESTful API built with **FastAPI**, providing structured access to the world of ♂ Gachimuchi ♂ characters and media. This project blends meme culture with clean backend design and optional frontend documentation via **Vue 3**.

---

## ♂️ Project Description

**Gachimuchi API – Right Version** is a tongue-in-cheek, yet functional RESTful API built with **FastAPI** that provides structured access to a database of ♂ Gachimuchi ♂ characters and media. Designed for fun, fan communities, or meme-based experiments, this API allows users to search, retrieve, and reference iconic media, quotes, and personalities from the legendary Gachimuchi universe — including figures like Billy Herrington, Van Darkholm, and others.

In addition to the backend, the project includes a lightweight **Vue.js** frontend (docs site), which serves as a visual reference and documentation layer — ideal for browsing available endpoints and exploring the lore in a structured format.

Despite its meme origin, the project follows proper software engineering practices and is ready for production deployment on services like **Render** and **Vercel**.

---

## 🎯 Features

- 🔍 Search characters by `name`, `surname`, or `nickname`
- 🎬 Search Gachimuchi media by `title`
- 📁 Media objects include `file_url`, `character_id`, and timestamps
- 🌐 FastAPI-based REST API with auto-generated Swagger and ReDoc docs
- 🧩 PostgreSQL/Supabase as the backend database
- ⚡ Deployed with Uvicorn for async performance
- 📘 Optional Vue 3 frontend for documentation and browsing

---

## 🛠️ Technologies

- Python 3.10+
- FastAPI
- Supabase (PostgreSQL)
- Uvicorn
- Pydantic
- Vue 3 (optional frontend)
- Vercel (for frontend)
- Render.com (for backend deployment)

---

## 🚀 Deployment

### Backend (Render.com)

1. Create a **new Web Service** on [Render.com](https://render.com).
2. Set environment variables for Supabase URL and key:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
3. Add a `start.sh` file:

```bash
#!/bin/bash
uvicorn main:app --host 0.0.0.0 --port $PORT