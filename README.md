# Telegram Bot with Web App Integration

This Telegram bot is designed to facilitate the purchase of items from an online store directly within the Telegram application using a Web App interface. Below is a brief overview of its functionality and structure.

## Functionality

### Starting the Bot
- Upon starting the bot, users are greeted with a welcome message and presented with a custom keyboard for navigation.

### Making Purchases
- Users can select items from the list presented in the Web App interface embedded in the chat.
- Each item has a "Buy" button associated with it, which triggers the purchase process.
- Upon clicking "Buy," an invoice is sent to the user for payment.

### Payment Handling
- After receiving the payment, the bot confirms the successful transaction and processes the order.
- It handles pre-checkout queries and successful payment notifications.

### Additional Features
- Users can access information about the store, delivery details, and leave reviews via text commands in the chat.

## File Structure

### Python Files
- `bot.py`: Contains the main logic of the Telegram bot, including message handlers, payment processing, and command functionalities.

### JS Files
- `app.js`: Handles the behavior of the Web App interface embedded in the Telegram chat.

### HTML File
- `index.html`: The main HTML file containing the structure of the Web App interface.
- `style.css`: Stylesheet for formatting the HTML content of the Web App.

### Other Files
- `README.md`: This file provides an overview of the bot's functionality, structure, and usage instructions.

## Usage

To use the bot:
1. Start a chat with the bot.
2. Navigate through the Web App interface to select items for purchase.
3. Click on the "Buy" button to initiate the purchase process.
4. Follow the prompts to complete the payment.
5. Upon successful payment, the order is confirmed, and the transaction is processed.

## Notes
- Ensure that all required tokens and URLs are properly configured in the code before deployment.
- This README file serves as a guide for understanding the bot's functionality and structure.


