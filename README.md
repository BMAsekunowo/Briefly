# 🧠 Briefly – Your Daily Productivity Assistant

**Briefly** is a smart assistant built with Django, Celery, and Redis that helps users stay on top of important updates from emails and messages. It delivers a **daily brief** (or on-demand updates) via platforms like WhatsApp, making personal productivity accessible and proactive.

---

## 🚀 Features

- 🔒 **User Authentication**
- 📥 **Multi-Account Email Connection**
- 🧾 **Daily Brief Parsing & Summary**
- 💬 **Delivery via WhatsApp** (initially)
- ⏰ **Smart Reminders & Task Management**
- 📣 **Aggregates Messages from Multiple Sources**
- ⚙️ **Celery-based Background Task System**
- ⏲️ **Periodic Task Scheduling with Celery Beat**

---

## 🛠️ Tech Stack

- **Backend**: Django + Django Rest Framework  
- **Task Queue**: Celery  
- **Scheduler**: Celery Beat  
- **Message Broker**: Redis  
- **Database**: PostgreSQL (SQLite in development)  
- **Deployment**: Docker (planned), GitHub Actions, etc.

---

## 📦 Project Structure

```
Briefly/
├── accounts/
├── api/
├── celery_tasks/
├── core/
├── dashboard/
├── emails/
├── integrations/
├── notifications/
├── reminders/
├── static/
├── templates/
├── Briefly/
│   └── settings.py
└── manage.py
```

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.12  
- Redis server running locally  
- Virtual environment activated  
- Required Python packages installed (`pip install -r requirements.txt`)  

### 💻 Run Django Server

```bash
python manage.py runserver
```

### 🧵 Start Celery Worker

```bash
celery -A core worker --loglevel=info
```

### 🧠 Start Celery Beat Scheduler

```bash
celery -A core beat --loglevel=info
```

### 🔄 Start Redis (if not already running)

```bash
redis-server
```

---

## 🎯 Project Goals

- Make personal assistant-level productivity available to everyone  
- Empower users to get proactive daily updates  
- Help users manage tasks and reminders via messaging  
- Let users never miss what matters again  

---

## 🛤️ Roadmap

- [ ] WhatsApp Message Delivery (via API)  
- [ ] Admin UI for Task Management  
- [ ] Email Parsing Logic  
- [ ] Dynamic Reminder Creation  
- [ ] Dockerization & Cloud Deployment  

---

## 👤 Author

**Boluwatife Asekunowo**  
- [GitHub](https://github.com/BMAsekunowo)  
- [X](https://x.com/BMAsekunowo)  
- [LinkedIn](https://www.linkedin.com/in/boluwatife-asekunowo-60956133a/)