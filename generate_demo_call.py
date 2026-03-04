#!/usr/bin/env python3
"""Generate a realistic AI receptionist demo call using ElevenLabs TTS.

Creates a simulated phone conversation between a caller and an AI dental receptionist.
Output: demo_call.mp3
"""

import os
import json
import time
import subprocess
import tempfile
import urllib.request

API_KEY = "sk_907fd00f189be7e3e3834da25224287fdc086cd4f423e196"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Voices
RECEPTIONIST_VOICE = "EXAVITQu4vr4xnSDxMaL"  # Sarah - warm, professional female
CALLER_VOICE = "onwK4e9ZLuTAKqWW03F9"  # Daniel - casual male

# Conversation script
SCRIPT = [
    {"role": "receptionist", "text": "Thank you for calling Bright Smile Dental. This is Sarah, your after-hours assistant. How can I help you today?", "pause_after": 0.8},
    {"role": "caller", "text": "Hi, yeah, I've been having really bad tooth pain since this afternoon. It's my back molar on the left side. Is there any way I can see someone tonight?", "pause_after": 0.6},
    {"role": "receptionist", "text": "I'm sorry to hear you're in pain. Let me help you with that. On a scale of one to ten, how would you rate the pain right now?", "pause_after": 0.5},
    {"role": "caller", "text": "It's probably like a seven. It's throbbing and it's gotten worse over the last couple hours.", "pause_after": 0.5},
    {"role": "receptionist", "text": "I understand, that sounds really uncomfortable. Our office is currently closed for the evening, but I can get you scheduled as the very first appointment tomorrow morning at eight AM. In the meantime, I'd recommend taking ibuprofen for the pain and applying a cold compress to your cheek. Would you like me to book that morning appointment for you?", "pause_after": 0.6},
    {"role": "caller", "text": "Yes please, that would be great. Eight AM works.", "pause_after": 0.4},
    {"role": "receptionist", "text": "Perfect. Can I get your full name please?", "pause_after": 0.4},
    {"role": "caller", "text": "It's Michael Rodriguez.", "pause_after": 0.3},
    {"role": "receptionist", "text": "Thank you, Michael. And what's the best phone number to reach you at?", "pause_after": 0.4},
    {"role": "caller", "text": "Nine four one, five five five, oh three two one.", "pause_after": 0.3},
    {"role": "receptionist", "text": "Got it. I've scheduled you for eight AM tomorrow with Doctor Chen. You're all set, Michael. If the pain becomes severe, or you notice any swelling or fever, please don't hesitate to visit your nearest emergency room. Otherwise, we'll see you first thing in the morning. Is there anything else I can help with?", "pause_after": 0.6},
    {"role": "caller", "text": "No, that's perfect. Thank you so much, Sarah.", "pause_after": 0.3},
    {"role": "receptionist", "text": "You're welcome, Michael. Try to get some rest tonight, and we'll take great care of you tomorrow. Have a good evening!", "pause_after": 0.5},
]

def generate_speech(text, voice_id, output_path):
    """Generate speech using ElevenLabs API."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    
    data = json.dumps({
        "text": text,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": {
            "stability": 0.65,
            "similarity_boost": 0.80,
            "style": 0.15,
            "use_speaker_boost": True
        }
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers={
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    })
    
    with urllib.request.urlopen(req) as response:
        with open(output_path, 'wb') as f:
            f.write(response.read())
    
    print(f"  ✓ Generated: {os.path.basename(output_path)}")

def create_silence(duration_seconds, output_path):
    """Create a silence audio file."""
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i",
        f"anullsrc=r=44100:cl=mono",
        "-t", str(duration_seconds),
        "-q:a", "9",
        output_path
    ], capture_output=True)

def add_phone_effect(input_path, output_path):
    """Add telephone bandpass filter effect to caller audio."""
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path,
        "-af", "highpass=f=300,lowpass=f=3400,volume=0.9",
        output_path
    ], capture_output=True)

def main():
    print("🎙️  Generating AI Receptionist Demo Call")
    print("=" * 50)
    
    tmp_dir = tempfile.mkdtemp()
    segments = []
    
    # Add a brief ring tone at the start
    ring_path = os.path.join(tmp_dir, "ring.mp3")
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i",
        "sine=frequency=440:duration=0.4",
        "-f", "lavfi", "-i",
        "sine=frequency=480:duration=0.4",
        "-filter_complex", "amix=inputs=2:duration=first",
        ring_path
    ], capture_output=True)
    
    # Create ring-pause-ring pattern
    silence_short = os.path.join(tmp_dir, "silence_short.mp3")
    create_silence(0.3, silence_short)
    
    ring_pattern = os.path.join(tmp_dir, "ring_pattern.mp3")
    subprocess.run([
        "ffmpeg", "-y",
        "-i", ring_path, "-i", silence_short, "-i", ring_path, "-i", silence_short,
        "-filter_complex", "[0][1][2][3]concat=n=4:v=0:a=1",
        ring_pattern
    ], capture_output=True)
    segments.append(ring_pattern)
    
    # Add pickup pause
    pickup_pause = os.path.join(tmp_dir, "pickup_pause.mp3")
    create_silence(0.5, pickup_pause)
    segments.append(pickup_pause)
    
    # Generate each line
    for i, line in enumerate(SCRIPT):
        print(f"  Generating line {i+1}/{len(SCRIPT)}: {line['role']}")
        
        voice_id = RECEPTIONIST_VOICE if line["role"] == "receptionist" else CALLER_VOICE
        raw_path = os.path.join(tmp_dir, f"line_{i:02d}_raw.mp3")
        final_path = os.path.join(tmp_dir, f"line_{i:02d}.mp3")
        
        generate_speech(line["text"], voice_id, raw_path)
        
        # Add phone effect to caller lines
        if line["role"] == "caller":
            add_phone_effect(raw_path, final_path)
        else:
            # Keep receptionist clean (they're the AI, crystal clear)
            subprocess.run(["cp", raw_path, final_path])
        
        segments.append(final_path)
        
        # Add pause between lines
        if line.get("pause_after", 0) > 0:
            pause_path = os.path.join(tmp_dir, f"pause_{i:02d}.mp3")
            create_silence(line["pause_after"], pause_path)
            segments.append(pause_path)
        
        # Rate limit
        time.sleep(0.5)
    
    # Concatenate all segments
    print("\n📦 Combining segments...")
    concat_list = os.path.join(tmp_dir, "concat.txt")
    with open(concat_list, 'w') as f:
        for seg in segments:
            f.write(f"file '{seg}'\n")
    
    output_path = os.path.join(OUTPUT_DIR, "demo_call.mp3")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-acodec", "libmp3lame", "-q:a", "2",
        output_path
    ], capture_output=True)
    
    # Also create a version with slight background ambience
    final_output = os.path.join(OUTPUT_DIR, "demo_call_final.mp3")
    subprocess.run([
        "ffmpeg", "-y", "-i", output_path,
        "-af", "acompressor=threshold=-20dB:ratio=3:attack=5:release=50,loudnorm",
        "-acodec", "libmp3lame", "-q:a", "2",
        final_output
    ], capture_output=True)
    
    print(f"\n✅ Demo call generated: {final_output}")
    print(f"   Raw version: {output_path}")
    
    # Cleanup
    import shutil
    shutil.rmtree(tmp_dir)

if __name__ == "__main__":
    main()
