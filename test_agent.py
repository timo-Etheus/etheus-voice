#!/usr/bin/env python3
"""
Test script for the Dental Clinic AI Voice Agent
"""

import requests
import json
import time
from config import API_KEY, BASE_URL, get_system_prompt, get_first_message, VOICE_CONFIG, DEMO_SCENARIOS

def test_agent_creation():
    """Test creating the dental clinic agent"""
    
    headers = {
        "Content-Type": "application/json", 
        "xi-api-key": API_KEY
    }
    
    # Updated agent configuration based on latest ElevenLabs API
    agent_config = {
        "name": "Dental Clinic After-Hours Demo",
        "tags": ["dental", "healthcare", "after-hours", "demo"],
        "conversation_config": {
            "agent": {
                "prompt": {
                    "prompt": get_system_prompt()
                },
                "first_message": get_first_message(),
                "language": "en"
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
        }
    }
    
    print("🦷 Testing Dental Clinic AI Agent Creation")
    print("=" * 50)
    
    # Test API connectivity first
    print("🔍 Testing API connectivity...")
    voices_url = f"{BASE_URL}/voices"
    response = requests.get(voices_url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ API connectivity test failed: {response.status_code}")
        print(f"Response: {response.text}")
        return None
    else:
        print("✅ API connectivity successful")
        voices_data = response.json()
        print(f"Found {len(voices_data.get('voices', []))} available voices")
    
    # Create the agent
    print(f"\n🏗️ Creating agent...")
    agent_url = f"{BASE_URL}/convai/agents"
    
    print(f"Request URL: {agent_url}")
    print(f"Request payload: {json.dumps(agent_config, indent=2)}")
    
    response = requests.post(agent_url, headers=headers, json=agent_config)
    
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.text}")
    
    if response.status_code in [200, 201]:
        agent_data = response.json()
        agent_id = agent_data.get("agent_id")
        
        print(f"✅ Agent created successfully!")
        print(f"Agent ID: {agent_id}")
        
        # Save agent info
        agent_info = {
            "agent_id": agent_id,
            "name": agent_config["name"],
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "config": agent_config,
            "response": agent_data
        }
        
        with open("agent_info.json", "w") as f:
            json.dump(agent_info, f, indent=2)
        
        print(f"Agent info saved to: agent_info.json")
        return agent_id
    else:
        print(f"❌ Failed to create agent: {response.status_code}")
        print(f"Error details: {response.text}")
        return None

def list_existing_agents():
    """List all existing agents"""
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }
    
    url = f"{BASE_URL}/convai/agents"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        agents_data = response.json()
        agents = agents_data.get("agents", [])
        
        print(f"\n📋 Found {len(agents)} existing agents:")
        for agent in agents:
            print(f"  - {agent.get('name', 'Unnamed')} (ID: {agent.get('agent_id')})")
            print(f"    Created: {agent.get('created_at', 'Unknown')}")
        
        return agents
    else:
        print(f"❌ Failed to list agents: {response.status_code}")
        return []

def get_widget_code(agent_id: str) -> str:
    """Generate widget code for embedding the agent"""
    widget_code = f"""<!-- ElevenLabs Dental Clinic Voice Agent Widget -->
<elevenlabs-convai agent-id="{agent_id}"></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>

<!-- Styling (optional) -->
<style>
elevenlabs-convai {{
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
}}
</style>"""
    
    return widget_code

def main():
    """Main test function"""
    print("🧪 Dental Clinic AI Voice Agent Test Suite")
    print("=" * 50)
    
    # List existing agents first
    existing_agents = list_existing_agents()
    
    # Check if we already have a dental clinic agent
    dental_agent = None
    for agent in existing_agents:
        if "dental" in agent.get("name", "").lower():
            dental_agent = agent
            break
    
    if dental_agent:
        print(f"\n🔄 Found existing dental agent: {dental_agent['name']}")
        print(f"Agent ID: {dental_agent['agent_id']}")
        agent_id = dental_agent['agent_id']
    else:
        # Create new agent
        agent_id = test_agent_creation()
    
    if agent_id:
        print(f"\n🎯 Agent ready for testing!")
        print(f"Agent ID: {agent_id}")
        
        # Generate widget code
        widget_code = get_widget_code(agent_id)
        
        # Save widget code to file
        with open("widget.html", "w") as f:
            f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dental Clinic Voice Agent Demo</title>
</head>
<body>
    <h1>Dental Clinic After-Hours Voice Assistant Demo</h1>
    <p>Click the voice assistant button to test the dental clinic after-hours service.</p>
    
    {widget_code}
</body>
</html>""")
        
        print(f"\n📄 Widget code saved to: widget.html")
        print(f"\n🔗 Testing options:")
        print(f"1. Open widget.html in your browser")
        print(f"2. Visit ElevenLabs dashboard: https://elevenlabs.io/app/agents")
        print(f"3. Integrate into your website using the widget code")
        
        print(f"\n🎭 Test scenarios to try:")
        for i, scenario in enumerate(DEMO_SCENARIOS, 1):
            print(f"{i}. {scenario['name']}: {scenario['description']}")
            print(f"   Expected: {scenario['expected_response']}")
        
        return agent_id
    else:
        print("❌ Agent creation failed")
        return None

if __name__ == "__main__":
    main()