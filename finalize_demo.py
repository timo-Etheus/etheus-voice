#!/usr/bin/env python3
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
        "<!-- Replace YOUR_AGENT_ID_HERE with actual agent ID -->\n    <!-- <elevenlabs-convai agent-id=\"YOUR_AGENT_ID_HERE\"></elevenlabs-convai>\n    <script src=\"https://unpkg.com/@elevenlabs/convai-widget-embed\" async type=\"text/javascript\"></script> -->",
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
            alert('🦷 Demo Mode\\n\\nThis is where the ElevenLabs voice agent would appear.\\n\\nTo activate:\\n1. Create agent in ElevenLabs dashboard\\n2. Replace YOUR_AGENT_ID_HERE with actual ID\\n3. Uncomment the widget code above');
        });
    </script>""", ""
    )
    
    with open("demo_website_live.html", "w") as f:
        f.write(updated_html)
    
    print(f"✅ Updated demo website saved as: demo_website_live.html")
    print(f"🔗 Widget code:\n{widget_code}")

if __name__ == "__main__":
    if AGENT_ID == "YOUR_AGENT_ID_HERE":
        print("❌ Please update AGENT_ID with your actual agent ID from ElevenLabs dashboard")
        print("📖 See SETUP_INSTRUCTIONS.md for details")
    else:
        update_demo_website(AGENT_ID)
        print(f"✅ Demo updated with agent ID: {AGENT_ID}")
