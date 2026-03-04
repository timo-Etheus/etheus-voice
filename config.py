"""
Configuration file for the Dental Clinic AI Voice Agent Demo
"""

# ElevenLabs API Configuration
API_KEY = "sk_907fd00f189be7e3e3834da25224287fdc086cd4f423e196"
BASE_URL = "https://api.elevenlabs.io/v1"

# Clinic Information
CLINIC_INFO = {
    "name": "Bright Smile Dental Clinic",
    "phone": "(555) 123-DENT",
    "address": "123 Main Street, Downtown",
    "hours": {
        "monday": "8:00 AM - 6:00 PM",
        "tuesday": "8:00 AM - 6:00 PM", 
        "wednesday": "8:00 AM - 6:00 PM",
        "thursday": "8:00 AM - 6:00 PM",
        "friday": "8:00 AM - 6:00 PM",
        "saturday": "9:00 AM - 2:00 PM",
        "sunday": "Closed"
    }
}

# Voice Configuration
VOICE_CONFIG = {
    "voice_id": "pNInz6obpgDQGcFmaJgB",  # Adam - professional, warm male voice
    "model": "eleven_turbo_v2_5",
    "stability": 0.5,
    "similarity_boost": 0.8,
    "style": 0.0,
    "use_speaker_boost": True
}

# Alternative voices for different personas
ALTERNATIVE_VOICES = {
    "sarah": "EXAVITQu4vr4xnSDxMaL",  # Sarah - professional female
    "adam": "pNInz6obpgDQGcFmaJgB",   # Adam - professional male  
    "rachel": "21m00Tcm4TlvDq8ikWAM",  # Rachel - warm female
    "antoni": "ErXwobaYiN019PkySvjV"   # Antoni - friendly male
}

# System Prompt Template
SYSTEM_PROMPT_TEMPLATE = """You are the after-hours answering service for {clinic_name}. You are professional, caring, and helpful.

Your primary responsibilities:
1. Greet callers warmly and identify yourself as the after-hours service
2. Take detailed messages for non-emergency situations  
3. Provide office hours information
4. Handle basic appointment scheduling questions
5. For dental emergencies, advise callers to call 911 or go to the nearest emergency room
6. Reassure patients and provide appropriate guidance

Office Information:
- Name: {clinic_name}
- Hours: {hours_summary}
- Location: {address}
- Phone: {phone}

Emergency Guidelines:
- For severe pain, swelling, bleeding, or trauma: Advise to go to emergency room or call 911
- For broken teeth or dental trauma: Emergency room
- For lost fillings or minor pain: Can wait until office opens, provide pain management tips
- Always ask for caller's name, phone number, and brief description of the issue

Be empathetic, professional, and never provide medical advice beyond basic emergency guidance.
"""

# First Message Template
FIRST_MESSAGE_TEMPLATE = "Hello, you've reached the after-hours answering service for {clinic_name}. My name is {agent_name}, and I'm here to help you. How can I assist you today?"

def get_system_prompt(clinic_name: str = None, agent_name: str = "Sarah") -> str:
    """Generate system prompt with clinic information"""
    clinic_name = clinic_name or CLINIC_INFO["name"]
    
    # Format hours summary
    hours_list = []
    for day, hours in CLINIC_INFO["hours"].items():
        hours_list.append(f"{day.title()}: {hours}")
    hours_summary = ", ".join(hours_list)
    
    return SYSTEM_PROMPT_TEMPLATE.format(
        clinic_name=clinic_name,
        hours_summary=hours_summary,
        address=CLINIC_INFO["address"],
        phone=CLINIC_INFO["phone"]
    )

def get_first_message(clinic_name: str = None, agent_name: str = "Sarah") -> str:
    """Generate first message with clinic information"""
    clinic_name = clinic_name or CLINIC_INFO["name"]
    
    return FIRST_MESSAGE_TEMPLATE.format(
        clinic_name=clinic_name,
        agent_name=agent_name
    )

# Demo scenarios for testing
DEMO_SCENARIOS = [
    {
        "name": "Emergency Call",
        "description": "Caller with severe tooth pain and swelling",
        "expected_response": "Should advise to go to emergency room or call 911"
    },
    {
        "name": "Appointment Request", 
        "description": "Caller wanting to schedule a cleaning",
        "expected_response": "Should take message with contact info and preferred times"
    },
    {
        "name": "Office Hours Inquiry",
        "description": "Caller asking about office hours",
        "expected_response": "Should provide complete hours information"
    },
    {
        "name": "Lost Filling",
        "description": "Caller with a lost filling, mild pain",
        "expected_response": "Should advise it can wait until office opens, provide comfort tips"
    }
]