# FileShare

FileShare is a Django-based file-sharing application that allows users to upload files and generate a unique URL to share with others. The recipients can then use the URL to download the shared files.

## Features
- Upload files easily via a web interface.
- Generate a shareable link for each uploaded file.
- Download files using the provided unique URL.
- Hosted on **Render.com** using **Gunicorn** and **Whitenoise** for serving static and media files.

## Tech Stack
- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default) / PostgreSQL (for production)
- **Deployment:** Render.com
- **File Handling:** Django Media Files with Whitenoise

---

## Live Project
Check out the live project here: [FileShare Live](https://fileshare-ggz0.onrender.com)

---

## Installation
### 1. Clone the Repository
```sh
 git clone https://github.com/yourusername/fileshare.git
 cd fileshare
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Run the Server
```sh
python manage.py runserver
```

Now, open your browser and go to `http://127.0.0.1:8000/`.

---

## Usage
### Upload a File
1. Visit the homepage.
2. Select a file to upload.
3. Click "Upload" to generate a unique URL.

### Share the File
- Copy the generated URL and send it to others.

### Download a File
- Open the shared URL in a browser.
- Click the "Download" button to retrieve the file.



