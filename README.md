# This project is dead don't try it if you do you do ...

## Google Bard AI Chat

A Python implementation for interacting with Google's Bard AI using unofficial API methods. This project provides a simple interface to send and receive data from Google Bard's language model.

## ⚠️ Important Notes

- **Regional Access**: Currently requires a United States IP address
- **VPN Requirement**: Users outside the US need to use a US-based VPN/proxy
- **Unofficial API**: Uses cookie-based authentication as no official API is currently available
- **Availability**: Access may be limited in certain regions (e.g., Iran) due to sanctions

## Prerequisites

- Python 3.6+
- US-based internet connection or VPN
- Google account with access to Bard

## Installation

1. Install the required package using pip:
```bash
# Stable version
pip install bardapi

# OR Development version
pip install git+https://github.com/dsdanielpark/Bard-API.git
```

## Authentication Setup

1. Visit [Google Bard](https://bard.google.com/)
2. Open Developer Tools (F12)
3. Navigate to: Application → Cookies
4. Find and copy the value of `__Secure-1PSID` cookie
   - This serves as your authentication token

## Usage

Replace the token in the following code with your `__Secure-1PSID` value:

```python
import bardapi
import tkinter as tk

# Authentication token
token = 'YOUR_SECURE_1PSID_VALUE'

# Create the main window
window = tk.Tk()
window.title("Bard AI Chat")
window.geometry("600x400")

# Create text widgets
output_text = tk.Text(window, height=15)
output_text.pack(pady=10)

input_text = tk.Text(window, height=5)
input_text.pack(pady=10)

def send_message():
    # Get input text
    message = input_text.get("1.0", tk.END).strip()
    
    try:
        # Initialize Bard API
        bard = bardapi.Bard(token=token)
        
        # Get response from Bard
        response = bard.get_answer(message)['content']
        
        # Display response
        output_text.insert(tk.END, f"You: {message}\n\n")
        output_text.insert(tk.END, f"Bard: {response}\n\n")
        
        # Clear input field
        input_text.delete("1.0", tk.END)
        
    except Exception as e:
        output_text.insert(tk.END, f"Error: {str(e)}\n\n")

# Create send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=10)

# Start the application
window.mainloop()
```

## Features

- Simple Tkinter-based GUI interface
- Real-time communication with Bard AI
- Error handling for failed requests
- Clear input/output display

## Troubleshooting

1. **Authentication Errors**
   - Ensure your `__Secure-1PSID` token is valid and complete
   - Check if you're connected to a US-based IP address

2. **Connection Issues**
   - Verify your internet connection
   - Check if your VPN is properly configured (if using one)
   - Ensure you have access to Google Bard in your region

3. **Package Installation Problems**
   - Try upgrading pip: `pip install --upgrade pip`
   - Install dependencies manually if needed

## Security Considerations

- Keep your `__Secure-1PSID` token secure
- Don't share your token in public repositories
- Regularly refresh your token for security

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your chosen license]

## Acknowledgments

- [Bard-API](https://github.com/dsdanielpark/Bard-API) project
- All contributors

## Contact

- GitHub: [@aliasghar1379](https://github.com/aliasghar1379)
