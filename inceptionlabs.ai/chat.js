const response = await fetch('https://api.inceptionlabs.ai/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer sk_b03e2c38065dcf207b5047e47e9d1717'
  },
  body: JSON.stringify({
    model: 'mercury-2',
    messages: [
      { role: 'user', content: 'explain VLESS?' }
    ]
  })
});

const data = await response.json();
console.log(data.choices[0].message.content);