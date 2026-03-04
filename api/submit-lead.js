// Vercel serverless function - handles lead form submissions
// Sends to Telegram VoiceAgent_Dev group

const TELEGRAM_BOT_TOKEN = '7476789197:AAH8rkcvrmVYR1ktfdn265qbUZAxx6EaraM';
const TELEGRAM_CHAT_ID = '-1003701131797';

export default async function handler(req, res) {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const { name, business, phone, email, industry, message } = req.body;

    if (!name || !phone) {
      return res.status(400).json({ error: 'Name and phone required' });
    }

    const text = `🔔 *New Lead from Etheus Voice*\n\n` +
      `👤 *Name:* ${name}\n` +
      `🏢 *Business:* ${business || 'Not provided'}\n` +
      `📞 *Phone:* ${phone}\n` +
      `📧 *Email:* ${email || 'Not provided'}\n` +
      `🏭 *Industry:* ${industry || 'Not specified'}\n` +
      `💬 *Message:* ${message || 'None'}\n\n` +
      `_Submitted at ${new Date().toLocaleString('en-US', { timeZone: 'America/New_York' })}_`;

    const tgRes = await fetch(
      `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: TELEGRAM_CHAT_ID,
          text,
          parse_mode: 'Markdown',
        }),
      }
    );

    if (!tgRes.ok) {
      console.error('Telegram error:', await tgRes.text());
      return res.status(500).json({ error: 'Failed to submit' });
    }

    return res.status(200).json({ success: true });
  } catch (err) {
    console.error('Error:', err);
    return res.status(500).json({ error: 'Server error' });
  }
}
