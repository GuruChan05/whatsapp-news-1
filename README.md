# whatsapp-news-1

Daily AI-powered Sports, Politics and AI news delivered to WhatsApp.

## Features

- Fetch latest news
- AI-generated summaries
- WhatsApp delivery
- Automatic daily scheduling

## Setup

### Clone

```bash
git clone https://github.com/YOUR_USERNAME/whatsapp-news-agent.git

cd whatsapp-news-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Configure

Edit `.env`

```env
NEWS_API_KEY=
OPENAI_API_KEY=
WHATSAPP_TOKEN=
PHONE_NUMBER_ID=
MY_PHONE=
```

### Run

```bash
python main.py
```

## Deployment

Deploy to:
- Render
- Railway
- PythonAnywhere
- VPS