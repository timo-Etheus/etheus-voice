
# 🦷 Dental Clinic AI Voice Agent Setup Instructions

## Prerequisites
- ElevenLabs account (free tier is sufficient for testing)
- API key with agent creation permissions

## Step 1: Manual Agent Creation via Dashboard

1. Go to https://elevenlabs.io/app/agents
2. Click "Create New Agent" or "New Assistant"
3. Choose "Blank Template"

## Step 2: Configure Agent Settings

### Basic Settings
- **Name**: Dental Clinic After-Hours Assistant
- **Description**: Professional after-hours answering service for dental clinic
- **Tags**: dental, healthcare, after-hours, emergency

### Agent Tab Configuration

**System Prompt** (copy this exactly):
```
You are the after-hours answering service for Bright Smile Dental Clinic. You are professional, caring, and helpful.

Your primary responsibilities:
1. Greet callers warmly and identify yourself as the after-hours service
2. Take detailed messages for non-emergency situations  
3. Provide office hours information
4. Handle basic appointment scheduling questions
5. For dental emergencies, advise callers to call 911 or go to the nearest emergency room
6. Reassure patients and provide appropriate guidance

Office Information:
- Name: Bright Smile Dental Clinic
- Hours: Monday: 8:00 AM - 6:00 PM, Tuesday: 8:00 AM - 6:00 PM, Wednesday: 8:00 AM - 6:00 PM, Thursday: 8:00 AM - 6:00 PM, Friday: 8:00 AM - 6:00 PM, Saturday: 9:00 AM - 2:00 PM, Sunday: Closed
- Location: 123 Main Street, Downtown
- Phone: (555) 123-DENT

Emergency Guidelines:
- For severe pain, swelling, bleeding, or trauma: Advise to go to emergency room or call 911
- For broken teeth or dental trauma: Emergency room
- For lost fillings or minor pain: Can wait until office opens, provide pain management tips
- Always ask for caller's name, phone number, and brief description of the issue

Be empathetic, professional, and never provide medical advice beyond basic emergency guidance.

```

**First Message** (copy this exactly):
```
Hello, you've reached the after-hours answering service for Bright Smile Dental Clinic. My name is Sarah, and I'm here to help you. How can I assist you today?
```

**Language**: English (en)
**Max Duration**: 10 minutes (600 seconds)

### Voice Tab Configuration
- **Voice**: Adam (Professional, warm male voice)
  - Voice ID: pNInz6obpgDQGcFmaJgB
- **Model**: ElevenLabs Turbo v2.5
- **Stability**: 0.5
- **Similarity Boost**: 0.8
- **Style**: 0.0
- **Speaker Boost**: Enabled

### Conversation Flow
- **Turn Detection**: Server VAD
- **Threshold**: 0.5
- **Prefix Padding**: 300ms
- **Suffix Padding**: 100ms

## Step 3: Test the Agent

### Test Scenarios to Try:

1. **Emergency Call**: Caller with severe tooth pain and swelling
   Expected: Should advise to go to emergency room or call 911

2. **Appointment Request**: Caller wanting to schedule a cleaning
   Expected: Should take message with contact info and preferred times

3. **Office Hours Inquiry**: Caller asking about office hours
   Expected: Should provide complete hours information

4. **Lost Filling**: Caller with a lost filling, mild pain
   Expected: Should advise it can wait until office opens, provide comfort tips


### Expected Behaviors:
- ✅ Professional, warm greeting identifying as after-hours service
- ✅ Takes detailed messages (name, phone, issue description)
- ✅ Provides correct office hours
- ✅ Handles emergencies by directing to ER/911
- ✅ Reassures patients appropriately
- ✅ Never gives medical advice

## Step 4: Deploy Options

### Option A: Web Widget
After creating the agent, you'll get an agent ID. Use this widget code:

```html
<!-- ElevenLabs Dental Clinic Voice Agent Widget -->
<elevenlabs-convai agent-id="YOUR_AGENT_ID_HERE"></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
```

### Option B: Phone Integration
1. In the ElevenLabs dashboard, go to Phone Numbers
2. Purchase or configure a phone number
3. Connect the phone number to your agent
4. Test by calling the number

## Step 5: Customization

### For Different Clinics:
- Update clinic name, hours, and contact info in the system prompt
- Adjust voice selection based on preference
- Modify emergency protocols based on clinic policy

### Advanced Features:
- Add knowledge base with common dental FAQs
- Set up appointment booking integration (requires tools/API)
- Configure call recording and transcription
- Set up notifications for urgent calls

## Pricing Estimates (as of 2026)
- **Basic Testing**: Free tier (10,000 characters/month)
- **Production Use**: Pay-per-use (approximately $0.15-0.30 per minute of conversation)
- **Phone Numbers**: $1-5/month per number
- **High Volume**: Custom enterprise pricing

## Support
- ElevenLabs Documentation: https://elevenlabs.io/docs
- Community: https://discord.gg/elevenlabs
- Support: support@elevenlabs.io
