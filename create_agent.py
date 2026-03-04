#!/usr/bin/env python3
"""
ElevenLabs AI Voice Agent Demo for Dental Clinic
Creates and configures a conversational AI agent for after-hours dental clinic support
"""

import requests
import json
import os
from typing import Dict, Any

# Configuration
API_KEY = "sk_907fd00f189be7e3e3834da25224287fdc086cd4f423e196"
BASE_URL = "https://api.elevenlabs.io/v1"

HEADERS = {
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}

DENTAL_CLINIC_CONFIG = {
    "name": "Dental Clinic After-Hours Assistant",
    "tags": ["dental", "healthcare", "after-hours"],
    "conversation_config": {
        "agent": {
            "prompt": {
                "prompt": """You are the after-hours answering service for Bright Smile Dental Clinic. You are professional, caring, and helpful.

Your primary responsibilities:
1. Greet callers warmly and identify yourself as the after-hours service
2. Take detailed messages for non-emergency situations
3. Provide office hours information
4. Handle basic appointment scheduling questions
5. For dental emergencies, advise callers to call 911 or go to the nearest emergency room
6. Reassure patients and provide appropriate guidance

Office Information:
- Name: Bright Smile Dental Clinic
- Hours: Monday-Friday 8:00 AM - 6:00 PM, Saturday 9:00 AM - 2:00 PM, Closed Sunday
- Location: 123 Main Street, Downtown
- Phone: (555) 123-DENT (3368)

Emergency Guidelines:
- For severe pain, swelling, bleeding, or trauma: Advise to go to emergency room or call 911
- For broken teeth or dental trauma: Emergency room
- For lost fillings or minor pain: Can wait until office opens, provide pain management tips
- Always ask for caller's name, phone number, and brief description of the issue

Be empathetic, professional, and never provide medical advice beyond basic emergency guidance."""
            }
        },
        "tts": {
            "model": "eleven_turbo_v2_5",
            "voice_id": "pNInz6obpgDQGcFmaJgB",  # Adam - professional male voice
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        },
        "asr": {
            "model": "eleven_multilingual_v2",
            "language": "en"
        },
        "language": "en",
        "turn_detection": {
            "type": "server_vad",
            "threshold": 0.5,
            "prefix_padding_ms": 300,
            "suffix_padding_ms": 100
        },
        "conversation_config_override": {
            "agent": {
                "first_message": "Hello, you've reached the after-hours answering service for Bright Smile Dental Clinic. My name is Sarah, and I'm here to help you. How can I assist you today?"
            }
        }
    }
}

class ElevenLabsAgentManager:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "xi-api-key": api_key
        }
        self.base_url = BASE_URL

    def create_agent(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new agent with the given configuration"""
        url = f"{self.base_url}/convai/agents"
        
        print(f"Creating agent: {config['name']}")
        print(f"Making request to: {url}")
        
        response = requests.post(url, headers=self.headers, json=config)
        
        if response.status_code == 201:
            result = response.json()
            print(f"✅ Agent created successfully!")
            print(f"Agent ID: {result.get('agent_id')}")
            return result
        else:
            print(f"❌ Error creating agent: {response.status_code}")
            print(f"Response: {response.text}")
            return {"error": response.text}

    def list_agents(self) -> Dict[str, Any]:
        """List all agents in the account"""
        url = f"{self.base_url}/convai/agents"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Error listing agents: {response.status_code}")
            return {"error": response.text}

    def get_agent(self, agent_id: str) -> Dict[str, Any]:
        """Get details for a specific agent"""
        url = f"{self.base_url}/convai/agents/{agent_id}"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Error getting agent: {response.status_code}")
            return {"error": response.text}

    def list_voices(self) -> Dict[str, Any]:
        """List available voices"""
        url = f"{self.base_url}/voices"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Error listing voices: {response.status_code}")
            return {"error": response.text}

def main():
    """Main function to create and configure the dental clinic agent"""
    
    print("🦷 Creating Dental Clinic AI Voice Agent Demo")
    print("=" * 50)
    
    # Initialize agent manager
    agent_manager = ElevenLabsAgentManager(API_KEY)
    
    # List existing agents first
    print("\n📋 Checking existing agents...")
    agents = agent_manager.list_agents()
    
    if "agents" in agents:
        print(f"Found {len(agents['agents'])} existing agents:")
        for agent in agents["agents"]:
            print(f"  - {agent.get('name', 'Unnamed')} (ID: {agent.get('agent_id')})")
    
    # Create the new agent
    print(f"\n🏗️ Creating new agent: {DENTAL_CLINIC_CONFIG['name']}")
    result = agent_manager.create_agent(DENTAL_CLINIC_CONFIG)
    
    if "agent_id" in result:
        agent_id = result["agent_id"]
        
        # Save agent info to file
        agent_info = {
            "agent_id": agent_id,
            "name": DENTAL_CLINIC_CONFIG["name"],
            "created_at": "2026-02-20",
            "config": DENTAL_CLINIC_CONFIG
        }
        
        with open("agent_info.json", "w") as f:
            json.dump(agent_info, f, indent=2)
        
        print(f"\n✅ Agent created successfully!")
        print(f"Agent ID: {agent_id}")
        print(f"Configuration saved to: agent_info.json")
        
        print(f"\n🔗 Next steps:")
        print(f"1. Test the agent via ElevenLabs dashboard: https://elevenlabs.io/app/agents")
        print(f"2. Get a phone number and configure it to use this agent")
        print(f"3. Set up the web widget for website integration")
        
        return agent_id
    else:
        print("❌ Failed to create agent")
        return None

if __name__ == "__main__":
    main()