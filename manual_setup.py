#!/usr/bin/env python3
"""
Manual setup guide and demo configuration for ElevenLabs Dental Clinic Agent
Since API key permissions may be limited, this provides manual setup instructions
"""

import json
from config import get_system_prompt, get_first_message, VOICE_CONFIG, CLINIC_INFO, DEMO_SCENARIOS

def generate_agent_config():
    """Generate the complete agent configuration for manual setup"""
    
    config = {
        "name": "Dental Clinic After-Hours Assistant",
        "description": "Professional after-hours answering service for dental clinic",
        "tags": ["dental", "healthcare", "after-hours", "emergency"],
        "conversation_config": {
            "agent": {
                "prompt": {
                    "prompt": get_system_prompt()
                },
                "first_message": get_first_message(),
                "language": "en",
                "max_duration_seconds": 600  # 10 minute max calls
            },
            "tts": {
                "model_id": VOICE_CONFIG["model"],
                "voice_id": VOICE_CONFIG["voice_id"],
                "voice_settings": {
                    "stability": VOICE_CONFIG["stability"],
                    "similarity_boost": VOICE_CONFIG["similarity_boost"], 
                    "style": VOICE_CONFIG["style"],
                    "use_speaker_boost": VOICE_CONFIG["use_speaker_boost"]
                }
            },
            "asr": {
                "model": "eleven_multilingual_v2",
                "language": "en"
            },
            "conversation_config": {
                "turn_detection": {
                    "type": "server_vad",
                    "threshold": 0.5,
                    "prefix_padding_ms": 300,
                    "suffix_padding_ms": 100
                }
            }
        },
        "platform_settings": {
            "widget": {
                "conversation_mode": "text_and_audio",
                "position": "bottom-right",
                "color_scheme": "light"
            }
        }
    }
    
    return config

def generate_setup_instructions():
    """Generate step-by-step setup instructions"""
    
    instructions = """
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
{system_prompt}
```

**First Message** (copy this exactly):
```
{first_message}
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
{test_scenarios}

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
"""
    
    system_prompt = get_system_prompt()
    first_message = get_first_message()
    
    # Format test scenarios
    test_scenarios_text = ""
    for i, scenario in enumerate(DEMO_SCENARIOS, 1):
        test_scenarios_text += f"\n{i}. **{scenario['name']}**: {scenario['description']}\n   Expected: {scenario['expected_response']}\n"
    
    return instructions.format(
        system_prompt=system_prompt,
        first_message=first_message,
        test_scenarios=test_scenarios_text
    )

