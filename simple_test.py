#!/usr/bin/env python3
"""
Simplified test - just try to create an agent directly
"""

import requests
import json
from config import API_KEY, BASE_URL, get_system_prompt, get_first_message

def test_agent_creation():
    """Test creating the dental clinic agent with minimal config"""
    
    headers = {
        "Content-Type": "application/json", 
        "xi-api-key": API_KEY
    }
    
    # Simplified agent configuration
    agent_config = {
        "name": "Dental Clinic Demo Agent",
        "conversation_config": {
            "agent": {
                "prompt": {
                    "prompt": get_system_prompt()
                },
                "first_message": get_first_message(),
                "language": "en"
            }
        }
    }
    
    print("🦷 Testing Simplified Dental Clinic AI Agent Creation")
    print("=" * 60)
    
    # Try creating the agent directly
    print("🏗️ Creating agent...")
    agent_url = f"{BASE_URL}/convai/agents"
    
    print(f"Request URL: {agent_url}")
    print(f"Request headers: {headers}")
    print(f"Request payload keys: {list(agent_config.keys())}")
    
    response = requests.post(agent_url, headers=headers, json=agent_config)
    
    print(f"Response status: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")
    print(f"Response body: {response.text}")
    
    if response.status_code in [200, 201]:
        agent_data = response.json()
        agent_id = agent_data.get("agent_id")
        
        print(f"✅ Agent created successfully!")
        print(f"Agent ID: {agent_id}")
        
        return agent_id
    else:
        print(f"❌ Failed to create agent: {response.status_code}")
        try:
            error_data = response.json()
            print(f"Error details: {json.dumps(error_data, indent=2)}")
        except:
            print(f"Raw error: {response.text}")
        return None

def test_user_info():
    """Test getting user information"""
    headers = {
        "xi-api-key": API_KEY
    }
    
    user_url = f"{BASE_URL}/user"
    print(f"\n🔍 Testing user info endpoint...")
    
    response = requests.get(user_url, headers=headers)
    print(f"User info status: {response.status_code}")
    
    if response.status_code == 200:
        user_data = response.json()
        print(f"User info: {json.dumps(user_data, indent=2)}")
        return user_data
    else:
        print(f"User info error: {response.text}")
        return None

if __name__ == "__main__":
    # Test user info first to see if API key works at all
    test_user_info()
    
    # Then try creating agent
    test_agent_creation()