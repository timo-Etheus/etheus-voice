# 🦷 AI Voice Agent Demo - Dental Clinic After-Hours Service

A complete demonstration of an AI voice agent built with ElevenLabs Conversational AI for dental clinic after-hours support.

## 🎯 Project Overview

This demo creates an intelligent voice agent that can:
- ✅ Greet callers professionally as an after-hours service
- ✅ Take detailed messages for non-emergency situations
- ✅ Provide office hours and basic information
- ✅ Handle emergency situations by directing to appropriate care
- ✅ Reassure patients with professional, empathetic responses
- ✅ Never provide medical advice beyond emergency guidance

## 📁 Project Structure

```
/demo/
├── README.md                     # This file - project overview
├── SETUP_INSTRUCTIONS.md         # Detailed setup guide
├── config.py                     # Configuration and clinic info
├── agent_configuration.json      # Complete agent config for ElevenLabs
├── demo_website.html            # Sample dental clinic website
├── finalize_demo.py             # Script to activate live agent
├── requirements.txt             # Python dependencies
├── manual_setup.py              # Script that generated all files
├── create_agent.py              # API-based agent creation (requires special permissions)
├── test_agent.py                # Testing script
└── venv/                        # Python virtual environment
```

## 🚀 Quick Start

### Option 1: Manual Setup (Recommended)

1. **Read the setup guide**:
   ```bash
   open SETUP_INSTRUCTIONS.md
   ```

2. **Create agent via ElevenLabs dashboard**:
   - Go to https://elevenlabs.io/app/agents
   - Create new agent using configuration from `agent_configuration.json`
   - Follow detailed instructions in `SETUP_INSTRUCTIONS.md`

3. **Test the demo website**:
   ```bash
   open demo_website.html
   ```

4. **Finalize with your agent ID**:
   ```bash
   # Edit finalize_demo.py with your agent ID
   python3 finalize_demo.py
   open demo_website_live.html
   ```

### Option 2: API Setup (Requires Special Permissions)

```bash
# Set up virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Try creating agent via API
python3 create_agent.py
```

**Note**: The provided API key may not have agent creation permissions. Use manual setup if you get permission errors.

## 🎭 Demo Features

### Voice Agent Capabilities
- **Professional greeting**: "Hello, you've reached the after-hours answering service for Bright Smile Dental Clinic..."
- **Emergency handling**: Directs severe cases to ER/911
- **Message taking**: Collects name, phone, and issue description
- **Office information**: Provides hours and contact details
- **Empathetic responses**: Professional, caring tone throughout

### Technical Features
- **Voice**: Adam (professional male voice) with optimized settings
- **Language**: English with multilingual ASR support
- **Turn detection**: Server-side VAD for natural conversation flow
- **Duration limits**: 10-minute maximum calls
- **Integration**: Web widget and phone number support

## 🧪 Testing Scenarios

Try these scenarios to test the agent:

1. **Emergency Call**: "I have severe tooth pain and my face is swelling"
   - *Expected*: Should direct to emergency room or 911

2. **Appointment Request**: "I'd like to schedule a teeth cleaning"
   - *Expected*: Should take detailed message with contact info

3. **Office Hours**: "What time do you open tomorrow?"
   - *Expected*: Should provide complete hours information

4. **Lost Filling**: "My filling fell out but there's only mild pain"
   - *Expected*: Should advise it can wait, provide comfort tips

## 🛠️ Customization

### For Different Clinics
Edit `config.py` to customize:
- Clinic name, address, phone number
- Office hours
- Emergency protocols
- Voice selection and settings

### Advanced Features
- **Knowledge Base**: Add dental FAQs and procedures
- **Appointment Booking**: Integrate with scheduling systems
- **Call Recording**: Enable transcription and logging
- **Multiple Languages**: Configure for multilingual support

## 💰 Pricing Estimates

Based on ElevenLabs pricing (as of 2026):
- **Free Tier**: 10,000 characters/month (good for testing)
- **Production**: ~$0.15-0.30 per minute of conversation
- **Phone Numbers**: $1-5/month per number
- **High Volume**: Custom enterprise pricing available

## 🔗 Integration Options

### Web Widget
```html
<elevenlabs-convai agent-id="your-agent-id"></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async></script>
```

### Phone Integration
- Purchase phone number via ElevenLabs dashboard
- Configure number to use your agent
- Test by calling the number

### Mobile Apps
- React Native SDK available
- Native iOS (Swift) and Android (Kotlin) SDKs
- WebSocket API for custom implementations

## 📞 Getting a Demo Phone Number

1. **Via ElevenLabs Dashboard**:
   - Go to Phone Numbers section
   - Purchase a number (usually $1-5/month)
   - Assign your agent to the number
   - Test immediately

2. **Via Twilio Integration**:
   - Connect existing Twilio account
   - Use existing phone numbers
   - More complex setup but full control

## 🔍 Monitoring & Analytics

ElevenLabs provides built-in analytics:
- Conversation history and recordings
- Response time metrics  
- User satisfaction analysis
- Custom evaluation criteria
- A/B testing capabilities

## 🆘 Troubleshooting

### Common Issues

**API Permission Errors**: Use manual setup via dashboard instead of API creation

**Voice Not Working**: Check browser permissions for microphone access

**Agent Not Responding**: Verify agent ID is correct in widget code

**Poor Voice Quality**: Adjust voice settings (stability, similarity boost)

### Getting Help
- **Documentation**: https://elevenlabs.io/docs
- **Community Discord**: https://discord.gg/elevenlabs
- **Support Email**: support@elevenlabs.io

## 📋 Production Checklist

Before deploying to production:

- [ ] Test all demo scenarios thoroughly
- [ ] Configure appropriate emergency protocols
- [ ] Set up call recording/logging if required
- [ ] Configure proper HIPAA compliance if needed
- [ ] Set usage limits and monitoring alerts
- [ ] Train staff on handling messages from the agent
- [ ] Create backup procedures for system downtime
- [ ] Test phone number integration thoroughly

## 🎬 Demo Walkthrough

1. **Visit the demo website**: Open `demo_website.html`
2. **Click voice assistant**: Activate the agent (when configured)
3. **Try emergency scenario**: Test emergency detection
4. **Leave a message**: Test message-taking functionality
5. **Ask about hours**: Verify information accuracy
6. **Test edge cases**: Try unclear or complex requests

## 🚀 Next Steps for Production

1. **Customize for your clinic**: Update all clinic-specific information
2. **Get phone number**: Purchase and configure phone integration
3. **Train staff**: Ensure team knows how to handle agent messages
4. **Monitor performance**: Use ElevenLabs analytics to optimize
5. **Gather feedback**: Collect patient feedback and improve
6. **Scale up**: Add more features like appointment booking

## 📄 License

This demo is provided as-is for educational and demonstration purposes. Customize as needed for your specific use case.

---

**Created**: February 20, 2026  
**Last Updated**: February 20, 2026  
**Version**: 1.0  
**Contact**: Built with ❤️ using ElevenLabs Conversational AI