def create_demo_files():
    """Create all necessary demo files"""
    
    print("🦷 Creating Dental Clinic AI Voice Agent Demo Files")
    print("=" * 55)
    
    # Generate agent configuration
    config = generate_agent_config()
    
    # Save configuration to JSON file
    with open("agent_configuration.json", "w") as f:
        json.dump(config, f, indent=2)
    print("✅ Saved: agent_configuration.json")
    
    # Generate setup instructions
    instructions = generate_setup_instructions()
    
    # Save instructions to markdown file
    with open("SETUP_INSTRUCTIONS.md", "w") as f:
        f.write(instructions)
    print("✅ Saved: SETUP_INSTRUCTIONS.md")
    
    # Create sample HTML widget page
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dental Clinic - After Hours Service</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .header {{
            text-align: center;
            border-bottom: 2px solid #2c5aa0;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        
        .clinic-info {{
            background: #e7f3ff;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        
        .emergency {{
            background: #ffebee;
            border: 2px solid #f44336;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        
        .hours {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            margin: 15px 0;
        }}
        
        .day {{
            padding: 10px;
            background: #f5f5f5;
            border-radius: 5px;
            text-align: center;
        }}
        
        .cta {{
            text-align: center;
            margin: 30px 0;
            padding: 20px;
            background: #2c5aa0;
            color: white;
            border-radius: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🦷 {CLINIC_INFO['name']}</h1>
            <p>Professional Dental Care You Can Trust</p>
        </div>
        
        <div class="emergency">
            <h2>🚨 Dental Emergency?</h2>
            <p><strong>For severe pain, bleeding, trauma, or life-threatening situations:</strong></p>
            <p>Call 911 or go to your nearest emergency room immediately.</p>
        </div>
        
        <div class="clinic-info">
            <h2>📍 Clinic Information</h2>
            <p><strong>Address:</strong> {CLINIC_INFO['address']}</p>
            <p><strong>Phone:</strong> {CLINIC_INFO['phone']}</p>
            
            <h3>Office Hours</h3>
            <div class="hours">
                <div class="day"><strong>Monday</strong><br>{CLINIC_INFO['hours']['monday']}</div>
                <div class="day"><strong>Tuesday</strong><br>{CLINIC_INFO['hours']['tuesday']}</div>
                <div class="day"><strong>Wednesday</strong><br>{CLINIC_INFO['hours']['wednesday']}</div>
                <div class="day"><strong>Thursday</strong><br>{CLINIC_INFO['hours']['thursday']}</div>
                <div class="day"><strong>Friday</strong><br>{CLINIC_INFO['hours']['friday']}</div>
                <div class="day"><strong>Saturday</strong><br>{CLINIC_INFO['hours']['saturday']}</div>
                <div class="day"><strong>Sunday</strong><br>{CLINIC_INFO['hours']['sunday']}</div>
            </div>
        </div>
        
        <div class="cta">
            <h2>📞 After-Hours Support</h2>
            <p>Our office is currently closed, but our AI assistant is here to help!</p>
            <p><strong>Click the voice assistant icon below to:</strong></p>
            <ul style="text-align: left; display: inline-block;">
                <li>Leave a message for our staff</li>
                <li>Get office hours information</li>
                <li>Receive emergency guidance</li>
                <li>Ask basic questions</li>
            </ul>
        </div>
    </div>
    
    <!-- Replace YOUR_AGENT_ID_HERE with actual agent ID -->
    <!-- <elevenlabs-convai agent-id="YOUR_AGENT_ID_HERE"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script> -->
    
    <!-- Demo placeholder (replace above when you have agent ID) -->
    <div style="position: fixed; bottom: 20px; right: 20px; background: #2c5aa0; color: white; padding: 15px; border-radius: 50px; cursor: pointer; font-weight: bold;">
        🎤 Voice Assistant (Demo)
    </div>
    
    <script>
        // Demo functionality - remove when implementing real agent
        document.querySelector('div[style*="position: fixed"]').addEventListener('click', function() {{
            alert('🦷 Demo Mode\\n\\nThis is where the ElevenLabs voice agent would appear.\\n\\nTo activate:\\n1. Create agent in ElevenLabs dashboard\\n2. Replace YOUR_AGENT_ID_HERE with actual ID\\n3. Uncomment the widget code above');
        }});
    </script>
</body>
</html>"""
    
    with open("demo_website.html", "w") as f:
        f.write(html_content)
    print("✅ Saved: demo_website.html")
    
    # Create requirements.txt
    with open("requirements.txt", "w") as f:
        f.write("requests>=2.32.0\n")
    print("✅ Saved: requirements.txt")
    
    # Create simple test script for when agent is created
    test_script = '''#!/usr/bin/env python3
"""
Test script to use once agent is created
"""

# Update these with your actual agent details
AGENT_ID = "YOUR_AGENT_ID_HERE"  # Replace with actual agent ID from ElevenLabs dashboard

def generate_widget_code(agent_id):
    """Generate embeddable widget code"""
    return f"""<!-- ElevenLabs Voice Agent Widget -->
<elevenlabs-convai agent-id="{agent_id}"></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>

<style>
elevenlabs-convai {{
    position: fixed !important;
    bottom: 20px !important;
    right: 20px !important;
    z-index: 1000 !important;
}}
</style>"""

def update_demo_website(agent_id):
    """Update demo website with actual agent ID"""
    with open("demo_website.html", "r") as f:
        html_content = f.read()
    
    # Replace placeholder with actual widget code
    widget_code = generate_widget_code(agent_id)
    updated_html = html_content.replace(
        "<!-- Replace YOUR_AGENT_ID_HERE with actual agent ID -->\\n    <!-- <elevenlabs-convai agent-id=\\"YOUR_AGENT_ID_HERE\\"></elevenlabs-convai>\\n    <script src=\\"https://unpkg.com/@elevenlabs/convai-widget-embed\\" async type=\\"text/javascript\\"></script> -->",
        widget_code
    )
    
    # Remove demo placeholder
    updated_html = updated_html.replace(
        """<!-- Demo placeholder (replace above when you have agent ID) -->
    <div style="position: fixed; bottom: 20px; right: 20px; background: #2c5aa0; color: white; padding: 15px; border-radius: 50px; cursor: pointer; font-weight: bold;">
        🎤 Voice Assistant (Demo)
    </div>
    
    <script>
        // Demo functionality - remove when implementing real agent
        document.querySelector('div[style*="position: fixed"]').addEventListener('click', function() {
            alert('🦷 Demo Mode\\\\n\\\\nThis is where the ElevenLabs voice agent would appear.\\\\n\\\\nTo activate:\\\\n1. Create agent in ElevenLabs dashboard\\\\n2. Replace YOUR_AGENT_ID_HERE with actual ID\\\\n3. Uncomment the widget code above');
        });
    </script>""", ""
    )
    
    with open("demo_website_live.html", "w") as f:
        f.write(updated_html)
    
    print(f"✅ Updated demo website saved as: demo_website_live.html")
    print(f"🔗 Widget code:\\n{widget_code}")

if __name__ == "__main__":
    if AGENT_ID == "YOUR_AGENT_ID_HERE":
        print("❌ Please update AGENT_ID with your actual agent ID from ElevenLabs dashboard")
        print("📖 See SETUP_INSTRUCTIONS.md for details")
    else:
        update_demo_website(AGENT_ID)
        print(f"✅ Demo updated with agent ID: {AGENT_ID}")
'''
    
    with open("finalize_demo.py", "w") as f:
        f.write(test_script)
    print("✅ Saved: finalize_demo.py")
    
    print("\n🎯 Demo Setup Complete!")
    print("=" * 30)
    print("Files created:")
    print("  📄 agent_configuration.json - Full agent config")
    print("  📚 SETUP_INSTRUCTIONS.md - Step-by-step setup guide")
    print("  🌐 demo_website.html - Sample dental clinic website")
    print("  📋 requirements.txt - Python dependencies")
    print("  🔧 finalize_demo.py - Script to finalize setup")
    
    print("\n📋 Next Steps:")
    print("1. Read SETUP_INSTRUCTIONS.md")
    print("2. Create agent manually via ElevenLabs dashboard")
    print("3. Update finalize_demo.py with your agent ID")
    print("4. Run finalize_demo.py to generate live website")
    print("5. Test with demo scenarios")
    
    return True

if __name__ == "__main__":
    create_demo_files()