# SCI-Survey

## Installation
### Requirements
- python >= 3.6
- [npm](https://nodejs.org/ko/download/)


## Development
### Frontend (Vue)
```bash
cd frontend
npm install
npm run serve
```
### Backend (Flask)

```bash
cd backend
pip install -r requirements.txt
python run_server.py
```

## Deployment (w/ docker-compose)
### Requirement
- Docker (docker-compose)

### Build and host
```bash
docker-compose build
docker-compose up  # (-d: backgorund)
```
and connect to `http://{server-ip}` on your web browser.

## Mange Problem List

### Attachments
Put your all resources(image, video) into `backend/public_attachments` directory.  

### Problem list
And copy `backend/variables/problem_type1_list.py.example` to `problem_type1_list.py`. You can modify this file in your style.